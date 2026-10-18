import sys
from random import uniform

import numpy as np
import pyqtgraph as pg
from gui.right_layout import RightLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)
from telemetry import Packet, RedZone, Telemetry


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SİHA ARAYÜZ DEMO")
        self.resize(1000, 700)
        self.setStyleSheet("""
            QMainWindow { background-color: #1e1e2e; }
            QLabel { color: #cdd6f4; font-size: 20px; padding: 8px; }
        """)

        self.own_plane = Telemetry()
        self.packet: Packet = self.own_plane.get_packet()

        self.target_planes = [Telemetry() for _ in range(3)]

        self.red_zones = [
            RedZone(
                x=uniform(0, 1000.0), y=uniform(0, 1000.0), radius=uniform(50.0, 120.0)
            )
            for _ in range(3)
        ]

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # TODO: Sol tarafa harita (pg.PlotWidget) ve katman checkbox'larını ekle
        #
        left_layout = QHBoxLayout()

        # TODO: Sağ tarafa dikey panel (QLabel'lar) ekle
        #
        self.right_layout = RightLayout(self.packet)
        self.altitude = QLabel()
        self.speed = QLabel()
        self.battery = QLabel()

        # TODO: Harita üzerine HSS dairesi, iz çizgisi ve İHA noktasını çizip referanslarını tut
        # TODO: Checkbox toggled sinyallerini ilgili çizimlerin setVisible metoduna bağla

        main_layout.addLayout(left_layout, stretch=3)
        main_layout.addLayout(self.right_layout, stretch=1)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000)

    def refresh(self):

        self.own_plane.update()
        self.packet = self.own_plane.get_packet()
        self.right_layout.update_data(self.packet)

        # TODO: Haritadaki iz ve İHA çizimlerinin verisini setData ile güncelle
        # TODO: Sağ paneldeki etiketleri (irtifa, hız, koordinat) f-string ile güncelle
        # TODO: HSS is_inside kontrolü yap ve duruma göre uyarı etiketini güncelle


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = MainWindow()
    pencere.show()
    sys.exit(app.exec_())
