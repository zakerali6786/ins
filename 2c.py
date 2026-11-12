def encrypt(text, columns):
    while len(text) % columns != 0:
        text += "X"

    rows = len(text) // columns

    matrix = [[""] * columns for _ in range(rows)]

    k = 0

    # Fill row-wise
    for row in range(rows):
        for col in range(columns):
            matrix[row][col] = text[k]
            k += 1

    result = ""

    # Read column-wise
    for col in range(columns):
        for row in range(rows):
            result += matrix[row][col]

    return result


def decrypt(cipher, columns):
    rows = len(cipher) // columns

    matrix = [[""] * columns for _ in range(rows)]

    k = 0

    # Fill column-wise
    for col in range(columns):
        for row in range(rows):
            matrix[row][col] = cipher[k]
            k += 1

    result = ""

    # Read row-wise
    for row in range(rows):
        for col in range(columns):
            result += matrix[row][col]

    return result.rstrip("X")


text = input("Enter plaintext: ")
columns = int(input("Enter number of columns: "))

encrypted = encrypt(text, columns)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, columns)
print("Decrypted:", decrypted)