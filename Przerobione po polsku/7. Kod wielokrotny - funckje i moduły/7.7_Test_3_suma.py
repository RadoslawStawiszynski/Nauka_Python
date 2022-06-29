def sum(x):
    res = 0
    for i in range(x):
        res += i
    return res


print("Wyniki sumowania: " + str(sum(10)))

# SEARCH ENGINE #

print("Wstaw tekst np artykuł.")
text = input()
print("Wstaw słowo do wyszukania w artykule.")
word = input()


def search(text, word):
    if word in text:
        return "Word found"
    else:
        return "Word not found"


print(search(text, word))
