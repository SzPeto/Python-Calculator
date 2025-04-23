
import sys
from PyQt5.QtGui import QGuiApplication, QFont, QKeyEvent
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout,
                             QGridLayout, QLineEdit, QPushButton)

# Main class ****************************************************************************************************
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.window_width = 500
        self.window_height = 700
        self.screen = QGuiApplication.primaryScreen().geometry() # Get the dimension of the main screen
        self.center_window(self.screen)
        self.initUI()
        self.cls = False
        self.operator = ""
        self.result = float(0)
        self.operator_allowed = True
        self.setFocus() # Necessary for key event, for example in order for line edit to not steal key focus

    def initUI(self): # Good practice to initialize the UI through initUI
        self.setWindowTitle("Calculator")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid = QGridLayout()
        self.grid.setHorizontalSpacing(10)
        self.grid.setVerticalSpacing(10)
        self.central_widget.setLayout(self.grid)
        self.create_display()
        self.create_buttons()

    # Other methods *********************************************************************************************
    def center_window(self, screen):
        screen_width = screen.width()
        screen_height = screen.height()
        window_x = int((screen_width - self.window_width) / 2)
        window_y = int((screen_height - self.window_height) / 2)
        self.setGeometry(window_x, window_y, self.window_width, self.window_height)

    def create_display(self):
        self.display = QLineEdit()
        self.display.setText("0")
        self.display.setReadOnly(False)
        self.display.setFont(QFont("SansSerif", 30))
        self.grid.addWidget(self.display, 0, 0, 1, 4) # First, Second : row, column, Third, Fourth : span vertically,
                                                 # span horizontally

    def get_result(self):
        if self.operator == "+":
            self.result = self.result + float(self.display.text())
        elif self.operator == "-":
            self.result = self.result - float(self.display.text())
        elif self.operator == "*":
            self.result = self.result * float(self.display.text())
        elif self.operator == "/":
            self.result = self.result / float(self.display.text())
        else:
            self.result = float(self.display.text())
        print(f"Result = {self.result}")

    def handle_input(self, text):

        # After operator input clear the screen
        if self.cls:
            self.display.setText("0")
            self.cls = False

        # Checking if there is the operator sign at the end of digits
        if not self.display.text()[len(self.display.text()) - 1].isdigit():
            display_num = float(self.display.text()[0:-1])
        else:
            display_num = float(self.display.text())

        # Checking the button clicked
        if text == "0":
            if display_num == 0:
                self.display.setText("0")
            else:
                self.display.setText(self.display.text() + "0")
            self.operator_allowed = True
        elif text == "1":
            if display_num == 0:
                self.display.setText("1")
            else:
                self.display.setText(self.display.text() + "1")
            self.operator_allowed = True
        elif text == "2":
            if display_num == 0:
                self.display.setText("2")
            else:
                self.display.setText(self.display.text() + "2")
            self.operator_allowed = True
        elif text == "3":
            if display_num == 0:
                self.display.setText("3")
            else:
                self.display.setText(self.display.text() + "3")
            self.operator_allowed = True
        elif text == "4":
            if display_num == 0:
                self.display.setText("4")
            else:
                self.display.setText(self.display.text() + "4")
            self.operator_allowed = True
        elif text == "5":
            if display_num == 0:
                self.display.setText("5")
            else:
                self.display.setText(self.display.text() + "5")
            self.operator_allowed = True
        elif text == "6":
            if display_num == 0:
                self.display.setText("6")
            else:
                self.display.setText(self.display.text() + "6")
            self.operator_allowed = True
        elif text == "7":
            if display_num == 0:
                self.display.setText("7")
            else:
                self.display.setText(self.display.text() + "7")
            self.operator_allowed = True
        elif text == "8":
            if display_num == 0:
                self.display.setText("8")
            else:
                self.display.setText(self.display.text() + "8")
            self.operator_allowed = True
        elif text == "9":
            if display_num == 0:
                self.display.setText("9")
            else:
                self.display.setText(self.display.text() + "9")
            self.operator_allowed = True
        elif text.upper() == "C":
            self.display.setText("0")
            self.result = float(0)
            self.operator_allowed = True
        elif text == "+":
            if self.operator_allowed:
                self.get_result()
                self.cls = True
                self.operator = "+"
                self.operator_allowed = False
                self.display.setText(self.display.text() + "+")
        elif text == "-":
            if self.operator_allowed:
                self.get_result()
                self.cls = True
                self.operator = "-"
                self.operator_allowed = False
                self.display.setText(self.display.text() + "-")
        elif text == "*":
            if self.operator_allowed:
                self.get_result()
                self.cls = True
                self.operator = "*"
                self.operator_allowed = False
                self.display.setText(self.display.text() + "*")
        elif text == "/":
            if self.operator_allowed:
                self.get_result()
                self.cls = True
                self.operator = "/"
                self.operator_allowed = False
                self.display.setText(self.display.text() + "/")
        elif text == "=":
            self.get_result()
            self.operator = ""
            # Checking if the result is whole number, and in case if yes, printing without decimal places
            int_result = int(self.result)
            int_result = float(int_result)
            float_result = self.result
            if int_result == float_result:
                int_result = int(int_result)
                self.display.setText(str(int_result))
            else:
                self.display.setText(str(float_result))
            self.operator_allowed = True

    def on_button_clicked(self):
        sender = self.sender()
        text = sender.text()
        self.handle_input(text)

    def keyPressEvent(self, event: QKeyEvent):
        text = event.text()
        if event.key() == 16777221:
            text = "="
        self.handle_input(text)

    def create_buttons(self):
        #Three quotes for multi len string - this css-like styling includes the whole QButton group
        self.setStyleSheet("""
            QPushButton {
                font-family: Bahnschrift;
                font-size: 30px;
            }
        """)

        self.button_0 = QPushButton("0", self)
        self.button_0.clicked.connect(self.on_button_clicked)
        self.button_1 = QPushButton("1", self)
        self.button_1.clicked.connect(self.on_button_clicked)
        self.button_2 = QPushButton("2", self)
        self.button_2.clicked.connect(self.on_button_clicked)
        self.button_3 = QPushButton("3", self)
        self.button_3.clicked.connect(self.on_button_clicked)
        self.button_4 = QPushButton("4", self)
        self.button_4.clicked.connect(self.on_button_clicked)
        self.button_5 = QPushButton("5", self)
        self.button_5.clicked.connect(self.on_button_clicked)
        self.button_6 = QPushButton("6", self)
        self.button_6.clicked.connect(self.on_button_clicked)
        self.button_7 = QPushButton("7", self)
        self.button_7.clicked.connect(self.on_button_clicked)
        self.button_8 = QPushButton("8", self)
        self.button_8.clicked.connect(self.on_button_clicked)
        self.button_9 = QPushButton("9", self)
        self.button_9.clicked.connect(self.on_button_clicked)
        self.button_add = QPushButton("+", self)
        self.button_add.clicked.connect(self.on_button_clicked)
        self.button_subtract = QPushButton("-", self)
        self.button_subtract.clicked.connect(self.on_button_clicked)
        self.button_multiply = QPushButton("*", self)
        self.button_multiply.clicked.connect(self.on_button_clicked)
        self.button_divide = QPushButton("/", self)
        self.button_divide.clicked.connect(self.on_button_clicked)
        self.button_equals = QPushButton("=", self)
        self.button_equals.clicked.connect(self.on_button_clicked)
        self.button_clear_screen = QPushButton("C", self)
        self.button_clear_screen.clicked.connect(self.on_button_clicked)
        self.button_decimal = QPushButton(".", self)
        self.button_decimal.clicked.connect(self.on_button_clicked)
        self.button_plus_minus = QPushButton("+/-", self)
        self.button_plus_minus.clicked.connect(self.on_button_clicked)

        #Adding the buttons to grid layout
        self.grid.addWidget(self.button_plus_minus, 5, 0)
        self.grid.addWidget(self.button_0, 5, 1)
        self.grid.addWidget(self.button_decimal, 5, 2)
        self.grid.addWidget(self.button_equals, 5, 3)
        self.grid.addWidget(self.button_1, 4, 0)
        self.grid.addWidget(self.button_2, 4, 1)
        self.grid.addWidget(self.button_3, 4, 2)
        self.grid.addWidget(self.button_divide, 4, 3)
        self.grid.addWidget(self.button_4, 3, 0)
        self.grid.addWidget(self.button_5, 3, 1)
        self.grid.addWidget(self.button_6, 3, 2)
        self.grid.addWidget(self.button_multiply, 3, 3)
        self.grid.addWidget(self.button_7, 2, 0)
        self.grid.addWidget(self.button_8, 2, 1)
        self.grid.addWidget(self.button_9, 2, 2)
        self.grid.addWidget(self.button_subtract, 2, 3)
        self.grid.addWidget(self.button_clear_screen, 1, 0)
        self.grid.addWidget(self.button_add, 1, 3)