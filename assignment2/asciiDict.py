def asciiDict():
    dictionary = {}
    for char in 'abcdefghijklmnopqrstuvwxyz':
        dictionary[char] = ord(char)
        
    return dictionary

print(asciiDict())