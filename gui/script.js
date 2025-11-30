// Create coefficient inputs based on degree
function createCoefficientInputs() {
    const degree = parseInt(document.getElementById('degree').value);
    const container = document.getElementById('coefficients-container');
    
    if (degree < 0 || degree > 20) {
        alert('Degree must be between 0 and 20');
        return;
    }
    
    container.innerHTML = '<h3>Enter Coefficients:</h3>';
    
    for (let i = degree; i >= 0; i--) {
        const div = document.createElement('div');
        div.className = 'coefficient-input';
        
        let label;
        if (i === degree) label = `x^${i}:`;
        else if (i === 1) label = 'x:';
        else if (i === 0) label = 'Constant:';
        else label = `x^${i}:`;
        
        div.innerHTML = `
            <label>${label}</label>
            <input type="number" id="coeff_${i}" value="${i === degree ? 1 : 0}" step="any">
        `;
        container.appendChild(div);
    }
}

// Solve using bisection method
async function solveBisection() {
    try {
        // Get input values
        const degree = parseInt(document.getElementById('degree').value);
        const x_lower = parseFloat(document.getElementById('x_lower').value);
        const x_upper = parseFloat(document.getElementById('x_upper').value);
        const tolerance = parseFloat(document.getElementById('tolerance').value);
        
        // Get coefficients
        const coefficients = [];
        for (let i = degree; i >= 0; i--) {
            const coeff = parseFloat(document.getElementById(`coeff_${i}`).value) || 0;
            coefficients.push(coeff);
        }
        
        // Create request data
        const requestData = {
            degree: degree,
            coefficients: coefficients,
            x_lower: x_lower,
            x_upper: x_upper,
            tolerance: tolerance
        };
        
        // Show loading
        document.getElementById('plot-container').innerHTML = '<p>Generating plot...</p>';
        
        // Send to Python backend
        const response = await fetch('http://localhost:5000/solve', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestData)
        });
        
        const result = await response.json();
        
        if (result.error) {
            showError(result.error);
        } else {
            displayResults(result);
        }
        
    } catch (error) {
        showError('Connection error: ' + error.message);
    }
}

// Display results with plot image
function displayResults(result) {
    const resultsDiv = document.getElementById('results');
    const errorDiv = document.getElementById('error');
    
    errorDiv.style.display = 'none';
    resultsDiv.style.display = 'block';
    
    // Store result globally for potential future use
    window.lastResult = result;
    
    // Display iteration table
    let tableHtml = `
        <h3>Iteration Progress</h3>
        <table class="iteration-table">
            <thead>
                <tr>
                    <th>Iteration</th>
                    <th>x_lower</th>
                    <th>f(x_lower)</th>
                    <th>x_upper</th>
                    <th>f(x_upper)</th>
                    <th>midpoint</th>
                    <th>f(midpoint)</th>
                    <th>Error %</th>
                </tr>
            </thead>
            <tbody>
    `;
    
    result.iterations_data.forEach(iter => {
        tableHtml += `
            <tr>
                <td>${iter.iteration}</td>
                <td>${iter.x_lower.toFixed(6)}</td>
                <td>${iter.f_x_lower.toFixed(6)}</td>
                <td>${iter.x_upper.toFixed(6)}</td>
                <td>${iter.f_x_upper.toFixed(6)}</td>
                <td>${iter.midpoint.toFixed(6)}</td>
                <td>${iter.f_midpoint.toFixed(6)}</td>
                <td>${iter.relative_error.toFixed(6)}</td>
            </tr>
        `;
    });
    
    tableHtml += '</tbody></table>';
    document.getElementById('iteration-table').innerHTML = tableHtml;
    
    // Display final result
    const finalHtml = `
        <div class="final-result">
            <h3>Final Result</h3>
            <p><strong>Root found:</strong> ${result.root.toFixed(8)}</p>
            <p><strong>f(root):</strong> ${result.f_root.toFixed(8)}</p>
            <p><strong>Iterations:</strong> ${result.iterations}</p>
            <p><strong>Final Error:</strong> ${result.final_error.toFixed(8)}%</p>
        </div>
    `;
    document.getElementById('final-result').innerHTML = finalHtml;
    
    // Display plot image
    if (result.plot_image) {
        document.getElementById('plot-container').innerHTML = `
            <h3>Function Plot</h3>
            <div class="plot-image">
                <img src="${result.plot_image}" alt="Function Plot" style="max-width: 100%; height: auto;">
            </div>
        `;
    } else {
        document.getElementById('plot-container').innerHTML = '<p><em>Plot not available</em></p>';
    }
}

// Show error message
function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    document.getElementById('results').style.display = 'none';
    document.getElementById('plot-container').innerHTML = '';
}

// Clear all inputs
function clearAll() {
    document.getElementById('degree').value = '3';
    document.getElementById('x_lower').value = '1';
    document.getElementById('x_upper').value = '3';
    document.getElementById('tolerance').value = '0.1';
    document.getElementById('coefficients-container').innerHTML = '';
    document.getElementById('results').style.display = 'none';
    document.getElementById('error').style.display = 'none';
    document.getElementById('plot-container').innerHTML = '';
    createCoefficientInputs();
}

// Initialize coefficient inputs when page loads
window.onload = createCoefficientInputs;