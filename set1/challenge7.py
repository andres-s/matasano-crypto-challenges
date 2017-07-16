with open('7.txt') as fp:
    base64_encoded_ciphertext_lines = fp.readlines()

base64_encoded_ciphertext =
  ''.join(line.strip() for line in base64_encoded_ciphertext_lines)
