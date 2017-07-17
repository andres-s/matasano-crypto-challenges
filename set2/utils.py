def pad_pkcs_7(text, padded_length):
    bytes_to_pad = padded_length - len(text)
    return text + chr(bytes_to_pad) * bytes_to_pad
