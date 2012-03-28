import sys

try:
    f = open(sys.argv[1], 'rb')
except IOError:
    sys.exit('Unable to open file')
except ValueError:
    sys.exit('Not a string')
except Exception as e:
    sys.exit(e)

toPrint = ''
while True :
    piece = f.read(1).decode("latin1")
    if piece == '' : 
        if len(toPrint) > 3 : 
            print(toPrint)
            toPrint = ''
        break
    if str.isprintable(piece):
        toPrint += piece
    else:
        if len(toPrint) > 3 : 
            print(toPrint)
            toPrint = ''
try:
    f.close()
except Exception as e:
    sys.exit(e)