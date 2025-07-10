from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout
import sys
from feedback_form import FeedbackForm
from feedback_table import FeedbackTable
from stats_view import StatsView
from database import init_db

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Testing Feedback Collector")
        self.setGeometry(100, 100, 800, 600)

        tabs = QTabWidget()
        tabs.addTab(FeedbackForm(), "Add Feedback")
        tabs.addTab(FeedbackTable(), "View Feedback")
        tabs.addTab(StatsView(), "Feedback Stats")

        self.setCentralWidget(tabs)

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
