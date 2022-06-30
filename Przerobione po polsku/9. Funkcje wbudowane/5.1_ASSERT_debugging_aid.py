# Fuknkcja wskazuje dokładne miejsce błędu

# Przykład nr 1

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


shoes_RS = {'name': 'Fancy Shoes RS', 'price': 14900}

print(apply_discount(shoes_RS, 0.25))
print(apply_discount(shoes_RS, 0))


# Przykład nr 2 - brzydki przykład

if price >= 100:
    print('Wartość powyżej 99, wykonuje funkcję promocja ()')
elif price < 100:
    print('Wartość poniżej 100, wykonuje funkcję promocja ()')