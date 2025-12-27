
#Caesar Cipher
def caesar_encrypt():
    encrypted_text = input("Input the message,you want to encrypt. ")
    x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    y = "defghijklmnopqrstuvwxyzabcDEFghijklmnopqrstuvwxyzABC"
    mytable = str.maketrans(x, y)
    print(encrypted_text.translate(mytable))   
def  caesar_decrypt():
    decrypted_text = input("Input the decrypted message. ")
    x = "defghijklmnopqrstuvwxyzabcDEFghijklmnopqrstuvwxyzABC"
    y = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mytable = str.maketrans(x, y)
    print(decrypted_text.translate(mytable))
#Atbash Cipher
def atbash_encrypt():
    encrypted_text = input("Input the message,you want to encrypt. ")
    x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    y = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
    mytable = str.maketrans(x, y)
    print(encrypted_text.translate(mytable))
def atbash_decrypt():
    encrypted_text = input("Input the message,you want to decrypt. ")
    y = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
    mytable = str.maketrans(x, y)
    print(encrypted_text.translate(mytable))
#ROT13 Cipher
def rot13_encrypt():
    encrypted_text = input("Input the message,you want to encrypt. ")
    x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    y = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    mytable = str.maketrans(x, y)
    print(encrypted_text.translate(mytable))
def rot13_decrypt():
    encrypted_text = input("Input the message,you want to decrypt. ")
    y = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    mytable = str.maketrans(x, y)
    print(encrypted_text.translate(mytable))
#GoldenBoy Cipher (EasterEgg)
def golden_encrypt():
    encrypted_text = input("Input the message,you want to encrypt. ")
    x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    y = "jnucksthraqflexovbmpdgiwyzJNUCKSTHRAQFLEXOVBMPDGIWYZ"
    mytable = str.maketrans(x, y)
    print(encrypted_text.translate(mytable))
def golden_decrypt():
    encrypted_text = input("Input the message,you want to decrypt. ")
    x = "jnucksthraqflexovbmpdgiwyzJNUCKSTHRAQFLEXOVBMPDGIWYZ"
    y = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mytable = str.maketrans(x, y)
    print(encrypted_text.translate(mytable))

#Gather user information 
userID = input("Enter a username ")
while True:
    process = input("Welcome " + userID + ", Would you like to encrypt or decrypt (e/d) or quit (q) ")
#Encryption Process 
    if process == "e":
        cipher = input("State the encryption method: Caesar (C), Atbash (A), ROT13, (R) ").upper()
        if cipher == "C": 
            caesar_encrypt()
        elif cipher == "A":
            atbash_encrypt()
        elif cipher == "R":
            rot13_encrypt()
        elif cipher == "G":
            golden_encrypt()
        else: 
            print("Error")  
    elif process == "d":
        cipher = input("State the decryption method: Caesar (C), Atbash (A), ROT13, (R) ").upper()
        if cipher == "C": 
            caesar_decrypt()
        elif cipher == "A":
            atbash_decrypt()
        elif cipher == "R":
            rot13_decrypt()
        elif cipher == "G":
            golden_decrypt()
        else: 
            print("Error")  
    elif process == "q":
        exit()
    else:
        print("Thank you, " + userID)






