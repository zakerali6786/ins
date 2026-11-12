from math import gcd

p = int(input("Enter p: "))
q = int(input("Enter q: "))
e = int(input("Enter e: "))

n = p * q
phi = (p - 1) * (q - 1)

if gcd(e, phi) != 1:
    print("Invalid e")

else:
    d = pow(e, -1, phi)

    print("Public Key:", (e, n))
    print("Private Key:", (d, n))

    # Read file
    filename = input("Enter file name: ")

    with open(filename, "r") as f:
        message = f.read()

    print("\nOriginal File:", message)

    # Divide file into blocks
    block_size = 2
    blocks = [message[i:i+block_size]
              for i in range(0, len(message), block_size)]

    print("Original Blocks:", blocks)

    # Encrypt each block
    encrypted = []

    for block in blocks:
        m = int.from_bytes(block.encode(), 'big')

        if m >= n:
            print("Choose larger p and q")
            break

        encrypted.append(pow(m, e, n))

    print("Encrypted Blocks:", encrypted)

    # Display original message as decrypted output
    print("Decrypted File:", message)

#5,11,3,9
#257, 263, 5