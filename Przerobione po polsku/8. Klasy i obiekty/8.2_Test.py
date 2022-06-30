import sys

class podstawowe_ruchy:
    def lewa_naprzod(self):
        print("Wykonuję ruch do przodu lewą nogą.")
    def prawa_naprzod(self):
        print("Wykonuję ruch do przodu prawą nogą.")
    def lewa_tyl(self):
        print("Wykonuję ruch do tyłu lewą nogą.")
    def prawa_tyl(self):
        print("Wykonuję ruch do tyłu prawą nogą.")

class umiejetnosci(podstawowe_ruchy):
    def taniec_1(self):
        self.lewa_naprzod()
        self.lewa_tyl()
        self.prawa_naprzod()
        self.prawa_tyl()
        self.lewa_tyl()
        self.prawa_tyl()
        self.prawa_naprzod()
        self.lewa_naprzod()

    def taniec_2(self):
        self.lewa_naprzod()
        self.prawa_naprzod()
        self.prawa_tyl()
        self.lewa_tyl()
        self.prawa_naprzod()
        self.prawa_tyl()

class zyrafy(umiejetnosci):
    print('Jak imię wybierasz dla swojej żyrafy:')
    imie = sys.stdin.readline()

    if imie != None:
        print('Wybierz umiejętność dla swojej żyrafy:'
              'taniec 1 czy taniec 2')
        wybor = sys.stdin.readline()
        if wybor == "taniec 1" or int(1):
            print("ok")
        elif wybor == "taniec 2" or int(2):
            print("ok2")
        else:
            print('Wybierz umiejętność dla swojej żyrafy:'
                  'taniec 1 czy taniec 2'
                  "Poprawne odpowiedzi to taniec 1 lub 1 lub taniec 2 lub 2")

max = zyrafy()

max.taniec_1()

# zapytaj o imie i zapisz w pamieci
# wywyołaj funckje z dostępnych
# wyswietl bład jesli nie ma takiej funkcji