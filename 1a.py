def encrypt(text,key):
    result=""
    for char in text :
        if char.isalpha():
            shift=ord('A') if char.isupper() else ord('a')
            result+=chr((ord(char)-shift+key)%26+shift)
        else:
            result+=char
    return result
def decrypt(text,key):
    return encrypt(text,-key)
text=input("enter ")
key=int(input("enter"))
print(encrypt(text,key))
print(decrypt(text,key))

import random

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


# Read 50 chats from file

file = open("chats.txt", "r")
chats = file.readlines()
file.close()

# Generate 10 random keys

keys = random.sample(range(1, 26), 10)

print("S.No | Random Key | Plaintext | Ciphertext")

# Encrypt 50 chats

for i in range(50):
    key = keys[i % 10]
    text = chats[i].strip()

    cipher = caesar_encrypt(text, key)

    print(i + 1, "|", key, "|", text, "|", cipher)
