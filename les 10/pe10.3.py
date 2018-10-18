invoerstring=input("geef de gebruiker + beginstation + eindstation:")

def code(invoerstring):
    uitvoer =""
    for letters in invoerstring :
        uitvoer += chr(ord(letters) + 3)
    print(uitvoer)
code(invoerstring)