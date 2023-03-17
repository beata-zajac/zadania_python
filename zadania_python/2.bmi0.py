mass= int(input("podaj swoją wagę: "))

if mass <= 30 or mass >= 400:

    print("waga musi być w przedziale od 30 do 400")
    mass= int(input("podaj swoją wagę: "))

else:
    print("teraz podaj swój wzrost")

height= float(input("podaj swój wzrost: "))

if height <= 1.0 or height >= 2.5:
        print("wzrost musi być w przedziale od 1.0 do 2.5")
        height= float(input("podaj swój wzrost: "))
else: 
        print("teraz obliczymy Twoje BMI")



BMI = mass/((height)*(height))




print("Twoje BMI wynosi: ", BMI)

if BMI < 20:
    print("NIEDOWAGA")

elif 20 <= BMI <= 25:
    print("WAGA W NORMIE")

elif 25 < BMI < 30:
    print("NADWAGA")

else:
    print("OTYLOSC")