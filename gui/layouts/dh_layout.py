from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from os import path
from gui.common import *


class DHWidget(QWidget):
    def __init__(self, parent: QWidget):
        super(DHWidget, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        # Init layout
        self.layout = QVBoxLayout(self)

        # Add text area for n
        self.text_area_n = QTextEdit(self)
        self.text_area_n.resize(300, 100)
        self.text_area_n.setPlaceholderText('n')
        self.text_area_n.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.text_area_n)

        # Add text area for g
        self.text_area_g = QTextEdit(self)
        self.text_area_g.resize(300, 100)
        self.text_area_g.setPlaceholderText('g')
        self.text_area_g.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.text_area_g)

        # Add text area for x
        self.text_area_x = QTextEdit(self)
        self.text_area_x.resize(300, 100)
        self.text_area_x.setPlaceholderText('x')
        self.text_area_x.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.text_area_x)

        # Add text area for y
        self.text_area_y = QTextEdit(self)
        self.text_area_y.resize(300, 100)
        self.text_area_y.setPlaceholderText('y')
        self.text_area_y.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.text_area_y)

        # Add generate session key
        self.button_generate_key = QPushButton('Generate session key', self)
        self.button_generate_key.clicked.connect(self._generate_session_key)
        self.layout.addWidget(self.button_generate_key)

        self.setLayout(self.layout)
    
    def _generate_session_key(self):
        pass