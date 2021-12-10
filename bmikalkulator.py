from enum import Enum
from easygui import *


class bmi_ertekek(Enum):
    '''BMI értékhatárok.'''
    Alultáplált = 18.5
    Normál = 25
    Túlsúlyos = 30
    Extrém_túlsúlyos = 40

class bmi:
    '''A személy adatai (kor, tömeg, magasság).'''
    def __init__(self, kor):
        self.kor = kor
        self.tomeg = self.tomeg()
        self.magassag = self.magassag()

    def show(self):
        print(self.kor)
        self.tomeg.show()
        self.magassag.show()

class tomeg(bmi):
    def __init__(self, tomeg):
        self.tomeg = tomeg

class magassag(bmi):
    def __init__(self, magassag):
        self.magassag = magassag


def kalkulacio():
    '''BMI kalkulálása.'''
    kalkul = bmi.tomeg / ((bmi.magassag / 100) ** 2)
    return round(kalkul)

def menu_opciok():
    '''A felhasználónak lehetőséget ad, hogy akar-e új személyt hozzáadni.'''
    print("Válasszon a lehetőségek közül.\n\t0 - Kilépés"
          "\n\t1 - Új személy hozzáadása")

szemelyek = [] #nagy tömb

print("----------------------------------------------------")
print("BMI Kalkulátor")
print("----------------------------------------------------")
print("Kérem a felhasználó törekedjen valós adatok megadására.")

'''Fájl megnyitása.'''
file = open("névsor.txt", "r+", encoding="utf8")

'''A fájlból beolvasott adatokat eltároljuk kis-tömbökben, amiket eltárolunk egy nagy tömbben.'''
for szemely in file:
    szemely = szemely.strip().split()
    szemelyek.append(szemely)


#-----------FŐMODUL--------------
for szemely in szemelyek:
    try:
        print("\n%s" % szemely[0])

        '''Bekérjük a személy korát, majd leellenőrizzük, hogy jó értéket adott e meg.'''

        bmi.kor = int(input("- Kor: "))

        '''Ha rossz értéket adott meg újból bekérjük.'''
        if bmi.kor < 1 or not float and not int:
            print("Valós értéket adjon meg.")
            bmi.kor = int(input("- Kor:"))

        '''Jó érték megadása esetén berkajuk egy kis-tömbbe.'''
        szemely.append("- Kor:")
        szemely.append(str(bmi.kor))
        szemely.append("éves |")
        #kor bekérve
        '''Megismételjük a tömegnél is ugyanazt, mint a kornál.'''
        bmi.tomeg = float(input("Tömeg (kg): "))

        if bmi.tomeg < 1 or not float and not int:
            print("Valós értéket adjon meg.")
            bmi.tomeg = float(input("Tömeg (kg): "))

        szemely.append("Tömeg:")
        szemely.append(str(bmi.tomeg))
        szemely.append("kg |")
        #tömeg bekérve
        bmi.magassag = float(input("Magasság (cm): "))

        if bmi.magassag < 1 or not float and not int:
            print("Valós értéket adjon meg.")
            bmi.magassag = float(input("Magasság (cm): "))

        szemely.append("Magasság:")
        szemely.append(str(bmi.magassag))
        szemely.append("cm |")
        #magasság bekérve

        szemely.append(" -->  BMI: ")
        szemely.append(str(kalkulacio()))
        #BMI értéke is a tömbbe került

        '''Megnézzük, hogy a számolt bmi érték, melyik csoportba tartozik.'''
        if kalkulacio() < bmi_ertekek.Alultáplált.value:
            szemely.append("- %s //" % bmi_ertekek.Alultáplált.name)

        if kalkulacio() >= bmi_ertekek.Alultáplált.value and kalkulacio() < bmi_ertekek.Normál.value:
            szemely.append("- %s testsúly //" % bmi_ertekek.Normál.name)

        if kalkulacio() < bmi_ertekek.Túlsúlyos.value and kalkulacio() >= bmi_ertekek.Normál.value:
            szemely.append("- %s //" % bmi_ertekek.Túlsúlyos.name)

        if kalkulacio() >= bmi_ertekek.Túlsúlyos.value and kalkulacio() < bmi_ertekek.Extrém_túlsúlyos.value:
            szemely.append("- Elhízás //")

        if kalkulacio() > bmi_ertekek.Extrém_túlsúlyos.value:
            szemely.append("- Extrém elhízás //")

    #ha hiba van
    except ZeroDivisionError:
        print("A nulla nem jó érték.")

    except ValueError:
        print("Szám értéket kell megadni.")
        #ha hibát talál az értékek között akkor kitörli a személy minden adatát
        del szemely[1:]

