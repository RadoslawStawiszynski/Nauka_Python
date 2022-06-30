print(bool(0))
print(bool(1))
print(bool(123.456))
print(bool(-1230))
print(bool(None))
print(bool("A co to?"))
print(bool("   "))
# Przy listach, krotkach i mapach jeśli są puste => FALSE
print("LISTY ....")
lista_pusta = []
print(bool(lista_pusta))
lista_pelna = ["a", "b", "c"]
print(bool(lista_pelna))
# Podaj rok urodzenia
rok = input("Podaj rok urodzenia: ")
if not bool(rok.rstrip()):
    print("Musisz podać swoj rok urodzenia.")
    # Funkscja rstrip() - usuwa wszystkie znaki typu spacje i entery z końca łańacucha.
    # Związku z tym otrzymujemy zmienną pustą, która generuje false, ze względu na pustą funkcję bool.


