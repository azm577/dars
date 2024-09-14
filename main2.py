from os import system
from json import dumps
system("cls")
with open('natija.txt', 'r') as file:  
    words = file.read().split()   

if words: 
    longest_word = max(words, key=len)   
    print(f"Eng uzun so'z: {longest_word}")
else:
    print("Fayl bo'sh")  
