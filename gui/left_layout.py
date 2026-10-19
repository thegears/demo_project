import pyqtgraph as pg
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QFont, QPen
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGridLayout, QLabel, QPushButton

from telemetry import Packet, RedZone, Telemetry


class SimulationView(pg.PlotWidget):
    def __init__(self, red_zones: list[RedZone]):
        super().__init__()

        self.setBackground("#18181b")
        self.showGrid(x=True, y=True, alpha=0.15)
        self.setAspectLocked(True)
        self.setMouseEnabled(x=False, y=False)
        self.hideButtons()
        self.view_mode = "follow_plane"
        toggle_view_mode_button = QPushButton("Uçağı takip et", self)
        toggle_view_mode_button.move(self.width(), 20)

        self.setLabel("bottom", "X (m)", color="#94a3b8")
        self.setLabel("left", "Y (m)", color="#94a3b8")

        for zone in red_zones:
            self.draw_red_zone(
                x=zone.x, y=zone.y, radius=zone.radius, color=(239, 68, 68), label="HSS"
            )

        self.draw_planes()

    def draw_red_zone(
        self, x: float, y: float, radius: float, color: tuple[int, int, int], label: str
    ):
        r, g, b = color
        circle = QGraphicsEllipseItem(x - radius, y - radius, 2 * radius, 2 * radius)

        pen = QPen(QColor(r, g, b, 220), 2)
        pen.setStyle(Qt.DashLine)
        circle.setPen(pen)
        circle.setBrush(QBrush(QColor(r, g, b, 35)))

        text = pg.TextItem(text=label, color=(r, g, b, 200), anchor=(0.5, 0.5))
        text.setPos(x, y)
        text.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.addItem(text)

        self.addItem(circle)

    def draw_planes(self):
        self.own_plane = pg.ArrowItem(
            pos=(0, 0),
            angle=0,
            tipAngle=30,
            headLen=20,
            brush="#22c55e",
            pen="#ffffff",
        )
        self.target_planes = [
            pg.ArrowItem(
                pos=(0, 0),
                angle=0,
                tipAngle=30,
                headLen=20,
                brush="#ef4444",
                pen="#ffffff",
            )
            for _ in range(3)
        ]
        for target_plane in self.target_planes:
            self.addItem(target_plane)
        self.addItem(self.own_plane)

    def update_own_plane_data(self, packet: Packet):
        self.own_plane.setPos(packet.x, packet.y)
        self.own_plane.setStyle(angle=90 + packet.heading)
        if self.view_mode == "follow_plane":
            self.setXRange(packet.x - 200, packet.x + 200)
            self.setYRange(packet.y - 200, packet.y + 200)

    def update_target_planes_data(self, target_planes_data: list[Packet]):
        for i, target_plane_data in enumerate(target_planes_data):
            self.target_planes[i].setPos(target_plane_data.x, target_plane_data.y)
            self.target_planes[i].setStyle(angle=90 + target_plane_data.heading)


class LeftLayout(QGridLayout):
    def __init__(self, red_zones: list[RedZone]):
        super().__init__()

        self.simulation = SimulationView(red_zones)

        self.addWidget(self.simulation)

    def update_own_plane_data(self, packet: Packet):
        self.simulation.update_own_plane_data(packet)

    def update_target_planes_data(self, target_planes: list[Packet]):
        self.simulation.update_target_planes_data(target_planes)
