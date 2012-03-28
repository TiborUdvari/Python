import sys

usage = """
usage: count.py <filename>
"""
try:
    filename = sys.argv[1]
except:
    print (usage)
    sys.exit(1)

try:    
    f = open(filename,'r')
except IOError as e:
    print ("Erreur en ouvrant le fichier:")
    print (e.strerror)
    sys.exit(1)

text = f.read()
f.close()

# Se débarrasse des carcatères non-alphabétiques
# (ponctuation, chiffres, ...)
# (Solution peu élégante; on verra de meilleures possibilités que cette boucle
# dans le chapitre sur la programmation fonctionnelle)
clean_text = ""
for c in range(len(text)): 
    if text[c].isalpha():
        clean_text += text[c]
    else:
        clean_text += ' '
        
words = clean_text.split()

counted = {}

for word in words:
    try:
        counted[word] += 1
    except KeyError:
        counted[word] = 1

sorted_words = list(counted.keys())
# Trie sans tenir compte de la casse
sorted_words.sort(key=str.lower)

#for w in sorted_words:
#    print ("%s: %d" % (w,counted[w]))ry[i].