from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QComboBox, QTextEdit, QMessageBox
from database import insert_feedback

class FeedbackForm(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QFormLayout()

        self.version_input = QLineEdit()
        self.tester_input = QLineEdit()
        self.type_input = QComboBox()
        self.type_input.addItems(["Bug", "Suggestion", "Improvement"])

        self.severity_input = QComboBox()
        self.severity_input.addItems(["Low", "Medium", "High"])

        self.description_input = QTextEdit()
        self.submit_button = QPushButton("Submit Feedback")
        self.submit_button.clicked.connect(self.submit_feedback)

        self.layout.addRow("Game Version:", self.version_input)
        self.layout.addRow("Tester Name:", self.tester_input)
        self.layout.addRow("Feedback Type:", self.type_input)
        self.layout.addRow("Severity:", self.severity_input)
        self.layout.addRow("Description:", self.description_input)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def submit_feedback(self):
        insert_feedback(
            self.version_input.text(),
            self.tester_input.text(),
            self.type_input.currentText(),
            self.severity_input.currentText(),
            self.description_input.toPlainText()
        )
        QMessageBox.information(self, "Success", "Feedback submitted!")
        self.version_input.clear()
        self.tester_input.clear()
        self.description_input.clear()
