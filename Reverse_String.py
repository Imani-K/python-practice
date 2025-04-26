#Function to reverse a string using slicing
def reverse_string(s):
    return s[::-1]# Returns the string reversed from last to first
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)

print("Reversed string: ", reversed_string)

#Starts a loop to validate the user's input
while True:
    #Prompts the user again expecting letters only
    input_string = input("Enter a string (Letters only): ")

    #Checks if the input is empty
    if not input_string.strip():
        print("Input cannot be empty.Try again.")
        continue# begins the loop

    #checks if the input contains letters
    if not input_string.isalpha():
        print("Invalid input. Please enter letters only.")
        continue#Ask for input again

    #if the input is valid, reverse of the input is excecuted.
    reversed_string = reverse_string(input_string)
    print("Reversed string:", reversed_string)
    break# Exits the loop since the input is valid.
