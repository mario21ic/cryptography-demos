from cryptography.fernet import Fernet

# Generar una clave
# key = Fernet.generate_key()
key = "QIRqW5PdDLyEEi4EBKaVfRi-X11rg5-GpG1YX3qS-_M="
print(f"Key: {key}")

# Crear una instancia de Fernet con la clave
cipher_suite = Fernet(key)

text = b"Hello, World!"

# Cifrar un mensaje
cipher_text = cipher_suite.encrypt(text)
print(f"Cipher text: {cipher_text}")

# Descifrar el mensaje
plain_text = cipher_suite.decrypt(cipher_text)
print(f"Plain text: {plain_text.decode()}")