#Létrehozunk egy menüt, ahol a felhasználó eldöntheti, akar e új személyt hozzáadni
menu = ""
while menu != "0":
    menu_opciok()
    menu = input()

    '''Ha szeretne új személyt hozzáadni, akkor gyakorlatilag a főmodul indul újra kisebb változásokkal.'''
    if menu == "1":
        uj_sor=[]
        nev = input("Kérem a személy nevét: ")

        for szemely in szemelyek:
            try:
                '''Létre hozunk egy teljesen új és üres kis-tömböt
                ,hogy a nevet is el tudjuk benne tárolni, mert a fileba ez már nincs benne.'''
                szemelyek.append(uj_sor)

                uj_sor.append(nev)
                #név hozzáadva

                '''Ugynaazt az eljárást és ellenőrzést használjuk, mint az előző személyeknél.'''
                bmi.kor = int(input("- Kor: "))
                if bmi.kor<1 or not float and not int:
                    print("Valós értéket adjon meg.")
                    bmi.kor = int(input("- Kor:"))

                uj_sor.append("- Kor:")
                uj_sor.append(str(bmi.kor))
                uj_sor.append("éves |")
                #kor hozzáadva

                bmi.tomeg = float(input("Tömeg (kg): "))
                if bmi.tomeg<1 or not float and not int:
                    print("Valós értéket adjon meg.")
                    bmi.tomeg = float(input("Tömeg (kg): "))

                uj_sor.append("Tömeg:")
                uj_sor.append(str(bmi.tomeg))
                uj_sor.append("kg |")
                #tömeg hozzáadva

                bmi.magassag = float(input("Magasság (cm): "))
                if bmi.magassag<1 or not float and not int:
                    print("Valós értéket adjon meg.")
                    bmi.magassag = float(input("Magasság (cm): "))
                
                uj_sor.append("Magasság:")
                uj_sor.append(str(bmi.magassag))
                uj_sor.append("cm |")
                #magasság hozzáadva

                uj_sor.append(" -->  BMI: ")
                uj_sor.append(str(kalkulacio()))
                #bmi érték hozzáadva

                '''Leellenőrizzük, hogy a számolt bmi érték, melyik csoportba tartozik.'''
                if kalkulacio() < bmi_ertekek.Alultáplált.value:
                    uj_sor.append("- %s //" % bmi_ertekek.Alultáplált.name)

                if kalkulacio() >= bmi_ertekek.Alultáplált.value and kalkulacio() < bmi_ertekek.Normál.value:
                    uj_sor.append("- %s testsúly //" % bmi_ertekek.Normál.name)

                if kalkulacio() < bmi_ertekek.Túlsúlyos.value and kalkulacio() >= bmi_ertekek.Normál.value:
                    uj_sor.append("- %s //" % bmi_ertekek.Túlsúlyos.name)

                if kalkulacio() >= bmi_ertekek.Túlsúlyos.value and kalkulacio() < bmi_ertekek.Extrém_túlsúlyos.value:
                    uj_sor.append("- Elhízás //")

                if kalkulacio() > bmi_ertekek.Extrém_túlsúlyos.value:
                    uj_sor.append("- Extrém elhízás //")

                break

            except ZeroDivisionError:
                print("A nullával nem osztunk.")

            except ValueError:
                print("Szám értéket kell megadni. Adatait törölnünk kell.")
                szemelyek.remove(uj_sor)

'''Kitöröljük a neveket a fájlból, hogy újból be tudjuk írni így nem kétszer lesznek benne.'''
file.truncate()
file.seek(0)

'''Kiírjuk a fileba az adatokat szemelyenkent.'''
for szemely in szemelyek:
    x=(' '.join(szemely))
    file.write(x + '\n')

file.close()

print("Program vége.")