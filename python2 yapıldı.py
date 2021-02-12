username_rule = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_'
website_rule = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
extension_max = 3

def EmailValidation(email,extension_rule):
    exp1 = email.split('@')
    if(len(exp1) == 2):
        exp2 = exp1[1].split(".")
        if(len(exp2) == extension_rule):
            error_username = UsernameValidation(exp1[0])
            if(error_username != 0):
                data = False
            else:
                error_website = WebsiteValidation(exp2[0])
                if(error_website != 0):
                    data = False
                else:
                    data = True
        else:
            data = False
    else:
        data = False
    return data

def UsernameValidation(username):
    errors = 0
    letters = list(username)
    for i in range(0, len(username)):
        check = username_rule.find(letters[i])
        if(check == -1):
            errors += 1
    return errors

def WebsiteValidation(website):
    errors = 0
    letters = list(website)
    for i in range(0, len(website)):
        check = website_rule.find(letters[i])
        if(check == -1):
            errors += 1
    return errors
    
try:
    extension_rule = int(input("Uzantı uzunluğunu giriniz: "))
    if(extension_rule < 0 or extension_rule > 3):
        print("Uzantının maksimum uzunluğu 3 olmalıdır")
    else:
        email = input("Email adresini giriniz: ")
        validate = EmailValidation(email,extension_rule)

        if not validate:
            print(extension_rule,"\n",email,"\nMail adresiniz yanlıştır")
        else:
            print(extension_rule,"\n",email,"\nMail adresiniz doğrudur")
except:
    print("Hatalı giriş")