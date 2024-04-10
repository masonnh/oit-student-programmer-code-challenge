#### Decimal to Roman Numeral Converter ####
### Author: Mason Hunter ###
### Date: 4/10/2024 ###

# a list of letters found in roman numerals
roman_letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

# function to convert a roman numeral to a decimal
def roman_to_decimal(roman_numeral):

    if roman_checker(roman_numeral) == False:      # check if the roman numeral is valid
        return False

    print("Valid roman numeral, proceeding to conversion...\n")

    roman_numeral = roman_numeral.upper()       # set the roman numeral to all caps for standardization

    # initialize variables
    previous_letter = ''            # tracks the previous letter to the current letter
    decimal = 0                     # the decimal equivalent of the roman numeral
    letter_decimal = 0              # the decimal equivalent of the current letter
    previous_letter_decimal = 0     # the decimal equivalent of the previous letter
    skip_next = False               # skips the next letter in the loop when True
    count = 0                       # counts the number of iterations the loop has run

    for letter in roman_numeral:
        # convert the roman numeral letters to their decimal equivalent
        letter_decimal = roman_to_decimal_letter(letter)
        previous_letter_decimal = roman_to_decimal_letter(previous_letter)

        # skip over the first letter in order to populate the previous_letter variable correctly
        if count == 0:
            skip_next = True

        # this logic is entered after using subtractive notation, since the current letter is already accounted for
        # this skips the letter that was just subtracted and proceeds to the next letter, keeping track of the new previous letter
        if skip_next:
            skip_next = False
            previous_letter = letter
            count += 1
            continue

        # handle subtrative notation
        # If symbol A is less than the symbol immediately following it (B), A is subtracted from B and AB is treated as a single unit to add to the total.
        # skip_next is set to true to skip the next letter in the loop, as it is already accounted for in subtractive notation
        if previous_letter_decimal < letter_decimal:
            decimal += (letter_decimal - previous_letter_decimal)
            skip_next = True

        # handle additive notation
        # Normally, values are combined by adding the values of the symbol together.
        # previous_letter_decimal is added here because we are acutally basing our addition on that number and only using letter_decimal for subtractive notation
        else:
            decimal += previous_letter_decimal

        # update previous_letter before entering the next loop and update the count
        previous_letter = letter
        count += 1

    # because we based our addition on the previous letter, we need to manually add the last letter, but only if it is not used in subtractive notation
    if letter_decimal <= previous_letter_decimal:
        decimal += letter_decimal

    # return the result
    return decimal

# function that takes a single roman numeral letter and returns its decimal equivalent
def roman_to_decimal_letter(letter):
    # check that it is a valid roman numeral
    if roman_checker(letter) == False:
        return False

    letter = letter.upper()

    if letter == 'I': return(1)
    if letter == 'V': return(5)
    if letter == 'X': return(10)
    if letter == 'L': return(50)
    if letter == 'C': return(100)
    if letter == 'D': return(500)
    if letter == 'M': return(1000)

    # return a 0 for any other letter
    return 0

# checks that a parameter is a valid roman numeral string
def roman_checker(roman_numeral):
    # check if roman_numeral is a string
    if (type(roman_numeral) != str):
        print("Not a valid roman numeral -- not a string")
        return False
    
    # set roman_numeral to all caps
    roman_numeral = roman_numeral.upper()

    # check if roman_numeral is a valid roman numeral (only contains letters found in roman numerals)
    for letter in roman_numeral:
        if letter not in roman_letters:
            print("Not a valid roman numeral -- invalid letter")
            return False

    return True

# function to convert a decimal to a roman numeral
def decimal_to_roman(decimal_number):

    # check that the decimal number is a valid integer
    if (type(decimal_number) != int):
        print("Not a valid decimal number -- not an integer")
        return False
    
    print('Valid decimal number, proceeding to conversion...\n')

    
    decimal_str = str(decimal_number)   # convert the decimal number to a string
    size = len(decimal_str)             # keep track of what place we are in the decimal number (thousands, hundreds, tens, ones)

    roman_numeral = ''                  # initialize the roman numeral

    
    for c in decimal_str:               # loop through each place in the decimal number
        
        if size == 4:                   # if we are in the thousands place
            for i in range(int(c)):     # loop through however many thousands we have
                roman_numeral += 'M'    # we can repeatedly add 'M' to the roman numeral because the highest number the archeologists found was 3999
            size -= 1                   # subtract 1 from the size so that in the next iteration, we know we are in the hundreds place
            continue                    # skip to the next iteration of the for loop

        elif size == 3:                               # if we are in the hundreds place
            if int(c) < 4:                          # this one is handled in 4 sections, starting with less than 4
                for i in range(int(c)):             # treat this same as the thousands above
                    roman_numeral += 'C'            
            
            elif int(c) == 4: roman_numeral += 'CD'   # add a custom letter if the number is 4
            
            elif int(c) > 4 and int(c) < 9:           # if the number is greater than 4 and less than 9
                roman_numeral += 'D'                # add a 'D' to the roman numeral (meaning 500)
                for i in range(int(c) - 5):         # add however many 'C's (100) we need to get to the correct number
                    roman_numeral += 'C'
            
            elif int(c) == 9: roman_numeral += 'CM'   # add a custom letter if the number is 9
            
            size -= 1
            continue

        elif size == 2:   # the same logic as the hundreds place was followed, but for the letters in the tens place
            if int(c) < 4:                          
                for i in range(int(c)):             
                    roman_numeral += 'X'            
            
            elif int(c) == 4: roman_numeral += 'XL'   
            
            elif int(c) > 4 and int(c) < 9:           
                roman_numeral += 'L'                
                for i in range(int(c) - 5):         
                    roman_numeral += 'X'
            
            elif int(c) == 9: roman_numeral += 'XC'
            
            size -= 1
            continue

        elif size == 1:   # the same logic as the tens place was followed, but for the letters in the ones place
            if int(c) < 4:                          
                for i in range(int(c)):             
                    roman_numeral += 'I'            
            
            elif int(c) == 4: roman_numeral += 'IV'   
            
            elif int(c) > 4 and int(c) < 9:           
                roman_numeral += 'V'                
                for i in range(int(c) - 5):         
                    roman_numeral += 'I'
            
            elif int(c) == 9: roman_numeral += 'IX'

    # return and print the roman numeral
    return roman_numeral


####### The User Interface Portion #######
print("Welcome to the Decimal and Roman Numeral Converter!")

keepGoing = True
while keepGoing:    # loop until the user quits the program

    # get ask the user what kind of conversion they want
    userInput = input("""
    Press 'R' to convert from Roman Numeral to Decimal
    Press 'D' to convert from Decimal to Roman Numeral
    Press 'Q' to quit the program
    
    Click 'Enter' to submit your choice
    """)

    print('')

    if userInput.upper() == 'Q':
        keepGoing = False
        print("Goodbye!")
        break

    elif userInput.upper() == 'R':
        romanNumeral = input("Please enter a roman numeral: ")

        print("=================================")
        print("Decimal Number: ", roman_to_decimal(romanNumeral))
        print("=================================")

    elif userInput.upper() == 'D':
        decimalNumber = input("Please enter a decimal number: ")

        # try to convert the decimal number to an integer, but if it doesn't work, tell the user to try again and restart the loop
        try:
            decimalNumber = int(decimalNumber)
        except ValueError:
            print("Not a valid input (must be a numeric integer). Please try again.")
            continue

        print("=================================")
        print("Roman Numeral:", decimal_to_roman(decimalNumber))
        print("=================================")

    else:
        print("Not a valid input. Please try again.")