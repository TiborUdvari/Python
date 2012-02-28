import sys

if(len(sys.argv)!=3):
    sys.exit("Not the good argument count ... Read the man page, oh wait there isn't one :)")

try:
    temperature = float(sys.argv[1])
    conversionVers = str(sys.argv[2]) 
except ValueError:
    sys.exit("Should be program.py {NUMBER} {F or C}")

if conversionVers != 'C' and conversionVers != 'F' :
    sys.exit("Second arg must be C or F")
if conversionVers == 'C' :
    resultat = 5/9 * (temperature - 32)
elif conversionVers == 'F':
    resultat = 9/5 * temperature + 32
print('Résultat {0:.2f}'. format(resultat))

    