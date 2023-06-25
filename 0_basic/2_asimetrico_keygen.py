from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Generar un par de claves
private_key = rsa.generate_private_key(
   public_exponent=65537,
   key_size=2048,
)

private_key_file = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)
#print("private_key_file", private_key_file)
with open("private.pem", 'wb') as file:
    file.write(private_key_file)


# Serializar la clave pública para compartirla
public_key = private_key.public_key()
public_pem = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("public_pem", public_pem)
with open("public.pem", 'wb') as file:
    file.write(public_pem)

"""
# Cifrar un mensaje
cipher_text = public_key.encrypt(
   b"Hello, World!",
   padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None
   )
)
print(f"Cipher text: {cipher_text}")

# Descifrar el mensaje
plain_text = private_key.decrypt(
   cipher_text,
   padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None
   )
)
print(f"Plain text: {plain_text.decode()}")
"""
