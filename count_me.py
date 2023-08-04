# A PROGRAM TO COUNT ALL THE ALPHABETS, LETTERS , SPECIAL CHARACTERS IN THE PARAGRAPH PROVIDED 

digits_in_count = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

small_letters_in_count = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

capital_letters_in_count = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

total_digits = 0
total_small_letters = 0
total_large_letters = 0
total_special_characters = 0

domain_string = "Suvajitkarmakar,socialnetworkingsite,2347261"

for s in domain_string:
    if s in digits_in_count:
        total_digits += 1
    elif s in small_letters_in_count:
        total_small_letters += 1
    elif s in capital_letters_in_count:
        total_large_letters +=1 
    else:
        total_special_characters += 1


print("TOTAL SMALL LETTERS FOUND : ", total_small_letters)
print("TOTAL LARGE LETTERS FOUND : ", total_large_letters)
print("TOTAL DIGITS FOUND : ", total_digits);
print("TOTAL SPECIAL CHARACTERS FOUND : ", total_special_characters)