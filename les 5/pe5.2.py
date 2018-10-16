leeftijd = int(input("geef je leeftijd:"))
paspoort = input("Nederlands paspoort:")

if leeftijd >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen!")
elif paspoort == "nee":
    print("Helaas je mag niet stemmen omdat je geen Nederlands paspoort hebt.")
else:
    print("Je bent te jong om te stemmen")