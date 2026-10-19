from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout


class Card(QFrame):
    def __init__(self, title: str, value: float):
        super().__init__()

        self.setObjectName("card")
        self.setFixedSize(200, 100)

        card_layout = QVBoxLayout(self)
        card_layout.setContentsMargins(0, 0, 0, 0)

        title_label = QLabel(title)
        title_label.setObjectName("title_label")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.value_label = QLabel()
        self.value_label.setObjectName("value_label")
        self.value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.update_data(value)

        card_layout.addWidget(title_label)
        card_layout.addWidget(self.value_label)

    def update_data(self, value: float):
        self.value_label.setText(f"{value:.2f}")
