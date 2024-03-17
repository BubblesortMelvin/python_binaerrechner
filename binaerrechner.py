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
# Function to convert decimal numbers to binary numbers #
def decimal_to_binary(decimal):
    if decimal == 0:                                                            # if decimal number = 0, binary number also 0
        return "0"

    #Setup local variables#
    abs_decimal = abs(decimal)                                                  # sets the absolute Number after an input (negative --> positive)
    num_bits = len(bin(abs_decimal)) - 2                                        # sets the lenght of the converted decimal number without 0b (start of each python binary number) 
    binary = ""                                                                 # sets the variable binary

    for i in range(num_bits):                                                   # calculates for each bit the binary number
        rest = abs_decimal % 2                                                  # "rest" is the number (0 or 1) after dividing the decomal number 5/2= 2 rest 1
        binary = str(rest) + binary                                             # rest gets safed to binary from right to left last for-loop ->1010101010<- first for-loop
        abs_decimal //= 2                                                       # resets the decimal  number to the new calculated number without rest (5/2 = 2 rest 1 --> 2 gets safed for next loop)

    # cases for decimal >= 0, decimal < 0 #
    if decimal < 0:
        binary = '-0' + binary                                                  # adds a '-0' in front of binary --> marks negative number + aesthetic purpose 
    else:
        binary = '0' + binary                                                   # adds a '0' in front of binary --> aesthetic purpose

    return binary

# Function to convert binary numbers to decimal numbers #
def binary_to_decimal(binary):
    #setup local variables#
    decimal = 0                                                                 # local variable decimal ist set
    power = len(binary) - 1                                                     # the power (of two) is set to be the length of the binary code minus one 
    

    for bit in binary:                                                          # every bit in the binary number is looked through and 
        if bit == '1':                                                          # if its '1' the two to the set power for the bit gets added to the decimal number
            decimal += 2 ** power
        power -= 1
    return decimal                                                              # after power < 0 the decimal number is returned 

# Calc-Function to add a binary number with another # 
def bin_add(binary1, binary2):
    return bin(int(binary1, 2) + int(binary2, 2))[2:]                           # two binary numbers are converted to integer 
                                                                                # then added together and then converted to binary

# Calc-Function to subtract a binary number with another #
def bin_sub(binary1, binary2):
    result = int(binary1, 2) - int(binary2, 2)                                  #binary numbers are converted to integer and subtracted
    if result < 0:                                                              #analysis of result 
        return '-0' + bin(abs(result))[2:]                                      #returns result smaller then 0 adds a "-0" infront of binary number
    else:
        return bin(result)[2:]                                                  # returns every other result 

# Calc-Function to multiply two binary numbers #
def bin_multi(binary1, binary2):
    return bin(int(binary1, 2) * int(binary2, 2))[2:]                           # returning result of "binary numbers are converted to integer, multiplied and converted to binary numbers again" 

# Calc-Function to divide two binary numbers #
def bin_div(binary1, binary2):
    return bin(int(binary1, 2) // int(binary2, 2))[2:]                          # returning result of "binary numbers are converted to integer, divided and converted to binary numbers again"

# UI-Function to resume or quit programm #
def ask_to_continue():
    while True:
        ask_continue = input("Do you want to choose a new option? (yes/no): ")  # User Input
        try:
            if ask_continue.lower() == 'no':                                    # If User Input = "no", "NO", "No", "nO" 
                return False                                                    # return False --> main while loop gets broken through 
            elif ask_continue.lower() == 'yes':                                 # If User Input = any Version of "yes"        
                return True                                                     # return True --> main while loop continues
            else:
                print("Error: Invalid input. Please enter yes or no.")          # if user input != yes or no--> Error 
        except Exception as e:                                                  # in case DAU gives unimaginable input 
            print("An error occurred:", e)

# Test-Function to control binary number input #
def is_it_binary(binnum):
    try:
        int(binnum, 2)                                                          # tries to convert binary number to integer
        return True                                                             # if possible continues loop
    except ValueError:                                                          # if error returns false --> skips to aski_to_continue
        print("Error: The used number not binary. Please only use 0 and 1")
        return False
    
# MAIN PROGRAMM #
while True:
    # main menu setup #
    print("""1. Convert decimal number to binary number
2. Convert binary number to binary number
3. Binary addition
4. Binary subtraction
5. Binary multiplication
6. Binary division
7. Quit programm""")
    print("")
    # user input - main menu #
    
    while True:
        choice = input("Please enter a number from 1 to 7: ")
        try:
            choice = int(choice)    
            if not 1 <= choice <= 7:
                print("The entered number is not within the valid range of 1 to 7.")
                break
            else:
                print("Valid input!")
                break

        except:
            print("Invalid input. Please enter an integer.")
            break
    

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
            if not is_it_binary(binary1):                               #first control
                break
            binary2 = input("Please input secon binary number: ")       # to not repeat asking for numbers they are asked after     
            if not is_it_binary(binary2):                               # second control
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

