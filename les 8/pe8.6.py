def menu():
    print("\n1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen ")
    print("4: Ik geef mijn kluis terug")
    print("5: Stoppen\n")
    menukeuze = input("Kies een optie (1-5): ")
    if menukeuze == "1":
        aantal_vrije_keuze()
    elif menukeuze == "2":
        nieuwe_kluis()
    elif menukeuze == "3":
        kluis_openen()
    elif menukeuze == "4":
        kluis_teruggeven()
    elif menukeuze == "5":
        exit(" ")
    else:
        print("Probeer iets anders...")
        menu()

def aantal_vrije_keuze():
    file = open("kluizen.txt", "r")
    kluizen = 12 - len(file.readlines())
    if kluizen == 0:
        print("Helaas,er zijn geen kluizen meer vrij!")
    else:
        print("Er zijn nog {} kluiz(en) beschikbaar".format(kluizen))
    file.close()
    menu()

def nieuwe_kluis():
    file=open("kluizen.txt", "r+")
    kluizen=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for de_kluis in (file.readlines()):
        for kluis in kluizen:
            if int(de_kluis.split(";")[0]) == kluis:
                kluizen.remove(kluis)
    if not kluizen:
        print("De lockers zitten helaas vol.")
    else:
        code=input("Voer een code in voor u kluis: ")
        file.write("\n{};{}".format(kluizen[0], code))
        print("U heeft een nieuwe kluis met kluisnummer: {}".format(kluizen[0]))
    file.close()
    menu()

def kluis_openen():
    try:
        kluisnummer = int(input("Wat is uw kluisnummer?: "))
        if kluisnummer >= 1 and kluisnummer <= 12:
            file=open("kluizen.txt", "r")
            kluisje={}
            for i in file.readlines():
                kluisje[i.split(";")[0]]=i.split(";")[1].replace("\n", "")
            if str(kluisnummer) in kluisje:
                kluiscode=input("Wat is uw kluiscode?: ")
                if kluiscode == kluisje.get(str(kluisnummer)):
                    print("kluis {} is geopend!".format(kluisnummer))
                else:
                    print("Verkeerde code voor kluis {}".format(kluisnummer))
            else:
                print("Deze kluis is nog vrij voor gebruik.")
            file.close()
            menu()
        else:
            print("Kies een van de twaalf kluizen")
            kluis_openen()
    except ValueError:
        print ("Probeer het nog een keer.")
        kluis_openen()


def kluis_teruggeven():
    try:
        kluisnummer = int(input("Wat is uw kluisnummer?: "))
        file = open("kluizen.txt", "r+")
        if kluisnummer >= 1 and kluisnummer <= 12:
            kluisje = {}
            for i in file.readlines():
                kluisje[i.split(";")[0]] = i.split(";")[1].replace("\n", "")
            if str(kluisnummer) in kluisje:
                kluiscode = input("Wat is uw kluiscode?: ")
                if kluiscode == kluisje.get(str(kluisnummer)):
                    file.seek(0)
                    lines = file.readlines()
                    file.seek(0)
                    file.truncate()
                    for line in lines:
                        if line != str(kluisnummer) + ";" + kluiscode and line != str(
                                kluisnummer) + ";" + kluiscode + "\n":
                            file.write(line)
                    file.close()
                    print("Kluis {} is nu weer vrij voor de volgende gebruiker.".format(kluisnummer))
                else:
                    print("Verkeerde code voor kluis {}".format(kluisnummer))
            else:
                print("Kluis {} is al vrij.".format(kluisnummer))
            menu()
        else:
            print("Kies een van de twaalf kluizen.:")
            kluis_teruggeven()
    except ValueError:
        print("Probeer opnieuw.")
        kluis_teruggeven()
menu()