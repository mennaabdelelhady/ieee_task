def find_first_nonrepeating_char(s):
    char_count = {}
    
    # count the frequency of each character in the string
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    
    # find the first character that occurs only once
    for c in s:
        if char_count[c] == 1:
            return c
    
    # if no such character is found, return None
    return None

# example 
my_str = "ieeemansourasociety"
result = find_first_nonrepeating_char(my_str)
print(result)  # output: "m"
