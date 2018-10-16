def checknumber(newpassword):
    check_number = False
    for char in newpassword:
        for i in range(10):
            if str(i) == char:
                check_number = True
    return check_number

def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6 and checknumber(newpassword) == True:
        return True
    else:
        return False

oldpassword = input("Enter your old password: ")
newpassword = input("Enter a new password: ")
print (new_password(oldpassword, newpassword))
