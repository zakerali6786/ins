import time
import matplotlib.pyplot as plt
def encrypt(text, rails):
    fence = [""] * rails
    row = 0
    direction = 1

    for ch in text:
        fence[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return "".join(fence)

def decrypt(cipher, rails):
    pattern = []
    row = 0
    direction = 1

    for i in range(len(cipher)):
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    counts = [pattern.count(i) for i in range(rails)]

    fence = []
    start = 0

    for count in counts:
        fence.append(list(cipher[start:start + count]))
        start += count

    result = ""

    for row in pattern:
        result += fence[row].pop(0)

    return result

file = open(input("Enter file path: "), "r")
text = file.read().strip()
file.close()

print("\nOriginal Text:", text)


keys = [2, 3, 4]

enc_times = []
dec_times = []
lengths = []

print("\nKEY | CIPHER LENGTH | ENC TIME | DEC TIME")

for key in keys:

    start = time.perf_counter()
    cipher = encrypt(text, key)
    enc_time = time.perf_counter() - start

    start = time.perf_counter()
    decrypted = decrypt(cipher, key)
    dec_time = time.perf_counter() - start

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

print("\nRESULTS TABLE")
print("Key | Cipher Length | Enc Time (ms) | Dec Time (ms)")

for i in range(len(keys)):
    print(keys[i], "|", lengths[i], "|",
          enc_times[i], "|", dec_times[i])


# GRAPH

plt.plot(keys, enc_times, marker='o', label='Encryption Time')
plt.plot(keys, dec_times, marker='s', label='Decryption Time')

plt.xlabel("Number of Rails")
plt.ylabel("Execution Time (ms)")
plt.title("Rail Fence Cipher Performance")
plt.legend()
plt.grid()
plt.show()
