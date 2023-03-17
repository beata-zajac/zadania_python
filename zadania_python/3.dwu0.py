liczbaN = int(input("Podaj liczbę całkowitą: "))

dwu = liczbaN * 2

if liczbaN >= (-10 ** 9) or liczbaN <= 10 ** 9:

    print("Dwukrotność liczby " + str(liczbaN) + " to: " + str(dwu) )
else: 
    print("Liczba całkowita musi znajdować się w przedziale od -10^9 do 10^9")