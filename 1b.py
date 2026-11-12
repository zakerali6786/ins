import time
import matplotlib.pyplot as plt

def create_matrix(key):
    key = key.upper().replace("J", "I")

    letters = ""

    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in letters:
            letters += ch

    matrix = []
    for i in range(0, 25, 5):
        matrix.append(list(letters[i:i+5]))

    return matrix


def find_position(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

    return -1, -1


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())

    result = ""
    i = 0

    while i < len(text):
        first = text[i]

        if i + 1 < len(text):
            second = text[i + 1]

            if first == second:
                result += first + "X"
                i += 1
            else:
                result += first + second
                i += 2
        else:
            result += first + "X"
            i += 1

    return result


def playfair_encrypt(text, matrix):
    encrypted = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            encrypted += matrix[row1][(col1 + 1) % 5]
            encrypted += matrix[row2][(col2 + 1) % 5]

        elif col1 == col2:
            encrypted += matrix[(row1 + 1) % 5][col1]
            encrypted += matrix[(row2 + 1) % 5][col2]

        else:
            encrypted += matrix[row1][col2]
            encrypted += matrix[row2][col1]

    return encrypted


def playfair_decrypt(text, matrix):
    decrypted = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            decrypted += matrix[row1][(col1 - 1) % 5]
            decrypted += matrix[row2][(col2 - 1) % 5]

        elif col1 == col2:
            decrypted += matrix[(row1 - 1) % 5][col1]
            decrypted += matrix[(row2 - 1) % 5][col2]

        else:
            decrypted += matrix[row1][col2]
            decrypted += matrix[row2][col1]

    return decrypted


testcases = [
    ("MONARCHY", "INSTRUMENTS"),
    ("KEYWORD", "BALLOON"),
    ("SECURITY", "HELLO WORLD")
]

results = []

for number, (key, plaintext) in enumerate(testcases, 1):

    matrix = create_matrix(key)
    prepared = prepare_text(plaintext)

    start = time.perf_counter()
    encrypted = playfair_encrypt(prepared, matrix)
    encryption_time = (time.perf_counter() - start) * 1000

    start = time.perf_counter()
    decrypted = playfair_decrypt(encrypted, matrix)
    decryption_time = (time.perf_counter() - start) * 1000

    results.append((
        number, key, plaintext, prepared,
        encrypted, decrypted,
        len(prepared), encryption_time, decryption_time
    ))

print("\nPLAYFAIR CIPHER RESULTS")

print("\nTest\tKey\t\tPlaintext\tEncrypted\tDecrypted")

for r in results:
    print(r[0], "\t", r[1], "\t", r[2], "\t",
          r[4], "\t", r[5])

print("\nPERFORMANCE ANALYSIS")

print("Test\tLength\tEncryption(ms)\tDecryption(ms)")

for r in results:
    print(r[0], "\t", r[6], "\t",
          round(r[7], 6), "\t\t",
          round(r[8], 6))

tests = [r[0] for r in results]
encryption = [r[7] for r in results]
decryption = [r[8] for r in results]

plt.plot(tests, encryption, marker='o', label="Encryption")
plt.plot(tests, decryption, marker='s', label="Decryption")

plt.xlabel("Test Case")
plt.ylabel("Execution Time (ms)")
plt.title("Playfair Cipher Performance Analysis")

plt.xticks(tests)
plt.legend()
plt.grid()
plt.show()