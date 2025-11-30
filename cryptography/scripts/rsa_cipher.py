M = 1234
e = 24377
n = 41567
d = 17393

C = pow(M, e, n)
print(f"Cipher text: {C}")

M_decrypted = pow(C, d, n)
print(f"Plain text: {M_decrypted}")
