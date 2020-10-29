from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from os import path
from gui.common import *


class CipherWidget(QWidget):
    def __init__(self, parent: QWidget):
        super(CipherWidget, self).__init__(parent)
        self._init_ui()

        self.public_key = None
        self.private_key = None

    def _init_ui(self):
        # Init layout
        self.layout = QVBoxLayout(self)

        # Add generate key
        self.button_generate_key = QPushButton('Generate key pair', self)
        self.button_generate_key.clicked.connect(self._generate_key_pair)
        self.layout.addWidget(self.button_generate_key)

        # Add save pub and priv key
        h_frame_widget = QWidget()
        h_frame_layout = QHBoxLayout()
        h_frame_layout.setContentsMargins(0, 0, 0, 0)

        self.button_save_pub = QPushButton('Save public key', self)
        self.button_save_pub.clicked.connect(self._save_pub_key)
        self.button_save_pub.setDisabled(True)
        h_frame_layout.addWidget(self.button_save_pub)

        self.button_save_priv = QPushButton('Save private key', self)
        self.button_save_priv.clicked.connect(self._save_priv_key)
        self.button_save_priv.setDisabled(True)
        h_frame_layout.addWidget(self.button_save_priv)

        h_frame_widget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_frame_widget.setLayout(h_frame_layout)
        self.layout.addWidget(h_frame_widget)

        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        self.layout.addWidget(sep)

        # Add load and save plaintext file button
        h_frame_widget_pt = QWidget()
        h_frame_layout_pt = QHBoxLayout()
        h_frame_layout_pt.setContentsMargins(0, 0, 0, 0)

        self.button_load_pt = QPushButton('Load plaintext', self)
        self.button_load_pt.clicked.connect(self._load_plaintext)
        h_frame_layout_pt.addWidget(self.button_load_pt)

        self.button_save_pt = QPushButton('Save plaintext', self)
        self.button_save_pt.clicked.connect(self._save_plaintext)
        h_frame_layout_pt.addWidget(self.button_save_pt)

        self.button_load_pub_key = QPushButton('Load public key', self)
        self.button_load_pub_key.clicked.connect(self._load_pub_key)
        h_frame_layout_pt.addWidget(self.button_load_pub_key)

        h_frame_widget_pt.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_frame_widget_pt.setLayout(h_frame_layout_pt)
        self.layout.addWidget(h_frame_widget_pt)

        # Add text area for plaintext
        self.text_area_pt = QTextEdit(self)
        self.text_area_pt.resize(300, 300)
        self.text_area_pt.setPlaceholderText('Load or type your plaintext...')
        self.text_area_pt.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.text_area_pt)

        # Add save encrypt and decrypt
        h_frame_widget2 = QWidget()
        h_frame_layout2 = QHBoxLayout()
        h_frame_layout2.setContentsMargins(0, 0, 0, 0)

        self.button_encrypt = QPushButton('Encrypt', self)
        self.button_encrypt.clicked.connect(self._encrypt)
        self.button_encrypt.setDisabled(True)
        h_frame_layout2.addWidget(self.button_encrypt)

        self.button_decrypt = QPushButton('Decrypt', self)
        self.button_decrypt.clicked.connect(self._decrypt)
        self.button_decrypt.setDisabled(True)
        h_frame_layout2.addWidget(self.button_decrypt)

        h_frame_widget2.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_frame_widget2.setLayout(h_frame_layout2)
        self.layout.addWidget(h_frame_widget2)

        # Add text area for ciphertext
        self.text_area_ct = QTextEdit(self)
        self.text_area_ct.resize(300, 300)
        self.text_area_ct.setPlaceholderText('Load or type your ciphertext...')
        self.text_area_ct.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.text_area_ct)

        # Add load and save ciphertext file button
        h_frame_widget_ct = QWidget()
        h_frame_layout_ct = QHBoxLayout()
        h_frame_layout_ct.setContentsMargins(0, 0, 0, 0)

        self.button_load_ct = QPushButton('Load ciphertext', self)
        self.button_load_ct.clicked.connect(self._load_ciphertext)
        h_frame_layout_ct.addWidget(self.button_load_ct)

        self.button_save_ct = QPushButton('Save ciphertext', self)
        self.button_save_ct.clicked.connect(self._save_ciphertext)
        h_frame_layout_ct.addWidget(self.button_save_ct)

        self.button_load_priv_key = QPushButton('Load private key', self)
        self.button_load_priv_key.clicked.connect(self._load_priv_key)
        h_frame_layout_ct.addWidget(self.button_load_priv_key)

        h_frame_widget_ct.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_frame_widget_ct.setLayout(h_frame_layout_ct)
        self.layout.addWidget(h_frame_widget_ct)

        self.setLayout(self.layout)
    
    def _generate_key_pair(self):
        pass
    
    def _save_pub_key(self):
        pass
    
    def _save_priv_key(self):
        pass
    
    def _load_pub_key(self):
        pass
    
    def _load_priv_key(self):
        pass
    
    def _load_plaintext(self):
        pass
    
    def _save_plaintext(self):
        pass
    
    def _load_ciphertext(self):
        pass
    
    def _save_ciphertext(self):
        pass
    
    def _encrypt(self):
        pass
    
    def _decrypt(self):
        pass