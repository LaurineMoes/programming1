
while True:
    try:
        aantal=int(input("aantal personen:"))
        cijfer = 4356 / (aantal)
        if aantal < 0:
            print('Delen door negatieve getallen is niet mogelijk!')
        else:
            print(cijfer)
    except ZeroDivisionError:
        print("Delen door nul kan niet!")
    except ValueError:
        print("Gebruik cijfers voor het invoeren van het aantal!")
    except:
        print("onjuist invoer!")
    break
