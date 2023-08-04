# A PROGRAM TO COUNT THE NUMBER OF INTERSECTIONS IN STRING 
def count (string, character):
    result = 0

    for i in range(len(string)):
        if (string[i] == character):
            result += 1
        
    return result




domain_string = "socialnetworkingwebsite"
search_character = 'n'
print(count(domain_string, search_character))