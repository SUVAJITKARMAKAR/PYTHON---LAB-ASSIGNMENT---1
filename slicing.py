# A PROGRAM TO DEMONSTRATE THE FUNCTIONALITIES OF SLICING AND NEGATIVE  INDEXING 

domain_string = ["HELLO", "I", "AM", "SUVAJIT", "KARMAKAR", "DOMAIN", "IS", "SOCIAL", "NETWORKING", "SITE"]
print("DOMAIN STRING : ", domain_string)

# NEGATIVE SLICING
print("THE STRING AFTER SLICING (NEGATIVE INDEXING) : ", domain_string[-4:-1])

# NEGATIVE SLICING WITH STEP
print("THE STRING AFTER SLICING (STEP) : ", domain_string[-9:-3:2])

# SLICE
slice_string_1 = slice(4)
slice_string_2 = slice (1,5,2)

print(domain_string[slice_string_1])
print(domain_string[slice_string_2])

# SLICING
print(domain_string[1:7:2])

# NEGATIVE SLICING
print(domain_string[-1:-12:-2])

# SLICING 
print(domain_string[::-2])

#SLICING 
print(domain_string[2:])

# SLICING 
print(domain_string[:])