import turtle


class Rzeczowniki:
    pass


class Niezywotne(Rzeczowniki):
    pass


class Zywotne(Rzeczowniki):
    pass


class Chodniki(Niezywotne):
    pass


class Zwierzeta(Zywotne):
    def oddycha(self):
        print("oddycham")

    def rusza_sie(self):
        print("ruszam się")

    def je(self):
        print("jem")


class Ssaki(Zwierzeta):
    def karmi_mlode_mlekiem(self):
        print("karmię młode mlekiem")

    def znajduje_pozywienie(self):
        self.rusza_sie()
        print("Znalazłem pozywienie")
        self.je()

    def je_lisice_z_drzew(self):
        self.je()

    def tanczy_polke(self):
        self.rusza_sie()
        self.rusza_sie()
        self.rusza_sie()
        self.rusza_sie()


class Zyrafy(Ssaki):
    def je_liscie_z_drzew(self):
        print("jem liscie z drzewa")

    def __init__(self, cetki):
        self.cetki_zyrafy = cetki


Reginald = Zyrafy(1)
Harold = Zyrafy(1)
print('Reginald:' ), Reginald.je_liscie_z_drzew()


class Funkcje:
    def funkcja(self):
        print("To jest funkcja przykładna.")

    def funkcja_2(self):
        print("ja też jestem funkcją klasy. Rozumiemy się?")


Reginald.rusza_sie()
Reginald.je_liscie_z_drzew()
Harold.rusza_sie()

Ewa = turtle.Pen()
Kasia = turtle.Pen()

Ewa.fd(50)
Ewa.right(90)
Ewa.forward(20)

Kasia.left(90)
Kasia.forward(100)

Jakub = turtle.Pen()
Jakub.left(180)
Jakub.forward(80)

Kasia = turtle.Pen()

Kasia.right(90)
Kasia.forward(120)
Kasia.right(90)
Kasia.forward(300)

# Funkcje wywołujące inne funckje
Harold.znajduje_pozywienie()
Harold.tanczy_polke()

# Iniciajlizowanie obiektu

Oswald = Zyrafy(100)
Gertruda = Zyrafy(150)
Ssaki_Ladowe = Ssaki()

print('Oswald ma %s cętek.' % Oswald.cetki_zyrafy)
print(Gertruda.cetki_zyrafy)
Ssaki_Ladowe.tanczy_polke()
