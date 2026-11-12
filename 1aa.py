
import random
import string

key = list(string.ascii_uppercase)
random.shuffle(key)

def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            index = ord(char.upper()) - ord('A')
            result += key[index] if char.isupper() else key[index].lower()
        else:
            result += char

    return result


def decrypt(text, key):
    result = ""
    original = string.ascii_uppercase

    for char in text:
        if char.isalpha():
            index = key.index(char.upper())
            result += original[index] if char.isupper() else original[index].lower()
        else:
            result += char

    return result


text = input("Enter plaintext: ")

encrypted = encrypt(text, key)

print("Key:", "".join(key))
print("Encrypted:", encrypted)
print("Decrypted:", decrypt(encrypted, key))
