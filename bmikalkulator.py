from enum import Enum

class bmi_ertekek(Enum):
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

    class tomeg:
        def __init__(self, tomeg):
            self.tomeg = tomeg

    class magassag:
        def __init__(self, magassag):
            self.magassag = magassag


def kalkulacio():
    kalkul = bmi.tomeg / ((bmi.magassag / 100) ** 2)
    return kalkul

def menu_opciok():
    print("Válasszon az alábbi menüpontok közül\n\t0 - Kilépés"
          "\n\t1 - Új személy hozzáadása")

tomb = []

fki = open("névsor.txt", "r+", encoding="utf8")

for sor in fki:
    sor = sor.strip().split()
    tomb.append(sor)

for sor in tomb:
    try:
        print("%s" %sor[0])

        bmi.kor = int(input("- Kor: "))
        sor.append("- Kor:")
        sor.append(str(bmi.kor))
        sor.append("éves |")

        bmi.tomeg = float(input("Tömeg: "))
        sor.append("Tömeg:")
        sor.append(str(bmi.tomeg))
        sor.append("kg |")

        bmi.magassag = float(input("Magasság: "))
        sor.append("Magasság:")
        sor.append(str(bmi.magassag))
        sor.append("cm |")

        sor.append(" -->  BMI: ")
        sor.append(str(kalkulacio()))

        if kalkulacio() < bmi_ertekek.Alultáplált.value:
            sor.append("- %s //" %bmi_ertekek.Alultáplált.name)

        if kalkulacio() >= bmi_ertekek.Alultáplált.value and kalkulacio() < bmi_ertekek.Normál.value:
            sor.append("- %s testsúly //" %bmi_ertekek.Normál.name)

        if kalkulacio() < bmi_ertekek.Túlsúlyos.value and kalkulacio() >= bmi_ertekek.Normál.value:
            sor.append("- %s //" %bmi_ertekek.Túlsúlyos.name)

        if kalkulacio() >= bmi_ertekek.Túlsúlyos.value and kalkulacio() < bmi_ertekek.Extrém_túlsúlyos.value:
            sor.append("- Elhízás //")

        if kalkulacio() > bmi_ertekek.Extrém_túlsúlyos.value:
            sor.append("- Extrém elhízás //")

    except ZeroDivisionError:
        print("A nulla nem jó érték.")

    except ValueError:
        print("Szám értéket kell megadni.")
        del sor[1:]

menu = ""
while menu != "0":
    menu_opciok()
    menu = input()
    if menu == "1":
        uj_sor=[]
        nev = input("Kérem a személy nevét: ")
        for sor in tomb:
            try:
                tomb.append(uj_sor)

                uj_sor.append(nev)

                bmi.kor = int(input("- Kor: "))
                uj_sor.append("- Kor:")
                uj_sor.append(str(bmi.kor))
                uj_sor.append("éves |")

                bmi.tomeg = float(input("Tömeg: "))
                uj_sor.append("Tömeg:")
                uj_sor.append(str(bmi.tomeg))
                uj_sor.append("kg |")

                bmi.magassag = float(input("Magasság: "))
                uj_sor.append("Magasság:")
                uj_sor.append(str(bmi.magassag))
                uj_sor.append("cm |")

                uj_sor.append(" -->  BMI: ")
                uj_sor.append(str(kalkulacio()))

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
                print("A nulla nem jó érték.")

            except ValueError:
                print("Szám értéket kell megadni.")
                tomb.remove(uj_sor)

fki.truncate()
fki.seek(0)

for sor in tomb:
    x=(' '.join(sor))
    fki.write(x+'\n')

fki.close()