from os import system
from json import dumps
system("cls")
with open('natija.txt', 'r') as file:
    a = file.readlines()
    if a:
        print(a[-1].strip()) 
    else:
        print("Fayl bo'sh")
