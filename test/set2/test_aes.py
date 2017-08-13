import unittest

import set2.aes as aes

class TestSubBytes(unittest.TestCase):
    def test_sub_bytes(self):
        state = [ [chr(0x00), chr(0x40), chr(0x80), chr(0xc0)],
                  [chr(0x10), chr(0x50), chr(0x90), chr(0xd0)],
                  [chr(0x20), chr(0x60), chr(0xa0), chr(0xe0)],
                  [chr(0x30), chr(0x70), chr(0xb0), chr(0xf0)] ]

        expected = [ [chr(0x63), chr(0x09), chr(0xcd), chr(0xba)],
                     [chr(0xca), chr(0x53), chr(0x60), chr(0x70)],
                     [chr(0xb7), chr(0xd0), chr(0xe0), chr(0xe1)],
                     [chr(0x04), chr(0x51), chr(0xe7), chr(0x8c)] ]

        self.assertEqual(aes.sub_bytes(state), expected)

class TestShiftRows(unittest.TestCase):
    def test_shift_rows(self):
        state = [ [chr(0x00), chr(0x01), chr(0x02), chr(0x03)],
                  [chr(0x10), chr(0x11), chr(0x12), chr(0x13)],
                  [chr(0x20), chr(0x21), chr(0x22), chr(0x23)],
                  [chr(0x30), chr(0x31), chr(0x32), chr(0x33)] ]

        expected = [ [chr(0x00), chr(0x01), chr(0x02), chr(0x03)],
                     [chr(0x11), chr(0x12), chr(0x13), chr(0x10)],
                     [chr(0x22), chr(0x23), chr(0x20), chr(0x21)],
                     [chr(0x33), chr(0x30), chr(0x31), chr(0x32)] ]

        self.assertEqual(aes.shift_rows(state), expected)

class TestMixColumns(unittest.TestCase):
    def test_mix_columns(self):
        state = [ [chr(0x63), chr(0x09), chr(0xcd), chr(0xba)],
                  [chr(0x53), chr(0x60), chr(0x70), chr(0xca)],
                  [chr(0xe0), chr(0xe1), chr(0xb7), chr(0xd0)],
                  [chr(0x8c), chr(0x04), chr(0x51), chr(0xe7)] ]

        expected = [ [chr(0x5f), chr(0x57), chr(0xf7), chr(0x1d)],
                     [chr(0x72), chr(0xf5), chr(0xbe), chr(0xb9)],
                     [chr(0x64), chr(0xbc), chr(0x3b), chr(0xf9)],
                     [chr(0x15), chr(0x92), chr(0x29), chr(0x1a)] ]

        self.assertEqual(aes.mix_columns(state), expected)
