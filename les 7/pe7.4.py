file = open('Hardlopers.txt',"a")

def strftime():
    import datetime
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y")
    # %a = weekdag /%d = dag van de maand bijv 02 /%b = de maand / %Y = het jaar
    return(s)

y = strftime()
print(y)