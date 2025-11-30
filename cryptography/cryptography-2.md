# Exercise 2

## a) Calculate n, φ(n), and the private exponent d

**1. Calculate the Modulus (n):**
n = p × q
n = 197 × 211 = 41567

**2. Calculate Euler's Totient Function φ(n):**
φ(n) = (p - 1) × (q - 1)
φ(n) = (197 - 1) × (211 - 1) = 196 × 210 = 41160

**3. Find the Private Exponent (d):**
We need to find d such that e · d = 1 (mod φ(n)).
Equation: 24377 · d = 1 (mod 41160).

We use the **Extended Euclidean Algorithm** to find the modular inverse.

We can use the following python code snippet to calculate d:
```python
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
```

The output is the following:
```
n: 41567
phi: 41160
d: 17393
```

So **d is equal to 17393**.

To verify the result:
e * d = 24377 * 17393 = 423989161 = 1 (mod 41160)

---

## b) Encrypt and Decrypt

**Encryption:**
C = m^e mod n

C = 1234^24377 mod 41567

I'll write a python snippet again to calculate the ciphertext:
```python
M = 1234
e = 24377
n = 41567
d = 17393

C = pow(M, e, n)
print(f"Cipher text: {C}")
```

The result is **C=26476**

**Decryption:**
M = C^d mod n

M = 26476^17393 mod 41567

Continuing with the python snippet:
```python
M_decrypted = pow(C, d, n)
print(f"Plain text: {M_decrypted}")
```

The result is **M=1234**

---

## c) Square-and-Multiply Steps (for exponent e)

We need to calculate 1234^24377 mod 41567.

**1. Convert Exponent to Binary:** 101111100111001

**2. Algorithm:**
We start with the base (1234). For every '0' bit, we **Square**. For every '1' bit, we **Square and Multiply** by the base. In each step, we also perform modulo at the end.

I'll use the following code snippet to perform these calculations:
```python
def square_and_multiply(base, exponent, modulus):
    binary_exp = bin(exponent)[2:]

    print(f"Exponent: {exponent}")
    print(f"Binary:   {binary_exp}\n")

    print(
        f"{'Step':<5} | {'Bit':<3} | {'Operation':<17} | {'Calculation':<25} | {'Result':<5}"
    )
    print("-" * 70)

    # First step: Initialization (MSB is always 1)
    result = base
    print(f"{'1':<5} | {'1':<3} | {'Initial':<17} | {'-':<25} | {result:<5}")

    # Iterate through the rest of the bits
    step_count = 2
    for bit in binary_exp[1:]:
        prev_result = result

        # Always Square first
        result = (result * result) % modulus
        op_name = "Square"
        calc_desc = f"{prev_result}^2"

        # If bit is 1, also Multiply
        if bit == "1":
            result = (result * base) % modulus
            op_name = "Square & Multiply"
            calc_desc = f"({prev_result}^2) * {base}"

        print(
            f"{step_count:<5} | {bit:<3} | {op_name:<17} | {calc_desc + ' mod n':<25} | {result:<5}"
        )
        step_count += 1

    print("-" * 70)
    print(f"Final Result: {result}")


m = 1234
e = 24377
n = 41567

square_and_multiply(m, e, n)
```

And we get the following:
```
Exponent: 24377
Binary:   101111100111001

Step  | Bit | Operation         | Calculation               | Result
----------------------------------------------------------------------
1     | 1   | Initial           | -                         | 1234
2     | 0   | Square            | 1234^2 mod n              | 26344
3     | 1   | Square & Multiply | (26344^2) * 1234 mod n    | 39933
4     | 1   | Square & Multiply | (39933^2) * 1234 mod n    | 583
5     | 1   | Square & Multiply | (583^2) * 1234 mod n      | 11996
6     | 1   | Square & Multiply | (11996^2) * 1234 mod n    | 6384
7     | 1   | Square & Multiply | (6384^2) * 1234 mod n     | 28435
8     | 0   | Square            | 28435^2 mod n             | 29508
9     | 0   | Square            | 29508^2 mod n             | 18115
10    | 1   | Square & Multiply | (18115^2) * 1234 mod n    | 21154
11    | 1   | Square & Multiply | (21154^2) * 1234 mod n    | 26747
12    | 1   | Square & Multiply | (26747^2) * 1234 mod n    | 22757
13    | 0   | Square            | 22757^2 mod n             | 39363
14    | 0   | Square            | 39363^2 mod n             | 35844
15    | 1   | Square & Multiply | (35844^2) * 1234 mod n    | 26476
----------------------------------------------------------------------
Final Result: 26476
```
