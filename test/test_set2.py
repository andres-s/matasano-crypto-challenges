import unittest
import set2.utils as utils

class TestPadPKCS7(unittest.TestCase):
    def test_no_change_when_input_is_full_length(self):
        self.assertEqual(utils.pad_pkcs_7('foo', 3), 'foo')

    def test_input_is_one_byte_short(self):
        self.assertEqual(utils.pad_pkcs_7('foo', 4), 'foo' + chr(1))

    def test_input_is_four_bytes_short(self):
        text = 'YELLOW SUBMARINE'
        self.assertEqual(utils.pad_pkcs_7(text, 20), text + 4 * chr(4))
