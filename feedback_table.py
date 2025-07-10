from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QMessageBox, QHBoxLayout
)
from database import get_feedback, delete_feedback

class FeedbackTable(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        # Table
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        # Buttons layout
        buttons_layout = QHBoxLayout()

        self.refresh_button = QPushButton("Refresh Table")
        self.refresh_button.clicked.connect(self.load_data)
        buttons_layout.addWidget(self.refresh_button)

        self.delete_button = QPushButton("Delete Selected")
        self.delete_button.clicked.connect(self.delete_selected)
        buttons_layout.addWidget(self.delete_button)

        self.layout.addLayout(buttons_layout)

        self.setLayout(self.layout)
        self.load_data()

    def load_data(self):
        data = get_feedback()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Version", "Tester", "Type", "Severity", "Description"])

        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                self.table.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def delete_selected(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Warning", "Please select a row to delete.")
            return

        feedback_id = self.table.item(selected, 0).text()

        confirm = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Are you sure you want to delete feedback ID {feedback_id}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            delete_feedback(feedback_id)
            QMessageBox.information(self, "Deleted", "Feedback deleted successfully.")
            self.load_data()