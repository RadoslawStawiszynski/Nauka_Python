plik_txt = open('9._OPEN.txt')
tekst = plik_txt.read()

print(tekst)

plik_txt = open('9._OPEN.txt', 'w')
plik_txt.write('''Przesłanie Pana Cogito(wiersz klasyka)
Zbigniew Herbert

Idź dokąd poszli tamci do ciemnego kresu
po złote runo nicości twoją ostatnią nagrodę

idź wyprostowany wsród tych co na kolanach
wsród odwroconych plecami i obalonych w proch

ocalałeś nie po to aby życ
masz mało czasu trzeba dac świadectwo

bądź odwazny gdy rozum zawodzi bądź odważny
w ostatecznym rachunku jedynie to sie liczy

a Gniew twój bezsilny niech będzie jak morze
ilekroć usłyszysz głos poniżonych i bitych

niech nie opuszcza cię twoja siostra Pogarda
dla szpiclów katów tchórzy - oni wygrają
pojdą na twój pogrzeb i z ulgą rzuca grude
a kornik napisze twój uładzony życiorys

i nie przebaczaj zaiste nie w twojej mocy
przebaczać w imieniu tych których zdradzono o świcie

strzeż sie jednak dumy niepotrzebnej
oglądaj w lustrze swa blazeńską twarz
powtarzaj: zostalem powolany - czyż nie było lepszych

strzeż sie oschłosci serca kochaj źrodło zaranne
ptaka o nieznanym imieniu dąb zimowy
światlo na murze splendor nieba
one nie potrzebują twojego ciepłego oddechu
są po to aby mówić: nikt cię nie pocieszy

czuwaj - kiedy światlo w górach daje znak - wstań i idź
dopóki krew obraca w piersi twoją ciemną gwiazdę

powtarzaj stare zaklęcia ludzkości bajki i legendy
bo tak zdobędziesz dobro którego nie zdobędziesz
powtarzaj wielkie słowa powtarzaj je z uporem
jak ci co szli przez pustynie i gineli w piasku

a nagrodzą cie za to tym co maja pod reką
chłosta śmiechu zabójstwem na śmietniku

idż bo tylko tak będziesz przyjęty do grona zimnych czaszek
do grona twoich przodków: Gilgamesza Hektora Rolanda
obronców królestwa bez kresu i miasta popiołów

Bądź wierny idź''')

plik_txt.close()

print()



plik_txt = open('9._OPEN.txt', 'a')
plik_txt.write('\n\nMój ulubiony wiersz')
plik_txt.close()

plik_txt = open('9._OPEN.txt')
tekst2 = plik_txt.read()
plik_txt.close()

print(tekst2)

