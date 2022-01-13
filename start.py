import requests
import pyfiglet
import termcolor

TL_NAME_text = pyfiglet.figlet_format("SQLI CHECK")
TL_NAME = termcolor.colored(TL_NAME_text, 'red')

print(TL_NAME) 
print(termcolor.colored('Created by izox\ntwitter : @izox99\n', 'blue'))
print(termcolor.colored('write the link like this : https://example.com/index.php?id=1\n', 'red'))

dictionary = open('dict.txt', 'r')
url = input("please enter a URL : ")
try:
    for x in dictionary:
        r = requests.get(url + x.rstrip())
        text = r.text
        result = "<b>Warning</b>:" in text
        if result == True:
            print(termcolor.colored("[+] This page " + url + " is infected", 'green'))
            break
except Exception:
    print(termcolor.colored("", 'green'))