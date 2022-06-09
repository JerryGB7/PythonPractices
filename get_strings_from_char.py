def create_strings_from_characters(frequencies, string1, string2):
    temp = frequencies.copy()
    temp2 = frequencies.copy()
    num_of_words = 0
    can_be_created1 = True
    can_be_created2 = True

    #check to see if the first word can be created
    while can_be_created1:
        for i in string1:
            # if the char in not in the dict then return false
            if i not in temp:
                can_be_created1 = False
            else:
            # using a temp dict to keep track of char uses
                temp[i] -= 1
                if temp[i] == 0:
                    temp.pop(i)    
        break
    
    # use a while loop to see if you can make the second word if the first one fails
    while can_be_created2 and can_be_created1 == False:
        for i in string2:
            # if a char is not in the full dict then return false
            if i not in temp2:
                can_be_created2 = False
            else:
                # use the second copy to keep track of the char's
                temp2[i] -= 1
                if temp2[i] == 0:
                    temp2.pop(i) 
        break
    # if the first word did not fail then use the first temp dict 
    else:
        for i in string2:
            if i not in temp:
                can_be_created2 = False
            else:
                temp[i] -= 1
                if temp[i] == 0:
                    temp.pop(i) 

    # add 1 to number of words and get rid of any char's in the dict that have 0
    if can_be_created1:
        num_of_words += 1
        for i in string1:
            frequencies[i] -= 1
            if frequencies[i] == 0:
                frequencies.pop(i)

    
    # add 1 to number of words and get rid of any char's in the dict that have 0
    if can_be_created2:
        num_of_words += 1
        for i in string2:
            frequencies[i] -= 1
            if frequencies[i] == 0:
                frequencies.pop(i)
                       

    return num_of_words      


x = create_strings_from_characters({"h": 2, "e": 1, "l": 1, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}, "hello", "world")
print(x)