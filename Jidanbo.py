import random
import string
from wonderwords import RandomWord

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

def passLength():
    minLength = 14
    while True:
        length = int(input("\nHow long do you want your password to be: "))
        if (length < minLength):
            print("Your password must be atleast 14 characters long according to the Gotei 13!")
        else:
            print("Very Well! Your password shall be {} characters long.".format(length))
            return length

def wordCount():
    minLength = 3
    while True:
        length = int(input("\nHow many words do you want your passphrase to be: "))
        if (length < minLength):
            print("Your passphrase must be atleast 3 words long according to the Gotei 13!")
        else:
            print("Very Well! Your passphrase shall be {} words long.".format(length))
            return length

def passPhrase():
    r = RandomWord()
    words = wordCount()
    pw = '_'.join(r.random_words(words, word_min_length=4, word_max_length=6))
    print("\nYou're generated pasword is: '{}'".format(pw))
    return pw
    
def comPW():
    pwLength = passLength()
    allowed_chars = string.ascii_letters + string.digits + string.punctuation
    pw = ''.join(random.choices(allowed_chars, k=pwLength))
    print("\nYou're generated pasword is: '{}'".format(pw))
    return pw

def main():
    pwType = ''
    print("I am Jidanbo! I will keep the soul society safe by creating strong and easy to remember passwords to stop the hollows!")
    pwType = compVsPhr()
    if pwType == "pp":
        passPhrase()
    elif pwType == "cp":
        comPW()
    
if __name__ == '__main__':
    main()



