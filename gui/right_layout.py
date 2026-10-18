from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget
from telemetry import Packet

from gui.components.card import Card


class RightLayout(QVBoxLayout):
    def __init__(self, packet: Packet):
        super().__init__()
        self.altitude_card = Card("İrtifa", packet.altitude)
        self.speed_card = Card("Hız", packet.speed)
        self.battery_card = Card("Batarya", packet.battery)

        self.addWidget(self.altitude_card)
        self.addWidget(self.speed_card)
        self.addWidget(self.battery_card)

    def update_data(self, packet: Packet):
        self.altitude_card.update_data(packet.altitude)
        self.speed_card.update_data(packet.speed)
        self.battery_card.update_data(packet.battery)
