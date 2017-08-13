import unittest

from set2.utils import CBCMode

class TestCBCMode(unittest.TestCase):
    def test_mix_block(self):
        cbc_mode = CBCMode(None)
        block, mixing_block = chr(0b01011100), chr(0b00101010)
        self.assertEqual(cbc_mode.mix_block(block, mixing_block), chr(0b01110110))
