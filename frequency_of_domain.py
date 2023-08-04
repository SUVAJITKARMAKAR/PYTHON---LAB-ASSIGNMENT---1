#  A PROGRAM TO COUNT THE FREQUENCY OF ANY SPECIFIC ELEMENTS IN THE DOMAIN 

str_domain = "SOCIAL NETWORKING WEBSITE"
letter_frequency = {}

for x in str_domain:
    if x in letter_frequency:
        letter_frequency[x] += 1
    else:
        letter_frequency[x] = 1


print("ALL CALCULATED FREQUENCIES ARE : \n" + str(letter_frequency))