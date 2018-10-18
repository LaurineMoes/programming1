a = 0
b = 0
while True:
    getal = int(input("geef een getal:"))
    b += getal
    a += 1
    if getal == 0:
        print("Er zijn {} getallen ingevoerd, de som is: {}".format(a, b))
        break



