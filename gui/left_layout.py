from PyQt5.QtWidgets import QGridLayout, QLabel


class LeftLayout(QGridLayout):
    def __init__(self):
        super().__init__()

        test_box = QLabel("Sol Panel / Grafikler")
        test_box.setStyleSheet("background-color: #222; color: white;")
        self.addWidget(test_box)
