
def reverse(string):
    output = ''
    for i in range(0,len(string)):
        output += string[len(string)-1-i]
    return output

print(reverse('test'))