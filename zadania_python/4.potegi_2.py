n = int(input("Podaj potęgę: "))

i = 0

while(pow(2,i)):
       print(pow(2,i))
       i+= 1
       if i == n+1:
        break
       elif  n <= 0 or n >= 60:
        print("Podana przec Ciebie liczba nie znajduje się w przedziale od 0 do 60 ")
        break 
