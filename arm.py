import ctre
import wpilib


class Arm:

    def __init__(self):
        self.arm = ctre.WPI_TalonFX(9)

    def update(self, controller1: wpilib.XboxController):
        self.arm.set(controller1.getRightY()*-0.2)
