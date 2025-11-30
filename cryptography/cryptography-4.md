# Exercise 4

## a) Calculate C₁^x mod p

- 20^6 mod 23
- 64000000 mod 23
- 16 mod 23

**Result:**
C₁^x = 16 (mod 23)

---

## b, c) Find M using modular inverse multiplication

We need to find the modular multiplicative inverse of the result from step (a) modulo p. We are looking for (16)^(-1) mod 23.

Let k be the inverse. We need to satisfy the equation:
16 · k = 1 (mod 23)

**Using the Extended Euclidean Algorithm:**

1. **Forward steps:**
   - 23 = 1 · 16 + 7
   - 16 = 2 · 7 + 2
   - 7 = 3 · 2 + 1

2. **Backward substitution:**
   - 1 = 7 - 3(2)
   - Substitute 2 from the second equation: 2 = 16 - 2(7)
   - 1 = 7 - 3(16 - 2(7))
   - 1 = 7 - 3(16) + 6(7)
   - 1 = 7(7) - 3(16)
   - Substitute 7 from the first equation: 7 = 23 - 1(16)
   - 1 = 7(23 - 16) - 3(16)
   - 1 = 7(23) - 7(16) - 3(16)
   - 1 = 7(23) - 10(16)

3. **Result:**
   - 1 = -10(16) (mod 23)
   - The inverse is -10. Converting this to a positive integer (add 23 to -10):
   - -10 = 13 (mod 23)
   - Finally, we have (C₁^x)^(-1) = 13

4. **Verification:**
   - 16 × 13 = 208
   - 208 ÷ 23 = 9 with a remainder of 1

---

The formula for ElGamal decryption is:
M = C₂ · (C₁^x)^(-1) mod p

Using the values we calculated:
- C₂ = 22
- (C₁^x)^(-1) = 13

We have:
- M = 22 · 13 mod 23
- M = 286 mod 23
- M = 10

**Final Plaintext:**
M = 10
