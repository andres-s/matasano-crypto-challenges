import codec
import utils

with open('10.txt') as fp:
    base64_encoded_lines = fp.readlines()

base_64_encoded_ciphertext = ''.join(base64_encoded_lines)
ciphertext = codec.decode(base_64_encoded_ciphertext, 'base64')

cipher = utils.BlockCipher(utils.AES(KEY), utils.CBC(INITIALISATION_VECTOR))
plaintext = cipher.decrypt(ciphertext)
