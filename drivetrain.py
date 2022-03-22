import math

import ctre


class Drivetrain:

    EASE_VALUE = 0.0125
    last_speed = 0

    def __init__(self):
        self.front_left = ctre.WPI_TalonFX(1, "rio")
        self.back_left = ctre.WPI_TalonFX(2, "rio")
        self.front_right = ctre.WPI_TalonFX(3, "rio")
        self.back_right = ctre.WPI_TalonFX(4, "rio")

    def drive(self, speed: float, rotation: float):
        speed *= 0.7
        if speed > self.last_speed + self.EASE_VALUE and self.last_speed < speed:
            speed = self.last_speed + self.EASE_VALUE
        if speed < self.last_speed - self.EASE_VALUE and self.last_speed > speed:
            speed = self.last_speed - self.EASE_VALUE
        self.last_speed = speed
        rotation *= 0.5
        self.front_left.set(rotation - speed)
        self.front_right.set(rotation + speed)
        self.back_left.set(rotation - speed)
        self.back_right.set(rotation + speed)

    def new_drive(self, speed: float, rotation: float):
        speed *= 0.7
        rotation *= 0.5
        self.front_left.set(rotation - speed)
        self.front_right.set(rotation + speed)
        self.back_left.set(rotation - speed)
        self.back_right.set(rotation + speed)