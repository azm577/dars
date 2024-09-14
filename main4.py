from os import system
from json import dumps
system("cls")
class Oda:
    def __init__(self, kurs_nomi, davom,narxi):
        self.__kurs_nomi = kurs_nomi  
        self.__davom = davom
        self.__narxi = narxi

    def __str__(self):
        return f"""
            kurs_nomi: {self.__kurs_nomi} 
            davom: {self.__davom} oy
            narxi: {self.__narxi} $
            

        """

oda = Oda("python dastur", 6,200)

print(oda)
