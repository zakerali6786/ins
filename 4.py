import secrets
import time
import matplotlib.pyplot as plt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = secrets.token_bytes(16)
cipher = AES.new(key, AES.MODE_ECB)

sizes = [1, 100, 1000]
times = []

# Encryption of SECURITY
message = b'SECURITY'
encrypted = cipher.encrypt(pad(message, 16))

print("AES Encrypted:", encrypted.hex())

# Performance Testing
for size in sizes:
    message = secrets.token_bytes(size * 1024)

    start = time.perf_counter()
    encrypted = cipher.encrypt(pad(message, 16))
    end = time.perf_counter()

    elapsed = (end - start) * 1000
    times.append(elapsed)

# Display Table
print("\nData Size (KB)\tEncryption Time (ms)")

for i in range(3):
    print(sizes[i], "\t\t", round(times[i], 4))

# Plot Graph
plt.plot(sizes, times, marker='o')
plt.xlabel("Data Size (KB)")
plt.ylabel("Encryption Time (ms)")
plt.title("AES Encryption Performance")
plt.grid()
plt.show()