#Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1 # defines the factorial of 0 or 1 is 1
    else:
        return n * factorial(n - 1)

# Main program
while True:
    try:
        # Ask the user for input
        num = int(input("Enter a non-negative integer: "))

        # Validate that the number is not negative
        if num < 0:
            print("Factorial is not defined for negative numbers. Try again.\n")
            continue

        # Call the recursive function and display the result
        print("Factorial of", num, "is:", factorial(num))
        break  # Exit the loop after successful calculation

    except ValueError:
        # Handle non-integer input
        print("Invalid input. Please enter a valid integer.")

