#  Copyright (c)2025. zhengzongwei
#  flask-app is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

import os
import argparse
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

from hardware import HardwareInfo


class CryptoTool:
    def __init__(self, salt=None):
        if salt:
            self.salt = salt.encode()
        else:
            hw_info = HardwareInfo()
            self.salt = hw_info.generate_machine_code().encode()
        self.backend = default_backend()
        self.salt_size = 16  # 盐的大小
        self.iterations = 100_000  # 迭代次数
        self.nonce_size = 12
        self.key_size = 32


    def _derive_key(self, salt):
        # 使用PBKDF2HMAC从密码和盐中导出密钥
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=self.iterations,
            backend=self.backend
        )
        return kdf.derive(self.salt)

    def encrypt(self, data):
        salt = os.urandom(self.salt_size)
        key = self._derive_key(salt)
        aead = ChaCha20Poly1305(key)
        nonce = os.urandom(self.nonce_size)
        encrypted_data = aead.encrypt(nonce, data.encode(), None)
        return salt + nonce + encrypted_data

    def decrypt(self, token):
        salt = token[:self.salt_size]
        nonce = token[self.salt_size:self.salt_size + self.nonce_size]
        encrypted_data = token[self.salt_size + self.nonce_size:]
        key = self._derive_key(salt)
        aead = ChaCha20Poly1305(key)
        return aead.decrypt(nonce, encrypted_data, None).decode()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Encrypt or decrypt data using Fernet symmetric encryption with salt.")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform")
    parser.add_argument("data", help="Data to encrypt or decrypt")
    parser.add_argument("-s", "--salt", help="Salt for key derivation", default=None)

    args = parser.parse_args()

    tool = CryptoTool(args.salt)

    if args.action == "encrypt":
        encrypted_data = tool.encrypt(args.data)
        print(f"Encrypted data: {base64.urlsafe_b64encode(encrypted_data).decode()}")
    elif args.action == "decrypt":
        try:
            encrypted_data = base64.urlsafe_b64decode(args.data.encode())
            decrypted_data = tool.decrypt(encrypted_data)
            print(f"Decrypted data: {decrypted_data}")
        except Exception as e:
            print(f"Decryption failed: {e}")
