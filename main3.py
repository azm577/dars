from os import system
from json import dumps
system("cls")
with open('natija.txt', 'r') as source_file: 
    data = source_file.read()  

with open('yangi_fayl.txt', 'w') as destination_file:   
    destination_file.write(data)   

print("Ma'lumot muvaffaqiyatli ko'chirildi!")
