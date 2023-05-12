from PyQt6.QtWidgets import QVBoxLayout, QLabel, QCheckBox, QPushButton, QMessageBox, QDialog

class Test(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" Социальный опрос")
        self.answers = []

        self.question1 = QLabel("Какой ваш возраст?")
        self.answer1_1 = QCheckBox("18 ")
        self.answer1_2 = QCheckBox("30")
        self.answer1_3 = QCheckBox("45")
        self.answer1_4 = QCheckBox("50")

        self.question2 = QLabel("Какой ваш пол?")
        self.answer2_1 = QCheckBox("Мужской")
        self.answer2_2 = QCheckBox("Женский")
        self.answer2_3 = QCheckBox("Другой")

        self.submit_button = QPushButton("Отправить")
        self.submit_button.clicked.connect(self.submit_survey)

        layout = QVBoxLayout()
        layout.addWidget(self.question1)
        layout.addWidget(self.answer1_1)
        layout.addWidget(self.answer1_2)
        layout.addWidget(self.answer1_3)
        layout.addWidget(self.answer1_4)
        layout.addWidget(self.question2)
        layout.addWidget(self.answer2_1)
        layout.addWidget(self.answer2_2)
        layout.addWidget(self.answer2_3)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_survey(self):
        age = []
        if self.answer1_1.isChecked():
            age.append("18")
        if self.answer1_2.isChecked():
            age.append("30")
        if self.answer1_3.isChecked():
            age.append("45")
        if self.answer1_4.isChecked():
            age.append("50")

        gender = []
        if self.answer2_1.isChecked():
            gender.append("Мужской")
        if self.answer2_2.isChecked():
            gender.append("Женский")
        if self.answer2_3.isChecked():
            gender.append("Другой")

        if not age:
            age = "Не выбрано"
        if not gender:
            gender = "Не выбрано"

        QMessageBox.information(self, "Результаты опроса", f"Ваш возраст: {', '.join(age)}\nВаш пол: {', '.join(gender)}")
