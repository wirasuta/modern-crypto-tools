from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from time import time
from gui.common import *
from gui.layouts.cipher_layout import CipherWidget
from modern_crypto.rsa import *


class RSAWidget(CipherWidget):
    def _generate_key_pair(self):
        self.public_key, self.private_key = generate_rsa_key()
        self.button_save_pub.setDisabled(False)
        self.button_save_priv.setDisabled(False)
        self._update_enc_dec_state()

        message = QMessageBox(
            QMessageBox.NoIcon,
            'Modern Crypto Tools: RSA',
            f'Successfully created key pair'
        )
        message.exec()

    def _save_pub_key(self):
        pub_key_filename = save_file(
            self, 'Modern Crypto Tools: Save Public Key', 'default.pub', FILE_TYPE_FILTER['Public Key'])
        if not pub_key_filename:
            return
        save_key(pub_key_filename, self.public_key)

        message = QMessageBox(
            QMessageBox.NoIcon,
            'Modern Crypto Tools: RSA',
            f'Saved public key to {pub_key_filename}'
        )
        message.exec()

    def _save_priv_key(self):
        priv_key_filename = save_file(
            self, 'Modern Crypto Tools: Save Private Key', 'default.pri', FILE_TYPE_FILTER['Private Key'])
        if not priv_key_filename:
            return
        save_key(priv_key_filename, self.private_key)

        message = QMessageBox(
            QMessageBox.NoIcon,
            'Modern Crypto Tools: RSA',
            f'Saved private key to {priv_key_filename}'
        )
        message.exec()

    def _load_pub_key(self):
        pub_key_filename = open_file(
            self, 'Modern Crypto Tools: Load Public Key', FILE_TYPE_FILTER['Public Key'])
        if not pub_key_filename:
            return
        self.public_key = load_key(pub_key_filename)
        self.button_save_pub.setDisabled(False)
        self._update_enc_dec_state()

        message = QMessageBox(
            QMessageBox.NoIcon,
            'Modern Crypto Tools: RSA',
            f'Loaded public key from {pub_key_filename}'
        )
        message.exec()

    def _load_priv_key(self):
        priv_key_filename = open_file(
            self, 'Modern Crypto Tools: Load Private Key', FILE_TYPE_FILTER['Private Key'])
        if not priv_key_filename:
            return
        self.private_key = load_key(priv_key_filename)
        self.button_save_priv.setDisabled(False)
        self._update_enc_dec_state()

        message = QMessageBox(
            QMessageBox.NoIcon,
            'Modern Crypto Tools: RSA',
            f'Loaded private key from {priv_key_filename}'
        )
        message.exec()

    def _load_plaintext(self):
        pt_filename = open_file(
            self, 'Modern Crypto Tools: Load Plaintext', FILE_TYPE_FILTER['Any'])
        if not pt_filename:
            return
        with open(pt_filename, 'rb') as f:
            self.plaintext = f.read()
        self.text_area_pt.setText(self.plaintext.decode('ISO-8859-1'))

    def _save_plaintext(self):
        plaintext = self.plaintext if self.plaintext is not None else self.text_area_pt.toPlainText(
        ).encode('ISO-8859-1').replace(b'\n', b'\r')
        filename = 'default'
        pt_filename = save_file(
            self, 'Modern Crypto Tools: Save Plaintext', filename, FILE_TYPE_FILTER['Any'])
        if not pt_filename:
            return
        with open(pt_filename, 'wb+') as f:
            f.write(plaintext)

        message = QMessageBox(
            QMessageBox.NoIcon,
            'Modern Crypto Tools: RSA',
            f'Saved plaintext to {pt_filename}'
        )
        message.exec()

    def _load_ciphertext(self):
        ct_filename = open_file(
            self, 'Modern Crypto Tools: Load Ciphertext', FILE_TYPE_FILTER['Encrypted'])
        if not ct_filename:
            return
        with open(ct_filename, 'rb') as f:
            self.ciphertext = f.read()
        self.text_area_ct.setText(self.ciphertext.decode('ISO-8859-1'))

    def _save_ciphertext(self):
        ciphertext = self.ciphertext if self.ciphertext is not None else self.text_area_ct.toPlainText(
        ).encode('ISO-8859-1').replace(b'\n', b'\r')
        filename = 'default.enc'
        ct_filename = save_file(
            self, 'Modern Crypto Tools: Save Ciphertext', filename, FILE_TYPE_FILTER['Encrypted'])
        if not ct_filename:
            return
        with open(ct_filename, 'wb+') as f:
            f.write(ciphertext)

        message = QMessageBox(
            QMessageBox.NoIcon,
            'Modern Crypto Tools: RSA',
            f'Saved ciphertext to {ct_filename}'
        )
        message.exec()

    def _encrypt(self):
        self.plaintext = None
        pt = self.plaintext if self.plaintext is not None else self.text_area_pt.toPlainText(
        ).encode('ISO-8859-1').replace(b'\n', b'\r')
        start = time()
        self.ciphertext = encrypt(pt, self.public_key)
        end = time()
        self.plaintext = pt
        self.text_area_ct.setText(self.ciphertext.decode('ISO-8859-1'))

        message = QMessageBox(
            QMessageBox.NoIcon,
            'Modern Crypto Tools: RSA',
            f'Encrypted in {end - start:0.2f}s, ciphertext size {len(self.ciphertext)} bytes'
        )

        message.exec()

    def _decrypt(self):
        # self.ciphertext = None
        ct = self.ciphertext if self.ciphertext is not None else self.text_area_ct.toPlainText(
        ).encode('ISO-8859-1').replace(b'\n', b'\r')
        start = time()
        self.plaintext = decrypt(ct, self.private_key)
        end = time()
        self.text_area_pt.setText(self.plaintext.decode('ISO-8859-1'))

        message = QMessageBox(
            QMessageBox.NoIcon,
            'Modern Crypto Tools: RSA',
            f'Decrypted in {end - start:0.2f}s, plaintext size {len(self.plaintext)} bytes'
        )

        message.exec()

    def _update_enc_dec_state(self):
        if self.public_key:
            self.button_encrypt.setDisabled(False)

        if self.private_key:
            self.button_decrypt.setDisabled(False)