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

    #Setup local variables#
    abs_decimal = abs(decimal)
    num_bits = len(bin(abs_decimal)) - 2
    binary = ""

    for i in range(num_bits):
        rest = abs_decimal % 2 
        binary = str(rest) + binary
        abs_decimal //= 2

    # cases for decimal >= 0, decimal < 0 #
    if decimal < 0:
        binary = '-0' + binary
    else:
        binary = '0' + binary

    return binary

def binary_to_decimal(binary):
    #setup local variables#
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

def ask_to_continue():
    while True:
        ask_continue = input("Do you want to choose a new option? (yes/no): ")
        try:
            if ask_continue.lower() == 'no':
                return False
            elif ask_continue.lower() == 'yes':
                return True
            else:
                print("Error: Invalid input. Please enter yes or no.")
        except Exception as e:
            print("An error occurred:", e)

def is_it_binary(binnum):
    try:
        int(binnum, 2)
        return True
    except ValueError:
        print("Error: One or both numbers are not binary. Please only use 0 and 1")
        return False
    

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
    choice = int(input("Please choose an option (1-7): "))

    if choice < 1 or choice > 7:
        print("Error: Invalid Input. Please choose a number from 1 to 7. ")

    # getting to chosen option with if, elif, else #
    if choice == 7:
        break               # "breaking" the loop to finish programm

    elif choice == 1:
        while True:
            try:
                decimal = int(input("Please input a decimal number: "))
                print(f"The binary number to {decimal} is: ", decimal_to_binary(decimal))
                break
            except:
                print("Invalid User Input: Please enter a decimal number.")
                break

            

    elif choice == 2:
        while True:
            binary = input("Please input a binary number: ")
            if not is_it_binary(binary):
                break
            print(f"The decimal number to {binary} is: ", binary_to_decimal(binary))
            break 

    if choice in [3, 4, 5, 6]:
        while True:
    # user input for option 3 to 6 #
        
            binary1 = input("Please input first binary number: ")       # choice 3-6 need two binary numbers
            binary2 = input("Please input secon binary number: ")       # to not repeat asking for numbers they are asked after     
            if not is_it_binary(binary1) or not is_it_binary(binary2):  # is binary number a binary number
                break                                                   #if not skip choice 3-6
    # addition of binary1 and binary2 #
            if choice == 3:
                print(f"The result of the addition of {binary1} and {binary2} is:", bin_add(binary1, binary2))
    
    #subtraction of binary1 and binary2 #
            elif choice == 4:
                print(f"The result of the subtraction of {binary1} and {binary2} is:", bin_sub(binary1, binary2))
    
    # multiplication of binary1 and binary2 #
            elif choice == 5:
                print(f"The result of the multiplication of {binary1} and {binary2} is:", bin_multi(binary1, binary2))
    
    # division of binary1 and binary2 #
            elif choice == 6:
                try:
                    print(f"The result of the division of {binary1} and {binary2} is:", bin_div(binary1, binary2))
                except:
                    print("Ivalid User Input. You can not divide by zero!")
                
    
            break 
    
    if not ask_to_continue():
        break

print("Thanks for using binaerrechner.py!!!")
input("Press a button to close the programm.")
    
    
    
    
# To-Do Liste:
# try except: is binary number a binary number?
# try except: is decimal number a decimal number?
#def ask to continue as function --> works
    
    
    
    
    
    
    
    
    
    
    
    
