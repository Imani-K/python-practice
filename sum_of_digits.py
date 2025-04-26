# Function to calculate the sum of digits of a number using recursion
def sum_of_digits(number):
    #if the number is 0, the sum is 0
    if number == 0:
        return 0
    # Recursive case: take the last digit and add it to the sum of the remaining digits
    return (number % 10) + sum_of_digits(number // 10)

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Call the function to calculate the sum of digits
result = sum_of_digits(number)

# Prints the result
print(f"Sum of digits of {number} is {result}")
