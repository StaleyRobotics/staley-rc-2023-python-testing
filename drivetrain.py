import math

import ctre


class Drivetrain:

    def __init__(self):
        self.front_left = ctre.WPI_TalonFX(1, "rio")
        self.back_left = ctre.WPI_TalonFX(2, "rio")
        self.front_right = ctre.WPI_TalonFX(3, "rio")
        self.back_right = ctre.WPI_TalonFX(4, "rio")

    def drive(self, speed: float, rotation: float):
        speed *= 0.7
        rotation *= 0.5
        self.front_left.set(rotation - speed)
        self.front_right.set(rotation + speed)
        self.back_left.set(rotation - speed)
        self.back_right.set(rotation + speed)
