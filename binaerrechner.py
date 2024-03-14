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
    if decimal == 0:
        return "0"

    binary = ""
    while decimal > 0:
        rest = decimal % 2
        binary = str(rest) + binary
        decimal = decimal // 2
    return binary

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for bit in binary:
        if bit == '1':
            decimal += 2 ** power
        power -= 1
    return decimal
 


while True:
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
    
    try:
        choice >= 1 <= 7   # control if user chose the correct option
    except:
        error = True


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
        print(f"The result of the addition of {binary1} and {binary2} is:")
    
    #subtraction of binary1 and binary2 #
    elif choice == '4':
        print(f"The result of the subtraction of {binary1} and {binary2} is:")
    
    # multiplying binary1 with binary2 #
    elif choice == '5':
        print(f"The result of the multiplication of {binary1} and {binary2} is:")
    
    # deviding binary1 by binary2 #
    elif choice == '6':
        print(f"The result of the division of {binary1} and {binary2} is:")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    break