# Try block is used to catch any errors that may happen during user input and conversion
try:
    # Ask the user to enter a number and convert the input to an integer
    Num = int(input("Enter the number: "))
    # Calculate the remainder when Num is divided by 2
    flag = Num%2
    # If the remainder is 0, the number is even
    if flag == 0:
        print(Num, "is an even number.")
    # If the remainder is 1, the number is odd
    elif flag ==  1:
        print(Num, "is an odd number.")
except ValueError:
    print("Invalid input.")
