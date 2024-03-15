#############################################################
##                                                         ##
##                                                         ##
##                                                         ##
##                                                         ##
##                    Binary-Calculator                    ##
##                                                         ##
##                                                         ##
##                                                         ##
##                                                         ##
#############################################################
#### Author: Melvin Suljanovic                           ####
#### Date: 14.03.2024                                    ####
#### Brief: A Calculator to convert binary numbers to    ####
####        decimal numbers and decimal numbers to       ####
####        binary numbers                               ####
####        and                                          ####
####        Adding, subtracting, multiplying and dividing#### 
####        of two binary numbers                        ####
#############################################################

# FUNCTIONS #

def decimal_to_binary(decimal):
    if decimal == 0:                # if decimal number = 0, binary number also 0
        return "0"

    binary = ""
    while decimal > 0:              
        rest = decimal % 2              # decimal number / 2 = new decimal number + rest(1 or 0) 
        binary = str(rest) + binary     # rest gets safed to binary from bit 0 - x
        decimal = decimal // 2          # new decimal number gets set as decimal number
    return binary                       # binary number from the rest from every 

def binary_to_decimal(binary):
    decimal = 0                         # local variable decimal ist set
    power = len(binary) - 1             # the power (of two) is set to be the length of the binary code minus one 
    for bit in binary:                  # every bit in the binary number is looked through and 
        if bit == '1':                  # if its '1' the two to the set power for the bit gets added to the decimal number
            decimal += 2 ** power
        power -= 1
    return decimal                      #after power < 0 the decimal number is returned 
 
def bin_add(binary1, binary2):
    return bin(int(binary1, 2) + int(binary2, 2))[2:]

def bin_sub(binary1, binary2):
    return bin(int(binary1, 2) - int(binary2, 2))[2:]

def bin_multi(binary1, binary2):
    return bin(int(binary1, 2) * int(binary2, 2))[2:]

def bin_div(binary1, binary2):
    return bin(int(binary1, 2) // int(binary2, 2))[2:]

while True:
    error = False
    # main menu setup #
    print("1. Convert decimal number to binary number")
    print("2. Convert binary number to binary number")
    print("3. Binary addition")
    print("4. Binary subtraction")
    print("5. Binary multiplication")
    print("6. Binary division")
    print("7. Exit")
    # user input - main menu #
    choice = input("Please choose an option (1-7): ")

    # getting to chosen option with if, elif, else #
    if choice == '7':
        break               # "breaking" the loop to finish programm

    elif choice == '1':
        decimal = int(input("Please input a decimal number: "))
        print(f"The binary number to {decimal} is: ", decimal_to_binary(decimal))

    elif choice == '2':
        binary = input("Please input a binary number: ")
        print(f"The kdecimal number to {binary} is: ", binary_to_decimal(binary))

    # user input for option 3 to 6 #
    else:
        binary1 = input("Please input first binary number: ")      # choice 3-6 need two binary numbers
        binary2 = input("Please input secon binary number: ")     # to not repeat asking for numbers they are asked after     
                                                                    # choice 1, 2, 7
    # addition of binary1 and binary2 #
    if choice == '3':
        print(f"The result of the addition of {binary1} and {binary2} is:", bin_add(binary1, binary2))
    
    #subtraction of binary1 and binary2 #
    elif choice == '4':
        print(f"The result of the subtraction of {binary1} and {binary2} is:", bin_sub(binary1, binary2))
    
    # multiplying binary1 with binary2 #
    elif choice == '5':
        print(f"The result of the multiplication of {binary1} and {binary2} is:", bin_multi(binary1, binary2))
    
    # deviding binary1 by binary2 #
    elif choice == '6':
        
        try:
            print(f"The result of the division of {binary1} and {binary2} is:", bin_div(binary1, binary2))
        except:
            print("Ivalid User Input. You can not divide by zero!")
            error = True
    
    while True:
        ask_continue = input("Do you want to choose a new option? (yes/no): ")
        try:
            if ask_continue.lower() == 'no':
                break
            elif ask_continue.lower() == 'yes':
                break
            else:
                print("Error: Invalid input. Please enter yes or no.")
        except Exception as e:
            print("An error occurred:", e)
    
    if ask_continue.lower() == 'no':
        break

print("Thanks for using binaerrechner.py!!!")
input(print("Press a button to close the programm."))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
