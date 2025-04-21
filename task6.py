import math


try:
    num = float(input("Enter a positive number: "))

    if num <= 0:
        print("Please enter a number greater than 0 for valid log and square root calculations.")
    else:
        # Calculations
        sqrt_val = math.sqrt(num)
        log_val = math.log(num)
        sine_val = math.sin(num)

        # Display results
        print(f"\nResults for the number {num}:")
        print(f"Square root: {sqrt_val}")
        print(f"Natural logarithm (ln): {log_val}")
        print(f"Sine (in radians): {sine_val}")

except ValueError:
    print("Invalid input. Please enter a valid numeric value.")
