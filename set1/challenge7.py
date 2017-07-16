import codecs
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

with open('7.txt') as fp:
    base64_encoded_ciphertext_lines = fp.readlines()

base64_encoded_ciphertext = ''.join(
        line.strip() for line in base64_encoded_ciphertext_lines)

ciphertext = codecs.decode(base64_encoded_ciphertext, 'base64')

backend = default_backend()
key = 'YELLOW SUBMARINE'
cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

print(plaintext)
