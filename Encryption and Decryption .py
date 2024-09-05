
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_object = Fernet(key)

a = input("Enter your message: ")
cipher_text = cipher_object.encrypt(a.encode())

print("Your key is: ", key.decode())
print("Your encrypted message is: ", cipher_text.decode())

b = input("Enter your key to decrypt the message: ")

if b.encode() == key:

    decrypted_text = cipher_object.decrypt(cipher_text).decode()
    print("Decrypted message: ", decrypted_text)
else:
    print("The key is incorrect")
