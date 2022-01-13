import requests,pyfiglet,termcolor
from optparse import OptionParser
#___________________________ OPT ___________________________
use=OptionParser('\033[01;31mCommand\033[00;37m')
use.add_option("-t","--target",dest="target",help="write the Target like this : \033[01;31m https://example.com/index.php?id=")
(options,args) = use.parse_args()
#___________________________ OPT ___________________________
TL_NAME_text = pyfiglet.figlet_format("SQLI CHECK")
TL_NAME = termcolor.colored(TL_NAME_text, 'red')

print(TL_NAME) 
print(termcolor.colored('Created by izox\ntwitter : @izox99\n', 'blue'))

dictionary = open('dict.txt', 'r')
url = options.target
try:
    for x in dictionary:
        r = requests.get(url + x.rstrip()).text
        result = "mysql" in r
        if result == True:
            print(termcolor.colored("[+] The Payload is: " + x, 'green'))
            break
        else:
            print(termcolor.colored("[+] Payload is not Found" + x, 'red'))
except Exception:
    print(termcolor.colored("", 'green'))
