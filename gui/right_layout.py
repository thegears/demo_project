from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget
from pyqtgraph.Qt.QtWidgets import QGridLayout

from gui.components.card import Card
from telemetry import Packet, RedZone


class RightLayout(QGridLayout):
    def __init__(self, packet: Packet, red_zones: list[RedZone]):
        super().__init__()

        self.setContentsMargins(24, 0, 24, 0)
        image = QLabel()
        pixmap = QPixmap("logo.png")
        image.setPixmap(pixmap)
        image.setScaledContents(True)
        image.setFixedSize(200, 200)
        self.addWidget(image, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        self.altitude_card = Card("İrtifa (m)")
        self.speed_card = Card("Hız (m/s)")
        self.battery_card = Card("Batarya (%)")
        self.coordinate_card = Card("Koordinat (x/y)")
        self.check_zone_card = Card("Alanın içinde mi ?")

        self.update_data(packet, red_zones)
        self.setRowStretch(0, 3)

        self.addWidget(self.altitude_card, 1, 0)
        self.addWidget(self.speed_card, 1, 1)
        self.addWidget(self.battery_card, 2, 0)
        self.addWidget(self.coordinate_card, 2, 1)
        self.addWidget(self.check_zone_card, 3, 0, 1, 2)

        self.setRowStretch(4, 1)

    def update_data(self, packet: Packet, red_zones: list[RedZone]):
        self.altitude_card.update_data(f"{packet.altitude:.2f}")
        self.speed_card.update_data(f"{packet.speed:.2f}")
        self.battery_card.update_data(f"{packet.battery:.2f}")
        self.coordinate_card.update_data(f"{packet.x:.2f},{packet.y:.2f}")

        is_inside = False
        for zone in red_zones:
            if zone.check_is_inside(packet.x, packet.y):
                is_inside = True

        self.check_zone_card.setProperty("is_inside", is_inside)
        self.check_zone_card.update_data("EVET" if is_inside else "HAYIR")
