import numpy as np
from math import gcd


class HillCipher:

    def __init__(self, key):
        self.key = key
        self.MOD = 26

    def text_to_numbers(self, plain_text):
        return [ord(c.upper()) - ord('A') for c in plain_text if c.isalpha()]

    def numbers_to_text(self, numbers):
        return ''.join(chr(number + ord('A')) for number in numbers)

    def inverse(self, number):
        number %= self.MOD

        for i in range(1, self.MOD):
            if (number * i) % self.MOD == 1:
                return i

        raise ValueError("Not Possible")

    def matrix_inverse(self, matrix):
        det = round(np.linalg.det(matrix))
        det_mod = det % self.MOD

        if gcd(det_mod, self.MOD) != 1:
            raise ValueError("Not Possible")

        det_inverse = self.inverse(det_mod)

        adj = np.round(
            det * np.linalg.inv(matrix)
        ).astype(int)

        inverse_matrix = (det_inverse * adj) % self.MOD

        return inverse_matrix

    def encrypt(self, plain_text):
        number_plain_text = self.text_to_numbers(plain_text)
        result = []

        while len(number_plain_text) % len(self.key) != 0:
            number_plain_text.append(ord('X') - ord('A'))

        for i in range(0, len(number_plain_text), len(self.key)):
            block = number_plain_text[i:i+len(self.key)]
            encrypted_block = np.dot(self.key, block) % self.MOD
            result.extend(encrypted_block)

        return self.numbers_to_text(result)

    def decrypt(self, cipher_text):
        number_cipher_text = self.text_to_numbers(cipher_text)
        result = []

        inverse_key = self.matrix_inverse(self.key)

        for i in range(0, len(number_cipher_text), len(self.key)):
            block = number_cipher_text[i:i+len(self.key)]
            decrypted_block = np.dot(inverse_key, block) % self.MOD
            result.extend(decrypted_block)

        return self.numbers_to_text(result)


key = np.array([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])

hill = HillCipher(key)

cipher = hill.encrypt("Saketh")
plain = hill.decrypt(cipher)

print("Encrypted:", cipher)
print("Decrypted:", plain)