from typing import List, Dict
from PyQt5.QtWidgets import *

APP_MODE: List[str] = ['RSA', 'Elgamal', 'Diffie-Hellman']
FILE_TYPE_FILTER: Dict[str, str] = {
    'Private Key': 'PRI File (*.pri);;All Files (*)',
    'Public Key': 'PUB File (*.pub);;All Files (*)',
    'Encrypted': 'ENC File (*.enc);;All Files (*)',
    'Any': 'All Files (*)'
}
WIDGET_MIN_DIM = 360


def open_file(parent: QWidget, dialog_title: str, file_filter: str):
    file_name, _ = QFileDialog.getOpenFileName(
        parent, dialog_title, '', file_filter)

    if file_name:
        return file_name


def save_file(parent: QWidget, dialog_title: str, default_file_name: str, file_filter: str):
    file_name, _ = QFileDialog.getSaveFileName(
        parent, dialog_title, default_file_name, file_filter)

    if file_name:
        return file_name
