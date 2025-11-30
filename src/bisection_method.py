"""
Bisection Method implementation for finding roots of polynomials
"""

class BisectionMethod:
    def __init__(self, polynomial):
        self.polynomial = polynomial
        self.iterations_data = []
    
    def solve(self, x_lower, x_upper, tolerance, max_iterations=100):
        """
        Solve the polynomial using Bisection Method
        """
        # Validate inputs
        if x_lower >= x_upper:
            return {"error": "Lower bound must be less than upper bound"}
        
        f_lower = self.polynomial.evaluate(x_lower)
        f_upper = self.polynomial.evaluate(x_upper)
        
        if f_lower * f_upper > 0:
            return {"error": "Function must have opposite signs at lower and upper bounds"}
        
        if tolerance <= 0 or tolerance >= 100:
            return {"error": "Tolerance must be between 0 and 100"}
        
        self.iterations_data = []
        iteration = 0
        prev_midpoint = None
        relative_error = 100
        
        print(f"\n{'Iteration':<10} {'x_lower':<12} {'f(x_lower)':<12} {'x_upper':<12} {'f(x_upper)':<12} {'midpoint':<12} {'f(midpoint)':<12} {'Error %':<12}")
        print("-" * 100)
        
        while iteration < max_iterations and relative_error >= tolerance:
            midpoint = (x_lower + x_upper) / 2
            f_midpoint = self.polynomial.evaluate(midpoint)
            
            # Calculate relative error
            if prev_midpoint is not None and abs(prev_midpoint) > 1e-12:
                relative_error = abs((midpoint - prev_midpoint) / midpoint) * 100
            else:
                relative_error = 100
            
            # Store iteration data
            iteration_data = {
                'iteration': iteration + 1,
                'x_lower': x_lower,
                'f_x_lower': f_lower,
                'x_upper': x_upper,
                'f_x_upper': f_upper,
                'midpoint': midpoint,
                'f_midpoint': f_midpoint,
                'relative_error': relative_error
            }
            self.iterations_data.append(iteration_data)
            
            # Print current iteration
            print(f"{iteration+1:<10} {x_lower:<12.6f} {f_lower:<12.6f} {x_upper:<12.6f} {f_upper:<12.6f} {midpoint:<12.6f} {f_midpoint:<12.6f} {relative_error:<12.6f}")
            
            # Check for root found exactly
            if abs(f_midpoint) < 1e-12:
                break
            
            # Update bounds
            if f_lower * f_midpoint < 0:
                x_upper = midpoint
                f_upper = f_midpoint
            else:
                x_lower = midpoint
                f_lower = f_midpoint
            
            prev_midpoint = midpoint
            iteration += 1
        
        return {
            'root': midpoint,
            'f_root': f_midpoint,
            'iterations': iteration + 1,
            'final_error': relative_error,
            'iterations_data': self.iterations_data
        }
    
    def plot_function(self, x_lower, x_upper, root=None):
        """Plot the polynomial function and mark the root if found"""
        try:
            import matplotlib.pyplot as plt
            import numpy as np
            
            # Create a range of x values
            x_min = min(x_lower, x_upper) - 1
            x_max = max(x_lower, x_upper) + 1
            x = np.linspace(x_min, x_max, 400)
            y = [self.polynomial.evaluate(xi) for xi in x]
            
            plt.figure(figsize=(12, 8))
            
            # Plot the function
            plt.plot(x, y, 'b-', linewidth=2, label=str(self.polynomial))
            plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
            plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
            
            # Mark the initial bounds
            plt.axvline(x=x_lower, color='g', linestyle='--', alpha=0.7, label=f'Initial lower bound: {x_lower:.4f}')
            plt.axvline(x=x_upper, color='r', linestyle='--', alpha=0.7, label=f'Initial upper bound: {x_upper:.4f}')
            
            # Mark the root if found
            if root is not None:
                plt.plot(root, self.polynomial.evaluate(root), 'ro', markersize=8, 
                        label=f'Root: {root:.6f}')
            
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Bisection Method - Function Plot')
            plt.grid(True, alpha=0.3)
            plt.legend()
            plt.tight_layout()
            plt.show()
            
        except ImportError:
            print("Matplotlib is not installed. Cannot display plot.")
            print("Install it using: pip install matplotlib")
    
    def get_iteration_count(self):
        return len(self.iterations_data)