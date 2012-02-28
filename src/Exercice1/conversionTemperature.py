while True:
    try:
        temperature = float(input("Entrez une température : "))
        break
    except ValueError:
        print("Désolé mais la valeur entrée n'est pas juste. Try again")
#TODO gérér si l'utilisateur entre n'importe qua ici

#Solution 1 
# For the lack of a do while loop

#conversionVers = ""
#while(not(conversionVers == 'C' or conversionVers == 'F')):
#    conversionVers = input("Convertir vers degrees (C)elsius ou (F)ahrenheit:")

#Solution 2 
#For the lack of a do while loop

while True:
    conversionVers = input("Convertir vers degrees (C)elsius ou (F)ahrenheit:")
    if (conversionVers == 'C' or conversionVers == 'F'):
        break

if conversionVers == 'C' :
    resultat = 5/9 * (temperature - 32)
elif conversionVers == 'F':
    resultat = 9/5 * temperature + 32
print('Résultat {0:.2f}'. format(resultat))
