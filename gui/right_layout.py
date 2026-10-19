from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget
from pyqtgraph.Qt.QtWidgets import QGridLayout

from gui.components.card import Card
from telemetry import Packet


class RightLayout(QGridLayout):
    def __init__(self, packet: Packet):
        super().__init__()

        self.altitude_card = Card("İrtifa", packet.altitude)
        self.speed_card = Card("Hız", packet.speed)
        self.battery_card = Card("Batarya", packet.battery)

        self.addWidget(self.altitude_card, 0, 0)
        self.addWidget(self.speed_card, 0, 1)
        self.addWidget(self.battery_card, 1, 0)

        self.setRowStretch(2, 1)

    def update_data(self, packet: Packet):
        self.altitude_card.update_data(packet.altitude)
        self.speed_card.update_data(packet.speed)
        self.battery_card.update_data(packet.battery)
