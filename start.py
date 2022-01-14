import requests,pyfiglet,termcolor
from optparse import OptionParser
#___________________________ OPT ___________________________
use=OptionParser('\033[01;31mCommand\033[00;37m')
use.add_option("-t","--target",dest="target",help="write the Target like this : \033[01;31m https://example.com/index.php?id=1")
use.add_option("-s","--urls",dest="urls",help="to check more than one link, write the file name")
(options,args) = use.parse_args()
#___________________________ OPT ___________________________
TL_NAME_text = pyfiglet.figlet_format("SQLI CHECK")
TL_NAME = termcolor.colored(TL_NAME_text, 'red')

print(TL_NAME) 
print(termcolor.colored('Created by izox\ntwitter : @izox99\n', 'blue'))

# try:
if options.target != None:
    dictionary = open('dict.txt', 'r')
    # url = 1
    url = options.target
    for x in dictionary:
        r = requests.get(url + x.rstrip()).text
        result = "mysql" in r
        if result == True:
            print(termcolor.colored("[+] The Payload is : " + x, 'green'))
            break
        else:
            print(termcolor.colored("[-] Payload is not Found : " + x, 'red'))
            
elif options.urls != None:
    # url > 1
    urls = open(options.urls, 'r')
    for url in urls:
        dictionary = open('dict.txt', 'r')
        print(termcolor.colored(f"\n[%] url is : {url}", 'yellow'))
        for x in dictionary:
            r = requests.get(url + x.rstrip()).text
            result = "mysql" in r.lower()
            if result == True:
                print(termcolor.colored("[+] The Payload is : " + x, 'green'))
                break
            elif result == False:
                print(termcolor.colored("[-] Payload is not Found : " + x, 'red'))
        
else:
    print(termcolor.colored("[-] sorry, try again", 'red'))
    exit()
# except Exception:
#     print(termcolor.colored("[-] Error", 'red'))
