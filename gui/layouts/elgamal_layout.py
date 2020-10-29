from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from os import path
from gui.common import *
from gui.layouts.cipher_layout import CipherWidget
from modern_crypto.elgamal import *


class ElgamalWidget(CipherWidget):
    def _generate_key_pair(self):
        self.public_key, self.private_key = generate_eg_keypair()
        self.button_save_pub.setDisabled(False)
        self.button_save_priv.setDisabled(False)
        self._update_enc_dec_state()

        message = QMessageBox(
                QMessageBox.NoIcon,
                'Modern Crypto Tools: Elgamal',
                f'Successfully created key pair'
            )
        message.exec()
    
    def _save_pub_key(self):
        pub_key_filename = save_file(self, 'Modern Crypto Tools: Save Public Key', 'default.pub', FILE_TYPE_FILTER['Public Key'])
        if not pub_key_filename:
            return
        save_public_key(pub_key_filename, self.public_key)

        message = QMessageBox(
                QMessageBox.NoIcon,
                'Modern Crypto Tools: Elgamal',
                f'Saved public key to {pub_key_filename}'
            )
        message.exec()
    
    def _save_priv_key(self):
        priv_key_filename = save_file(self, 'Modern Crypto Tools: Save Private Key', 'default.pri', FILE_TYPE_FILTER['Private Key'])
        if not priv_key_filename:
            return
        save_private_key(priv_key_filename, self.private_key)

        message = QMessageBox(
                QMessageBox.NoIcon,
                'Modern Crypto Tools: Elgamal',
                f'Saved private key to {priv_key_filename}'
            )
        message.exec()
    
    def _load_pub_key(self):
        pub_key_filename = open_file(self, 'Modern Crypto Tools: Load Public Key', FILE_TYPE_FILTER['Public Key'])
        if not pub_key_filename:
            return
        self.public_key = load_public_key(pub_key_filename)
        self.button_save_pub.setDisabled(False)
        self._update_enc_dec_state()

        message = QMessageBox(
                QMessageBox.NoIcon,
                'Modern Crypto Tools: Elgamal',
                f'Loaded public key from {pub_key_filename}'
            )
        message.exec()
    
    def _load_priv_key(self):
        priv_key_filename = open_file(self, 'Modern Crypto Tools: Load Private Key', FILE_TYPE_FILTER['Private Key'])
        if not priv_key_filename:
            return
        self.private_key = load_private_key(priv_key_filename)
        self.button_save_priv.setDisabled(False)
        self._update_enc_dec_state()

        message = QMessageBox(
                QMessageBox.NoIcon,
                'Modern Crypto Tools: Elgamal',
                f'Loaded private key from {priv_key_filename}'
            )
        message.exec()

    # TODO: Handle binary file
    
    def _load_plaintext(self):
        pt_filename = open_file(self, 'Modern Crypto Tools: Load Plaintext', FILE_TYPE_FILTER['Any'])
        if not pt_filename:
            return
        with open(pt_filename, 'r') as f:
            content = f.read()
        self.text_area_pt.setText(content)
    
    def _save_plaintext(self):
        plaintext = self.text_area_pt.toPlainText()
        filename = 'default'
        pt_filename = save_file(self, 'Modern Crypto Tools: Save Plaintext', filename, FILE_TYPE_FILTER['Any'])
        if not pt_filename:
            return
        with open(pt_filename, 'w+') as f:
            content = f.write(plaintext)

        message = QMessageBox(
                QMessageBox.NoIcon,
                'Modern Crypto Tools: Elgamal',
                f'Saved plaintext to {pt_filename}'
            )
        message.exec()
    
    def _load_ciphertext(self):
        ct_filename = open_file(self, 'Modern Crypto Tools: Load Ciphertext', FILE_TYPE_FILTER['Encrypted'])
        if not ct_filename:
            return
        with open(ct_filename, 'r') as f:
            content = f.read()
        self.text_area_ct.setText(content)
    
    def _save_ciphertext(self):
        ciphertext = self.text_area_ct.toPlainText()
        filename = 'default.enc'
        ct_filename = save_file(self, 'Modern Crypto Tools: Save Ciphertext', filename, FILE_TYPE_FILTER['Encrypted'])
        if not ct_filename:
            return
        with open(ct_filename, 'w+') as f:
            content = f.write(ciphertext)

        message = QMessageBox(
                QMessageBox.NoIcon,
                'Modern Crypto Tools: Elgamal',
                f'Saved ciphertext to {ct_filename}'
            )
        message.exec()
    
    # TODO: Show size and time for encrypt and decrypt

    def _encrypt(self):
        pt = self.text_area_pt.toPlainText()
        ciphertext = encrypt(bytes(pt, 'ISO-8859-1'), self.public_key)
        self.text_area_ct.setText(ciphertext.decode('ISO-8859-1'))
    
    def _decrypt(self):
        ct = self.text_area_ct.toPlainText()
        plaintext = decrypt(bytes(ct, 'ISO-8859-1'), self.private_key)
        self.text_area_pt.setText(plaintext.decode('ISO-8859-1'))

    def _update_enc_dec_state(self):
        if self.public_key:
            self.button_encrypt.setDisabled(False)
        
        if self.private_key:
            self.button_decrypt.setDisabled(False)