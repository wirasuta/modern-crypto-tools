import sys
from PyQt5.QtWidgets import QApplication
from gui import App

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = App()
    sys.exit(app.exec_())
