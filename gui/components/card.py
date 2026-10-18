from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout


class Card(QFrame):
    def __init__(self, title: str, value: float):
        super().__init__()

        card_layout = QVBoxLayout(self)

        title_label = QLabel(title)

        self.value_label = QLabel()

        self.update_data(value)

        card_layout.addWidget(title_label)
        card_layout.addWidget(self.value_label)

    def update_data(self, value: float):
        self.value_label.setText(f"{value:.2f}")
