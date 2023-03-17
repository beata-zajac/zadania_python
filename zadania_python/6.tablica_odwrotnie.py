import random

ileliczb = int(input("Ile liczb ma się wyświetlić? "))
 
liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, 1000000)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

print("Wylosowane liczby:", liczby)

print("Wylosowane liczby w odwrotnej kolejności: ", liczby[::-1])
