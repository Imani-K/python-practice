 #it keeps asking until a valid input is given
while True:
    try:
        #Asks the user to enter an integer
        num = int(input("Enter the number: "))
        fact = 1

        #checks if the number is negative
        if num < 0:
            print("The factorial of a negative number is impossible. Try again")
            continue #Used to ask again

        #States the factorial of 0 is always 1
        elif num == 0:
            print("Factorial of 0 is 1")

      #For all positive numbers,compute factorial using a loop
        else:
            for i in range(1,num+1):
                fact = fact * i
            print("The factorial of", num, " is :", fact)

        break # Exit the loop if is valid and computation is done
    except ValueError:
        #Handles the code is the input is not an integer
        print("Invalid input. Try again")
