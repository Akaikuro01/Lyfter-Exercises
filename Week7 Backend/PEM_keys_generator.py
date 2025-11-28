# gen_keys.py  (run once)
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

def generate_private_key():
    private_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,      # "BEGIN PRIVATE KEY"
        encryption_algorithm=serialization.NoEncryption(),
    ).decode()

    return private_pem

def generate_puplic_key():
    public_pem = key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,  # "BEGIN PUBLIC KEY"
    ).decode()

    return public_pem

private_key = generate_private_key()
public_key = generate_puplic_key()

print(private_key)
print(public_key)