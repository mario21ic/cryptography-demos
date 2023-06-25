import hmac
import hashlib

# Clave secreta => simetrico
key = b'my_secret_key'

# Mensaje original
message = b'This is a message'

# Crear un nuevo objeto HMAC para el mensaje original
h_original = hmac.new(key, message, hashlib.sha256)

# HMAC original en formato hexadecimal
original_hmac = h_original.hexdigest()
print(f"Original HMAC: {original_hmac}")

# Supongamos que recibimos un mensaje y un HMAC y queremos verificarlo
# received_message = b'This is a message'  # este debería ser el mensaje recibido
received_message = b'This is a messagexD'  # este debería ser el mensaje recibido
received_hmac = original_hmac  # este debería ser el HMAC recibido

# Crear un nuevo objeto HMAC para el mensaje recibido
h_received = hmac.new(key, received_message, hashlib.sha256)

# Comprobar si el HMAC recibido coincide con el HMAC calculado
if hmac.compare_digest(h_received.hexdigest(), received_hmac):
    print("El mensaje es auténtico y no ha sido alterado.")
else:
    print("El mensaje no es auténtico o ha sido alterado.")
