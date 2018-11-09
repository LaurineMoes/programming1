import datetime


naam = input("geef je naam:")



vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
# %a = weekdag /%d = dag van de maand bijv 02 /%b = de maand / %Y = het jaar

while True:
    file=open('Hardlopers.txt', "a")
    tekst = "{} {}\n".format(s,vandaag)
    write.file(tekst)
    if naam == "stop":
        break

