import sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel, QSqlQuery
from main import Main
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно входа")

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('postgres')
        db.setHostName('Localhost')
        db.setPort(5432)
        db.setPassword('univer')
        db.setUserName('postgres')
        db.open()
        
        self.label_username = QLabel("Логин:")
        self.login_edit = QLineEdit()
        self.label_password = QLabel("Пароль:")
        self.password_edit = QLineEdit()
        self.button_login = QPushButton("Войти")
        self.btn_exit = QPushButton("Выход")
        self.table = QTableView()
        self.stm = QSqlTableModel(parent=self.table)
        self.button_login.clicked.connect(self.login)
        self.btn_exit.clicked.connect(self.exit)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.label_username)
        layout.addWidget(self.login_edit)
        layout.addWidget(self.label_password)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.button_login)
        layout.addWidget(self.btn_exit)
        
        self.stm.setTable('lg')
        self.stm.select()
        self.table.setModel(self.stm)
        
        query = QSqlQuery()
        sql = "SELECT * FROM public.lg"
        query.exec(sql)
        if query.isActive():
            print("ok")
        else:
            print("no")

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        
    def login(self):
        pass
        
    def exit(self):
        w.close()
        
app = QApplication(sys.argv)
window = LoginWindow()
window.show()
app.exec()