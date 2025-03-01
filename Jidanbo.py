def length():
    minLength = 14
    while True:
        length = int(input("\nHow long do you want your password to be: "))
        if (length < minLength):
            print("Your password must be atleast 14 characters long according to the Gotei 13!")
        else:
            print("Very Well! Your password shall be {} characters long.".format(length))
            return length
    
def compVsPhr():  
    while True:
        pwPref = (input("\nWould you like a passphrase(pp) or complex password(cp): "))
        if pwPref == "pp" or  pwPref == "passphrase":
            print("You have chosen passphrase.")
            return "pp"
        if pwPref == "complex" or pwPref == "cp":
            print("You have chosen complex.")
            return "cp"
        else:
            print("Imbicile!! You must choose from the given best practices!")
    
def passPhrase():
    return

def comPW():
    return


def main():
    pwLength = 0
    pwType = ''

    print("I am Jidanbo! I will keep the soul society safe by creating strong and easy to remember passwords to stop the hollows!")
    pwLength = length()
    pwType = compVsPhr()



if __name__ == '__main__':
    main()
