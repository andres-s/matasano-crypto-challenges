def pad_pkcs_7(text, padded_length):
    bytes_to_pad = padded_length - len(text)
    return text + chr(bytes_to_pad) * bytes_to_pad

class BlockCipher:
    def __init__(self, cipher, mode):
        self.cipher = cipher
        self.mode = mode

    def encrypt(self, plaintext):
        blocks = self._split_into_blocks(plaintext)
        encrypted_blocks = []
        mixing_block = self.mode.initialisation_vector
        for block in blocks:
            mixed_block = self.mode.mix_block(block, mixing_block)
            encrypted_block = self.cipher.encrypt(mixed_block)
            mixing_block = encrypted_block
            encrypted_blocks.append(encrypted_block)
        return ''.join(encrypted_blocks)

    def decrypt(self, ciphertext):
        blocks = self._split_into_blocks(ciphertext)
        decrypted_blocks = []
        self.mode.start_new_message()
        for block in blocks:
            mixed_block = self.cipher.decrypt(block)
            decrypted_block = self.mode.unmix_block(mixed_block)
            decrypted_blocks.append(decrypted_block)
        return ''.join(decrypted_block)

    def _split_into_blocks(self, text):
        block_size = self.cipher.block_size()
        blocks = []
        idx = 0
        while idx < len(text):
            next_block_start_idx = idx + block_size
            blocks.append(text[idx:next_block_start_idx])
            idx = next_block_start_idx
        return blocks
