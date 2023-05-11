import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from test import Test

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")

        self.label_login = QLabel("Логин:")
        self.login_edit = QLineEdit()
        self.label_password = QLabel("Пароль:")
        self.password_edit = QLineEdit()
        self.button_auth = QPushButton("Войти")
        self.button_exit = QPushButton("Выйти")
        self.button_auth.clicked.connect(self.auth)
        self.button_exit.clicked.connect(self.exit)
        

        self.captcha_dialog = CaptchaDialog(parent=self)
        self.captcha_dialog.setModal(True)

        self.login_attempts = 0

        layout = QVBoxLayout()
        layout.addWidget(self.label_login)
        layout.addWidget(self.login_edit)
        layout.addWidget(self.label_password)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.button_auth)
        layout.addWidget(self.button_exit)

        self.setLayout(layout)

    def auth(self):
        username = self.login_edit.text()
        password = self.password_edit.text()

        if username == "1" and password == "1":
            self.test = Test()
            self.test.show()
        else:
        
            self.captcha_dialog.start_timer()
                
            if self.captcha_dialog.exec() == QDialog.DialogCode.Accepted:
                QMessageBox.information(self, "Успех", "Вход выполнен после капчи")
                
            else:
                QMessageBox.warning(self, "Ошибка", "Неверные данные и капча")
                self.login_attempts = 0
                
    def exit(self):
        app.exit()
                
class CaptchaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Капча")
        self.label = QLabel("Введите капчу:")
        self.textbox = QLineEdit()
        self.button = QPushButton("Проверить")
        self.button.clicked.connect(self.verify_captcha)

        self.timer_label = QLabel("Таймер: 10")
        self.timer_counter = 10
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def verify_captcha(self):
        captcha = self.textbox.text()
        print("Проверка капчи:", captcha)
        
        if captcha.lower() == "captcha":  
            self.accept()
        else:
            self.textbox.setDisabled(True)  
            self.timer_counter = 11
            self.timer.start()
            QMessageBox.critical(self, "Ошибка", "Неправильная капча")

    def start_timer(self):
        self.timer_counter = 10
        self.timer.start()

    def update_timer(self):
        self.timer_counter -= 1
        self.timer_label.setText(f"Таймер: {self.timer_counter}")

        if self.timer_counter == 0 :
            self.timer.stop()
            self.textbox.setDisabled(False)
            
app = QApplication(sys.argv)
exe = LoginWindow()
exe.show()
app.exec()
