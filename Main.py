import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow

def initialize_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

def main():
    initialize_app()

if __name__ == "__main__":
    main()