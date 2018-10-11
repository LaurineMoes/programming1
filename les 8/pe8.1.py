maand = input("Hoeveelste maand is het?")

def seizoen(maand):
    Y = int(maand)
    if Y >= 5 and Y <= 3:
        seizoen = "lente"
    elif Y >= 6 and Y <= 8:
        seizoen = "zomer"
    elif Y >= 9 and Y <= 11:
        seizoen = "herfst"
    elif Y == 12 and Y <= 2:
        seizoen = "winter"
    return seizoen


print("Deze maand hoort bij het seizoen:" + "{}".format(seizoen(maand)))