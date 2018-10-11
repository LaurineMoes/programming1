def convert(T):
    Y = T * 1.8 + 32.
    return Y

def table():
    for i in range(-30, 41, 10):
        print ("{:7.1f}   {:7.1f}".format(i, convert(i)))

print ("    C         F")
print (table())
