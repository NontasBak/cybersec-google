def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


p, q, e = 197, 211, 24377

n = p * q
phi = (p - 1) * (q - 1)

g, d, _ = egcd(e, phi)
d = d % phi  # Ensure d is positive

print(f"n: {n}")
print(f"phi: {phi}")
print(f"d: {d}")
