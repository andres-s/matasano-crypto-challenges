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

