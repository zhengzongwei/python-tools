import random
import string
import unittest
from common.utils.qrcode import QRCode

def generate_random_name(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        qrcode = QRCode()
        msg = generate_random_name()
        print(f"Message: {msg}")
        QRCode.generate_qrcode(msg)
        parse_msg = QRCode.read_qrcode()

        self.assertEqual(parse_msg, msg)  # add assertion here


if __name__ == '__main__':
    unittest.main()
