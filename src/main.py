"""
Main application for Bisection Method Calculator
"""

def display_welcome():
    print("=" * 60)
    print("          BISECTION METHOD CALCULATOR")
    print("=" * 60)
    print("This application finds roots of polynomials using the Bisection Method")
    print()

def get_polynomial_input():
    """Get polynomial input from user"""
    print("=== Polynomial Input ===")
    
    while True:
        try:
            degree = int(input("Enter the degree of the polynomial (max 20): "))
            if degree < 0 or degree > 20:
                print("Degree must be between 0 and 20")
                continue
            break
        except ValueError:
            print("Please enter a valid integer")
    
    coefficients = []
    print("Enter coefficients from highest to lowest degree:")
    for i in range(degree, -1, -1):
        while True:
            try:
                if i == degree:
                    prompt = f"Coefficient for x^{i}: "
                elif i == 1:
                    prompt = f"Coefficient for x: "
                elif i == 0:
                    prompt = f"Constant term: "
                else:
                    prompt = f"Coefficient for x^{i}: "
                
                coeff = int(input(prompt))
                coefficients.append(coeff)
                break
            except ValueError:
                print("Please enter a valid integer")
    
    from polynomial import Polynomial
    return Polynomial(degree, coefficients)

def get_valid_bounds(polynomial):
    """Get bounds input from user with validation for opposite signs"""
    print("\n=== Bounds Input ===")
    
    while True:
        try:
            x_lower = float(input("Enter lower bound (x_lower): "))
            x_upper = float(input("Enter upper bound (x_upper): "))
            
            if x_lower >= x_upper:
                print("Error: Lower bound must be less than upper bound")
                print("Please try again.\n")
                continue
            
            # Check if function values have opposite signs
            f_lower = polynomial.evaluate(x_lower)
            f_upper = polynomial.evaluate(x_upper)
            
            print(f"f({x_lower}) = {f_lower:.6f}")
            print(f"f({x_upper}) = {f_upper:.6f}")
            
            # Check if either bound is exactly a root
            if f_lower == 0:
                print(f"Note: Lower bound x = {x_lower} is already a root!")
                print("The bisection method requires bounds with opposite signs.")
                print("Please choose bounds that bracket an unknown root.\n")
                continue
            elif f_upper == 0:
                print(f"Note: Upper bound x = {x_upper} is already a root!")
                print("The bisection method requires bounds with opposite signs.")
                print("Please choose bounds that bracket an unknown root.\n")
                continue
            
            # Check for proper opposite signs
            if f_lower * f_upper > 0:
                print("Error: f(x_lower) and f(x_upper) have the same sign.")
                print("The bisection method requires opposite signs at the bounds.")
                print("Please choose different bounds.\n")
                continue
            else:
                return x_lower, x_upper
            
        except ValueError:
            print("Please enter valid numbers")
            
def get_tolerance_input():
    """Get stopping criterion input from user"""
    print("\n=== Stopping Criterion ===")
    
    while True:
        try:
            tolerance = float(input("Enter tolerance for relative error (%): "))
            
            if tolerance <= 0 or tolerance >= 100:
                print("Tolerance must be between 0 and 100")
                continue
            
            break
        except ValueError:
            print("Please enter a valid number")
    
    return tolerance

def main():
    """Main application loop"""
    display_welcome()
    
    while True:
        try:
            # Get polynomial
            poly = get_polynomial_input()
            print(f"\nYour polynomial: {poly}")
            
            # Get bounds with validation (now returns only 2 values)
            x_lower, x_upper = get_valid_bounds(poly)
            
            # Get tolerance
            tolerance = get_tolerance_input()
            
            # Solve using bisection method
            from bisection_method import BisectionMethod
            bisection = BisectionMethod(poly)
            print(f"\nSolving using Bisection Method...")
            print(f"Target relative error: {tolerance}%")
            
            result = bisection.solve(x_lower, x_upper, tolerance)
            
            if 'error' in result:
                print(f"Error: {result['error']}")
                continue
            
            # Display results
            print("\n" + "=" * 60)
            print("                    RESULTS")
            print("=" * 60)
            print(f"Polynomial: {poly}")
            print(f"Root found: {result['root']:.8f}")
            print(f"f(root): {result['f_root']:.8f}")
            print(f"Number of iterations: {result['iterations']}")
            print(f"Final relative error: {result['final_error']:.8f}%")
            
            # Ask if user wants to see the plot
            plot_choice = input("\nDo you want to see the function plot? (y/n): ").lower()
            if plot_choice == 'y':
                bisection.plot_function(x_lower, x_upper, result['root'])
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
        
        # Ask if user wants to solve another problem
        another = input("\nDo you want to solve another problem? (y/n): ").lower()
        if another != 'y':
            print("Thank you for using Bisection Method Calculator!")
            break

if __name__ == "__main__":
    main()