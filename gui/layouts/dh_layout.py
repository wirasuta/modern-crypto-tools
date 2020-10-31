from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from os import path
from gui.common import *
from modern_crypto.diffie_hellman import *


class DHWidget(QWidget):
    def __init__(self, parent: QWidget):
        super(DHWidget, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        # Init layout
        self.layout = QVBoxLayout(self)

        # Add text area for n
        self.text_area_n = QTextEdit(self)
        self.text_area_n.resize(300, 50)
        self.text_area_n.setPlaceholderText('n')
        self.text_area_n.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.text_area_n)

        # Add text area for g
        self.text_area_g = QTextEdit(self)
        self.text_area_g.resize(300, 50)
        self.text_area_g.setPlaceholderText('g')
        self.text_area_g.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.text_area_g)

        # Add generate random n and g
        self.button_generate_random_n_g = QPushButton('Generate random n and g', self)
        self.button_generate_random_n_g.clicked.connect(self._generate_random_n_g)
        self.layout.addWidget(self.button_generate_random_n_g)

        # Add text area for x
        self.text_area_x = QTextEdit(self)
        self.text_area_x.resize(300, 50)
        self.text_area_x.setPlaceholderText('x is your secret number')
        self.text_area_x.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.text_area_x)

        # Calculate X
        self.text_area_x_calculation = QTextEdit(self)
        self.text_area_x_calculation.resize(300, 50)
        self.text_area_x_calculation.setReadOnly(True)
        # self.text_area_x_calculation.setHidden(True)
        self.text_area_x_calculation.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.text_area_x_calculation)

        # Add X calculation
        self.button_generate_x_calculation = QPushButton('Calculate X for other party (if x empty, it will automatically be filled with random number)', self)
        self.button_generate_x_calculation.clicked.connect(self._generate_x_calculation)
        self.layout.addWidget(self.button_generate_x_calculation)

        # Add text area for Y
        self.text_area_y = QTextEdit(self)
        self.text_area_y.resize(300, 50)
        self.text_area_y.setPlaceholderText('Y value is received by the other party')
        self.text_area_y.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.text_area_y)

        # Add generate session key
        self.button_generate_key = QPushButton('Generate session key', self)
        self.button_generate_key.clicked.connect(self._generate_session_key)
        self.layout.addWidget(self.button_generate_key)

        # Add session key result
        self.text_area_result = QTextEdit(self)
        self.text_area_result.resize(300, 100)
        self.text_area_result.setReadOnly(True)
        self.text_area_result.setHidden(True)
        self.text_area_result.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.text_area_result)

        self.setLayout(self.layout)

    def _generate_random_n_g(self):
        g, n = generate_shared_parameter()

        self.text_area_g.setText(str(g))
        self.text_area_n.setText(str(n))

        message = QMessageBox(
            QMessageBox.NoIcon,
            'Modern Crypto Tools: Diffie-Hellman',
            f'Generated shared prime number n and g'
        )
        message.exec()

    def _generate_x_calculation(self):
        g = int(self.text_area_g.toPlainText())
        n = int(self.text_area_n.toPlainText())
        x = self.text_area_x.toPlainText()

        if (x is None or x==''):
            x = generate_secret_pow()
            self.text_area_x.setText(str(x))
        else:
            x = int(x)

        X = shared_op(g, n, x)

        self.text_area_x_calculation.setText(str(X))

    def _generate_session_key(self):
        n = int(self.text_area_n.toPlainText())
        g = int(self.text_area_g.toPlainText())
        Y = int(self.text_area_y.toPlainText())
        x = int(self.text_area_x.toPlainText())

        K = generate_private_key(Y, n, x)

        self.text_area_result.setText(str(K))
        self.text_area_result.setHidden(False)

        message = QMessageBox(
            QMessageBox.NoIcon,
            'Modern Crypto Tools: Diffie-Hellman',
            f'Generated shared secret key'
        )
        message.exec()


