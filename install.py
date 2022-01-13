#Programming By GitHub:xF14x

from os import system

print(""" Welcome To \"install.py\" File

	The File Will Install for you:
	1- requests
	2- pyfiglet
	3- termcolor

	Windows (1)
	Linux (2)
""")

install = input("==>")

if install == "1":
	system("pip install requests")
	system("pip install pyfiglet")
	system("pip install termcolor")
elif install == "2":
	system("pip3 install requests")
	system("pip3 install pyfiglet")
	system("pip3 install termcolor")
else:
	exit("Error, Please ReOpen The install.py File And Choose Your OS")