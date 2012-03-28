import string;
import sys;

LOWER = string.ascii_lowercase;
UPPER = string.ascii_uppercase;

def rot13(c):
    try:
        i = LOWER.index(c)
        return LOWER[i-13]
    except ValueError:
        pass
    
    try:
        i = UPPER.index(c)
        return UPPER[i-13]
    except ValueError:
        pass 
    
    return c

while True:
    toTranslate = input("Give me something to decode : ")
    if (toTranslate == "") : 
        sys.exit("Good bye")
    output = ""
    for i in toTranslate:
        output+=rot13(i)
    print(output)

    