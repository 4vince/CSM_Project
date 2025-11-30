from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from bisection_method import BisectionMethod
from polynomial import Polynomial

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def serve_gui():
    return send_from_directory('../gui', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../gui', path)

@app.route('/solve', methods=['POST'])
def solve_bisection():
    try:
        data = request.json
        
        # Create polynomial
        poly = Polynomial(data['degree'], data['coefficients'])
        
        # Solve using bisection method
        bisection = BisectionMethod(poly)
        result = bisection.solve(
            data['x_lower'],
            data['x_upper'], 
            data['tolerance']
        )
        
        if 'error' in result:
            return jsonify({'error': result['error']}), 400
        
        # Generate plot and convert to base64
        plot_image = generate_plot(poly, data['x_lower'], data['x_upper'], result['root'])
        result['plot_image'] = plot_image
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_plot(polynomial, x_lower, x_upper, root):
    """Generate matplotlib plot and return as base64 image"""
    # Create plot
    plt.figure(figsize=(10, 6))
    
    # Generate x values for plotting
    margin = max(1, (x_upper - x_lower) * 0.2)
    x_min = min(x_lower, root) - margin
    x_max = max(x_upper, root) + margin
    x_plot = np.linspace(x_min, x_max, 400)
    y_plot = [polynomial.evaluate(x) for x in x_plot]
    
    # Plot the function
    plt.plot(x_plot, y_plot, 'b-', linewidth=2, label=f'f(x) = {str(polynomial)}')
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # Mark the root
    plt.plot(root, polynomial.evaluate(root), 'ro', markersize=8, label=f'Root: {root:.6f}')
    
    # Mark initial bounds
    plt.axvline(x=x_lower, color='g', linestyle='--', alpha=0.7, label=f'Initial lower: {x_lower}')
    plt.axvline(x=x_upper, color='r', linestyle='--', alpha=0.7, label=f'Initial upper: {x_upper}')
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Bisection Method - Function Plot')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    
    # Convert plot to base64 string
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()  # Close the figure to free memory
    
    return f"data:image/png;base64,{image_base64}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)