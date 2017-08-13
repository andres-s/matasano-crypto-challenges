import unittest
from set2.utils import BlockCipher

class ReverseCipher:
    def block_size(self):
        return 4

    def encrypt(self, block):
        return self._reverse(block)

    def decrypt(self, block):
        return self._reverse(block)

    def _reverse(self, string):
        return ''.join(reversed(string))

class AlphabetShiftMode:
    # Only handles lower case letters

    def __init__(self, initialisation_vector):
        self.initialisation_vector = initialisation_vector

    def mix_block(self, block, mixing_block):
        block_alphabet_positions = map(lambda c: ord(c) - ord('a'), block)
        mixer_alphabet_positions = map(lambda c: ord(c) - ord('a'), mixing_block)
        return_alphabet_positions = \
            [ a + b for a, b in zip(block_alphabet_positions, mixer_alphabet_positions) ]
        return_letters = map(lambda i: chr(ord('a') + i), return_alphabet_positions)
        return_block = ''.join(return_letters)
        return return_block

class TestBlockCipher(unittest.TestCase):
    def test_encrypt_single_block(self):
        block_cipher = BlockCipher(ReverseCipher(), AlphabetShiftMode('aaaa'))
        self.assertEqual(block_cipher.encrypt('abcd'), 'dcba')

    def test_encrypt_single_block_nonzero_init_vector(self):
        block_cipher = BlockCipher(ReverseCipher(), AlphabetShiftMode('abcd'))
        self.assertEqual(block_cipher.encrypt('abcd'), 'geca')

    def test_encrypt_two_blocks(self):
        block_cipher = BlockCipher(ReverseCipher(), AlphabetShiftMode('abcd'))
        self.assertEqual(block_cipher.encrypt('abcdefgh'), 'gecahijk')
