temperature = input("Entrez une température : ")
temperature = float(temperature)
#TODO gérér si l'utilisateur entre n'importe qua ici
conversionVers = ""
while(not(conversionVers == 'C' or conversionVers == 'F')):
    conversionVers = input("Convertir vers degrees (C)elsius ou (F)ahrenheit:")
if conversionVers == 'C' :
    resultat = 5/9 * (temperature - 32)
elif conversionVers == 'F':
    resultat = 9/5 * temperature + 32
print("Résultat", resultat)
