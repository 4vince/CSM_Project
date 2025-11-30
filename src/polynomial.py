"""
Polynomial class for representing and evaluating polynomials
"""
import numpy as np

class Polynomial:
    def __init__(self, degree, coefficients):
        self.degree = degree
        self.coefficients = coefficients
    
    def evaluate(self, x):
        """Calculate f(x) for the polynomial"""
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** (self.degree - i))
        return result
    
    def __str__(self):
        """String representation of the polynomial"""
        terms = []
        for i, coeff in enumerate(self.coefficients):
            power = self.degree - i
            if coeff == 0:
                continue
            if power == 0:
                terms.append(f"{coeff:+}")
            elif power == 1:
                terms.append(f"{coeff:+}x")
            else:
                terms.append(f"{coeff:+}x^{power}")
        
        # Remove the leading '+' if present
        if terms and terms[0].startswith('+'):
            terms[0] = terms[0][1:]
        
        return "f(x) = " + " ".join(terms) if terms else "f(x) = 0"
    
    def get_derivative(self):
        """Return the derivative of the polynomial"""
        if self.degree == 0:
            return Polynomial(0, [0])
        
        derivative_coeffs = []
        for i, coeff in enumerate(self.coefficients[:-1]):  # Exclude constant term
            power = self.degree - i
            derivative_coeffs.append(coeff * power)
        
        return Polynomial(self.degree - 1, derivative_coeffs)