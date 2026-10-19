import sys
from pathlib import Path
from random import uniform

import qdarktheme
from PyQt5.QtCore import QFileSystemWatcher, QTimer
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QWidget,
)

from gui.left_layout import LeftLayout
from gui.right_layout import RightLayout
from telemetry import Packet, RedZone, Telemetry


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SİHA ARAYÜZ DEMO")
        self.setFixedSize(1200, 700)

        self.own_plane = Telemetry()
        self.packet: Packet = self.own_plane.get_packet()

        self.target_planes = [Telemetry() for _ in range(3)]

        self.red_zones = [
            RedZone(
                x=uniform(120.0, 250.0),
                y=uniform(120.0, 880.0),
                radius=uniform(50.0, 100.0),
            ),
            RedZone(
                x=uniform(450.0, 580.0),
                y=uniform(120.0, 880.0),
                radius=uniform(50.0, 100.0),
            ),
            RedZone(
                x=uniform(780.0, 900.0),
                y=uniform(120.0, 880.0),
                radius=uniform(50.0, 100.0),
            ),
        ]

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        
        self.left_layout = LeftLayout(self.red_zones)

        
        self.right_layout = RightLayout(self.packet, self.red_zones)
        self.altitude = QLabel()
        self.speed = QLabel()
        self.battery = QLabel()


        main_layout.addLayout(self.left_layout, 3)
        main_layout.addLayout(self.right_layout, 1)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000)

    def refresh(self):

        self.own_plane.update()
        for target_plane in self.target_planes:
            target_plane.update()
        self.packet = self.own_plane.get_packet()

        self.right_layout.update_data(self.packet, self.red_zones)

        self.left_layout.update_own_plane_data(self.packet)
        self.left_layout.update_target_planes_data(
            [target_plane.get_packet() for target_plane in self.target_planes]
        )



# def hot_reload(app, path="style.css"):
#     style_path = Path(__file__).with_name(path)
#     style = style_path.read_text(encoding="utf-8")
#     qdarktheme.setup_theme("dark", additional_qss=style)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    style_path = Path(__file__).with_name("style.css")
    style = style_path.read_text(encoding="utf-8")
    qdarktheme.setup_theme("dark", additional_qss=style)

    # watcher = QFileSystemWatcher(["style.css"])
    # watcher.fileChanged.connect(lambda: hot_reload(app))

    pencere = MainWindow()
    pencere.show()
    sys.exit(app.exec_())
