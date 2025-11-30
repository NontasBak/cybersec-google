# Exercise 1

## a) Finding the Key

We organize the ciphertext `LXFOPVEFRNHR` into 5 batches based on the key length of 5.

* **Batch 1:** Letters at indices 0, 5, 10 (L, V, H)
* **Batch 2:** Letters at indices 1, 6, 11 (X, E, R)
* **Batch 3:** Letters at indices 2, 7 (F, F)
* **Batch 4:** Letters at indices 3, 8 (O, R)
* **Batch 5:** Letters at indices 4, 9 (P, N)

Frequency Table for each batch:

| # | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **#1** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** | 0 | 0 | 0 | **1** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** | 0 | 0 | 0 | 0 |
| **#2** | 0 | 0 | 0 | 0 | **1** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** | 0 | 0 | 0 | 0 | 0 | **1** | 0 | 0 |
| **#3** | 0 | 0 | 0 | 0 | 0 | **2** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **#4** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** | 0 | 0 | **1** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **#5** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** | 0 | **1** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

---

We analyze each row to find the shift that maps the letters to high-frequency English letters (like **e, t, a, o, i, n**).

**Row #3 (Letters: F, F):**
* **Observation:** The letter `F` appears 100% of the time.
* **Hypothesis:** If `F` (5) corresponds to the common letter `t` (19):
    * Shift = 5 - 19 = -14 = 12 (mod 26).
    * The 12th letter is **M**.
* **Key Letter:** **M**

**Row #4 (Letters: O, R):**
* **Observation:** We have `O` (14) and `R` (17). They are 3 spots apart.
* **Hypothesis:** Common letters separated by 3 spots are `a` (0) and `d` (3).
    * Shift = 14 - 0 = 14.
    * The 14th letter is **O**.
* **Key Letter:** **O**

**Row #5 (Letters: P, N):**
* **Observation:** `P` (15) and `N` (13).
* **Hypothesis:** If `N` maps to `a` (0), the shift is 13.
    * P (15) - 13 = 2 (`c`).
    * N (13) - 13 = 0 (`a`).
    * "ca" seems valid
* **Key Letter:** **N**

**Row #1 (Letters: L, V, H):**
* **Hypothesis:** If we try Key **L** (11):
    * L (11) - 11 = 0 (`a`).
    * V (21) - 11 = 10 (`k`).
    * H (7) - 11 = -4 ≡ 22 (`w`).
    * "akw" seems valid
* **Key Letter:** **L**

**Row #2 (Letters: X, E, R):**
* **Hypothesis:** If we try Key **E** (4):
    * X (23) - 4 = 19 (`t`).
    * E (4) - 4 = 0 (`a`).
    * R (17) - 4 = 13 (`n`).
    * "tan" seems valid
* **Key Letter:** **E**

**Recovered Key:** `LEMON`

---

We decrypt using the formula P = (C - K) mod 26.

| Cipher Letter | Key Letter | Calculation (C - K) | Plaintext |
| :--- | :--- | :--- | :--- |
| **L** (11) | **L** (11) | 11 - 11 = 0 | **a** |
| **X** (23) | **E** (4) | 23 - 4 = 19 | **t** |
| **F** (5) | **M** (12) | 5 - 12 = -7 → 19 | **t** |
| **O** (14) | **O** (14) | 14 - 14 = 0 | **a** |
| **P** (15) | **N** (13) | 15 - 13 = 2 | **c** |
| **V** (21) | **L** (11) | 21 - 11 = 10 | **k** |
| **E** (4) | **E** (4) | 4 - 4 = 0 | **a** |
| **F** (5) | **M** (12) | 5 - 12 = -7 → 19 | **t** |
| **R** (17) | **O** (14) | 17 - 14 = 3 | **d** |
| **N** (13) | **N** (13) | 13 - 13 = 0 | **a** |
| **H** (7) | **L** (11) | 7 - 11 = -4 → 22 | **w** |
| **R** (17) | **E** (4) | 17 - 4 = 13 | **n** |

**Decrypted Message:** `attackatdawn`
