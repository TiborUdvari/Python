import sys
import smtplib

#from email.MIMEText import MIMEText

try:
    fileName = sys.argv[1];
except IndexError:
    sys.exit("File name not given")
    
try:
    file = open(fileName, 'r');
except IOError:
    sys.exit("Erreur entree sortie")
except Exception as e:
    sys.exit(e);
#ajout test email

mots = (file.read()).split()

while True : 
    emailNote = file.readline();
    if emailNote == '' : break;
    print(emailNote);
    
file.close()