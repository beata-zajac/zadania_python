a= int(input("podaj liczbę a: "))
b= int(input("podaj liczbę b: "))

if a and b >= -2 * 10 ** 9 or a and b <= 2 * 10 **9:
    odleglosc = a-b
    print ("odległość pomiędzy a i b to: ", odleglosc)