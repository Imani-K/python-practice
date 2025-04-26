#Functions Body
def add_numbers(n1,n2):
    # This function takes two numbers and returns their sum
    sum = n1 + n2
    # Return the result to the caller
    return sum

#Main Body
if __name__ == '__main__':
    # This block runs only if the script is executed directly
  n1 = float(input("Enter the first number: "))
  n2 = float(input("Enter the second number: "))
  addition = add_numbers(n1,n2)
    #This prints the results to the screen
print("The sum is" ,addition)

