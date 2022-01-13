from os import system
from sys import platform
list=['requests','pyfiglet','termcolor']
for pip in list:
        if "linux" in platform:
                system(f'pip3 install {pip}')
        else:
                system(f'pip install {pip}')
