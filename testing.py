# imports
from decimal_roman_converter import roman_to_decimal, roman_to_decimal_letter, roman_checker, decimal_to_roman

# test cases

print("#### START TESTS ####")
print('\n==== roman_to_decimal_letter Tests ====')
if roman_to_decimal_letter('I') == 1: print("I passed")
if roman_to_decimal_letter('L') == 50: print("L passed")
if roman_to_decimal_letter('M') == 1000: print("M passed")
if roman_to_decimal_letter('A') == False: print("A passed (meaning it failed, as it was supposed to)")

print('\n==== roman_checker Tests ====')
if roman_checker('CMXXXVI') == True: print("I passed")
if roman_checker('A') == False: print("A passed (meaning it failed, as it was supposed to)")
if roman_checker(1) == False: print("1 passed (meaning it failed, as it was supposed to)")

print('\n==== roman_to_decimal Tests ====')
roman_to_decimal(1)
roman_to_decimal('I')
roman_to_decimal('A')

print('')
if roman_to_decimal('MMMCMXCIX') == 3999: print("MMMCMXCIX passed") # 3,999
if roman_to_decimal('CMXXXVI') == 936: print("CMXXXVI passed")  # 936
if roman_to_decimal('MMCCLIII') == 2253: print("MMCCLIII passed") # 2253

print('\n==== decimal_to_roman Tests ====')
decimal_to_roman(1)
decimal_to_roman('AABB')
decimal_to_roman(3999)
decimal_to_roman(3998)