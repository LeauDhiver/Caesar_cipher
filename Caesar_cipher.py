## encryption
def encrypt_caesar(txt, key):
    result = ""

    for char in txt:
        if char.isalpha():
            if char.isupper():
                result = result + chr((ord(char) - 65 + key) % 26 + 65)
            else:
                result = result + chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result = result + char

    return result


## decryption
def decrypt_caesar(txt, key):
    result = ""

    for char in txt:
        if char.isalpha():
            if char.isupper():
                result = result + chr((ord(char) - key - 65) % 26 + 65)
            else:
                result = result + chr((ord(char) - key - 97) % 26 + 97)
        else:
            result = result + char

    return result
