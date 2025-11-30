# Exercise 3

## 1. CBC Mode (Cipher Block Chaining)

In CBC mode, the decryption process is defined as:

**P_i = D_k(C_i) ⊕ C_(i-1)**

(Where C_0 is the IV)

**Effect on Decrypted Block P_1:**
* **Formula:** P_1' = D_k(C_1) ⊕ IV
* **Analysis:** If C_1 has 1 wrong bit, then the entire output of D_k(C_1) is corrupted (all bits corrupted).
* **Result:** The entire block **P_1' is completely corrupted** (random garbage), so 128 bits corrupted.

**Effect on Decrypted Block P_2:**
* **Formula:** P_2' = D_k(C_2) ⊕ C_1
* **Analysis:** C_2 is received correctly, so the output of D_k(C_2) is correct. However, this result is XORed with C_1 (which contains the 1-bit error) to produce P_2'.
* **Result:** **P_2' contains exactly one bit error** at the same position as the error in C_1.

In total, we have 128+1=**129 bits corrupted** (first 128 bits, and 1 bit at same position where the error at C_1 happened).

---

## 2. CFB Mode (Cipher Feedback)

In CFB mode, the decryption process is:

**P_i = C_i ⊕ E_k(C_(i-1))**

(Where C_0 is the IV)

**Effect on Decrypted Block P_1':**
* **Formula:** P_1' = C_1 ⊕ E_k(IV)
* **Analysis:** The keystream component E_k(IV) is generated using the IV, which is correct. The corruption is only in C_1, which is directly XORed with the keystream.
* **Result:** **P_1 contains exactly one bit error** at the specific position where C_1 was corrupted.

**Effect on Decrypted Block P_2':**
* **Formula:** P_2' = C_2 ⊕ E_k(C_1)
* **Analysis:** To decrypt P_2, the algorithm must encrypt the previous ciphertext block C_1 to create the keystream. Since C_1 has a bit error and is the input to the encryption function E_k, then the entire output is corrupted.
* **Result:** The entire block **P_2' is completely corrupted** (random garbage).

In total, we have 128+1=**129 bits corrupted** (one bit at the same position where the error at C_1 happened, and the remaining 128 bits).
