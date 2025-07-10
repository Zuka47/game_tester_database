from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtGui import QPainter
from database import get_feedback

class StatsView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.chart = QChart()
        self.series = QPieSeries()

        self.load_data()

        self.chart.setTitle("Feedback Type Distribution")
        self.chart.addSeries(self.series)
        self.chart.legend().setVisible(True)

        chart_view = QChartView(self.chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(chart_view)
        self.setLayout(self.layout)

    def load_data(self):
        feedback = get_feedback()
        type_counts = {}
        for entry in feedback:
            f_type = entry[3]
            type_counts[f_type] = type_counts.get(f_type, 0) + 1

        for t, count in type_counts.items():
            self.series.append(f"{t} ({count})", count)
