import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import datetime
import webbrowser
import socket

app = QApplication(sys.argv)
main_win = QWidget()
main_win.setWindowTitle("heyndra AI (ask question)")
main_win.setGeometry(100, 100, 500, 600)
layout = QVBoxLayout()


def generate_response(user_input):
    hostname = socket.gethostname()
    user_input = user_input.lower()
    if "hello" in user_input:
        return "hello", hostname ,"how may i assist you?"
    elif "who created you" in user_input:
        return "i created by electro micro since 2024 before relase"
    elif "what programing language that you was written" in user_input:
        return "its python (with library PyQT, datetime, webbrowser, and socket)"
    elif "what time is it now" in user_input:
        return f"the time now is {datetime.datetime.now().strftime('%H:%M:%S')}."
    elif "what date is it now" in user_input:
        return f"the date now is {datetime.datetime.now().strftime('%Y-%M-%d')}."
    elif "what programming language that are low level" in user_input:
        return "its assembly, HDL, mips assembly, machine code"
    elif "what programming language that are high level" in user_input:
        return "its fortran, SQL, golang, javascript, java, C++, python"
    elif "what is the first computer in the world" in user_input:
        return "its eniac. created in 17 february 1946"
    elif "what is electro micro" in user_input:
        return "its a software and hardware company who developed anything to sell of publish"
    elif "what is python (snake)" in user_input:
        return "its a snake found in asia, africa, autralia"
    elif "who painted mona lisa" in user_input:
        return "its leonardo da vinci"
    elif "why you was written in python" in user_input:
        return "cuz my developer was a full stack developer"
    else:
        return "sorry. i didn't understand"
    
def send_message():
    hostname = socket.gethostname()
    user_input = input_field.text()
    conversation.append(f"{hostname}: {user_input}")
    response = generate_response(user_input)
    conversation.append(f"AI: {response}")
    input_field.clear()

title = QLabel("heyndra AI", main_win)
title.setFont(QFont("Arial", 20, QFont.Bold))
title.setAlignment(Qt.AlignCenter)
layout.addWidget(title)

conversation = QTextEdit(main_win)
conversation.setReadOnly(True)
layout.addWidget(conversation)

input_field = QLineEdit(main_win)
input_field.setPlaceholderText("ask me for commanding")
layout.addWidget(input_field)

send_button = QPushButton("send", main_win)
send_button.clicked.connect(send_message)
layout.addWidget(send_button)

main_win.setLayout(layout)

main_win.show()

sys.exit(app.exec_())
