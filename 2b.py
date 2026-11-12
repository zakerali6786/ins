
import time
import matplotlib.pyplot as plt


# ENCRYPTION

def encrypt(text, columns):
    while len(text) % columns != 0:
        text += "X"

    rows = len(text) // columns
    matrix = [[""] * columns for _ in range(rows)]

    k = 0

    for col in range(columns):
        for row in range(rows):
            matrix[row][col] = text[k]
            k += 1

    result = ""

    for row in range(rows):
        for col in range(columns):
            result += matrix[row][col]

    return result


# DECRYPTION

def decrypt(cipher, columns):
    rows = len(cipher) // columns
    matrix = [[""] * columns for _ in range(rows)]

    k = 0

    for row in range(rows):
        for col in range(columns):
            matrix[row][col] = cipher[k]
            k += 1

    result = ""

    for col in range(columns):
        for row in range(rows):
            result += matrix[row][col]

    return result


# FILE HANDLING

file = open(input("Enter file path: "), "r")
text = file.read().strip()
file.close()

print("Original Text:", text)


# THREE KEYS

keys = [2, 3, 4]
enc_times = []
dec_times = []
lengths = []

for key in keys:

    start = time.time()
    cipher = encrypt(text, key)
    enc_time = time.time() - start

    start = time.time()
    decrypted = decrypt(cipher, key)
    dec_time = time.time() - start

    decrypted = decrypted[:len(text)]

    enc_times.append(enc_time * 1000)
    dec_times.append(dec_time * 1000)
    lengths.append(len(cipher))

    print("\nKey:", key)
    print("Encrypted:", cipher)
    print("Decrypted:", decrypted)
    print("Encryption Time:", enc_time * 1000, "ms")
    print("Decryption Time:", dec_time * 1000, "ms")
    print("Result:", "Success" if decrypted == text else "Failed")


# RESULTS TABLE

print("\nKEY | LENGTH | ENC TIME | DEC TIME")

for i in range(len(keys)):
    print(keys[i], "|", lengths[i], "|",
          enc_times[i], "|", dec_times[i])


# GRAPH

plt.plot(keys, enc_times, marker='o', label='Encryption')
plt.plot(keys, dec_times, marker='s', label='Decryption')

plt.xlabel("Number of Columns")
plt.ylabel("Execution Time (ms)")
plt.title("Column Transformation Performance")
plt.legend()
plt.grid()
plt.show()
