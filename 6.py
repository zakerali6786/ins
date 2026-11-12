def primitive_root(p):
    for g in range(2, p):
        values = set(pow(g, i, p) for i in range(1, p))
        if len(values) == p - 1:
            return g
    return None

p = int(input("Enter prime number p: "))

g = primitive_root(p)

print("Primitive root:", g)

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

A = pow(g, a, p)
B = pow(g, b, p)

key_A = pow(B, a, p)
key_B = pow(A, b, p)

print("Alice's public key:", A)
print("Bob's public key:", B)
print("Alice's secret key:", key_A)
print("Bob's secret key:", key_B)
#23 5 6 15