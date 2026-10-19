import asyncio
import math
from random import uniform
from time import time

from pydantic import BaseModel


class Packet(BaseModel):
    altitude: float
    speed: float
    heading: float
    x: float
    y: float
    battery: float
    time: float


class RedZone(BaseModel):
    x: float
    y: float
    radius: float

    def check_is_inside(self, target_x: float, target_y: float):
        distance = math.hypot(self.x - target_x, self.y - target_y)
        return distance <= self.radius


class Telemetry:
    def __init__(self) -> None:
        self.packet: Packet = Packet(
            altitude=0,
            speed=0,
            heading=0,
            x=0,
            y=0,
            battery=100.0,
            time=time(),
        )

    def update(self) -> None:
        self.packet.altitude = max(
            100.0, min(150.0, self.packet.altitude + uniform(-0.5, 0.5))
        )

        self.packet.speed = max(10.0, min(20.0, self.packet.speed + uniform(-2.0, 2.0)))

        self.packet.heading = (self.packet.heading + uniform(-10.0, 10.0)) % 360

        rad = math.radians(self.packet.heading)

        self.packet.x += self.packet.speed * math.sin(rad)
        self.packet.y += self.packet.speed * math.cos(rad)

        self.packet.battery -= uniform(0, 0.4)

        self.packet.time = time()

    def get_packet(self) -> Packet:
        return self.packet


### for test


async def test() -> None:
    self_plane = Telemetry()
    red_zone_1 = RedZone(
        x=uniform(0, 1000.0), y=uniform(0, 1000.0), radius=uniform(0, 100.0)
    )
    red_zone_2 = RedZone(
        x=uniform(0, 1000.0), y=uniform(0, 1000.0), radius=uniform(0, 100.0)
    )
    red_zone_3 = RedZone(
        x=uniform(0, 1000.0), y=uniform(0, 1000.0), radius=uniform(0, 100.0)
    )

    for _ in range(10):
        self_plane.update()
        packet = self_plane.get_packet()
        print(packet)

        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(test())
