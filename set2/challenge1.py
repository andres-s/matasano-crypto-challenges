import utils

text = 'YELLOW SUBMARINE'
padded_text = utils.pad_pkcs_7(text, 20)
print('Padding YELLOW SUBMARINE with PKCS#7 to 20 bytes yields:')
print('{}'.format([c for c in padded_text]))
