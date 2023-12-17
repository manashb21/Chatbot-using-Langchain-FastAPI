from cryptography.fernet import Fernet

key = "13haha34X@#$jsdfjk12348df49757374lsdfjhehr2fj4jf"

enc = Fernet.generate_key()

print("\nFernet Generate key:")
print(enc)

cipher = Fernet(enc)

encrypted_key = cipher.encrypt(key.encode())

print("\nOriginal Key:")
print(key)
print("\nEncrypted:")
print(encrypted_key.decode())
print("\nDecrypted:")
print(cipher.decrypt(encrypted_key).decode())