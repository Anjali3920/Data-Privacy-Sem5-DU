#Write a program to perform encryption and decryption using Rail Fence Cipher 
#(transpositional cipher) 
from cryptography.fernet import Fernet

def generate_key():
    """Generate a key for encryption and decryption."""
    return Fernet.generate_key()

def encrypt_data(data, key):
    """Encrypt the data using the provided key."""
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return encrypted

def decrypt_data(encrypted_data, key):
    """Decrypt the data using the provided key."""
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data).decode()
    return decrypted

key=generate_key
text=str(input("Enter the text to be encrypted: "))
encrypted_text=encrypt_data(text,key)
print("Encrypted text:", encrypted_text)
decrypted_text=decrypt_data(encrypted_text,key)
print("Decrypted text:", decrypted_text)







"""

# Rail Fence Cipher Encryption and Decryption

def encrypt(text, key):
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    direction = False
    row, col = 0, 0

    for char in text:
        rail[row][col] = char
        col += 1

        if row == 0 or row == key - 1:
            direction = not direction

        row += 1 if direction else -1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])

    return "".join(result)


def decrypt(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    direction = None
    row, col = 0, 0

    for i in range(len(cipher)):
        rail[row][col] = '*'
        col += 1

        if row == 0:
            direction = True
        elif row == key - 1:
            direction = False

        row += 1 if direction else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0

    for i in range(len(cipher)):
        result.append(rail[row][col])
        col += 1

        if row == 0:
            direction = True
        elif row == key - 1:
            direction = False

        row += 1 if direction else -1

    return "".join(result)


text = input("Enter the text: ")
key = int(input("Enter the number of rails: "))

encrypted_text = encrypt(text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
"""
