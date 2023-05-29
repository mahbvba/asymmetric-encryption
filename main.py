from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
key = RSA.generate(2048)

# Get public and private keys
public_key = key.publickey()
private_key = key

# Message to be encrypted
message = input("Enter a message: ")

# Encrypt the message
cipher = PKCS1_OAEP.new(public_key)
encrypted_message = cipher.encrypt(message.encode())

# Decrypt the message
cipher = PKCS1_OAEP.new(private_key)
decrypted_message = cipher.decrypt(encrypted_message)

# Print the results
print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message.decode())

