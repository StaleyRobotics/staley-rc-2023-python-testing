import ctre
import wpilib


class Arm:

    def __init__(self):
        self.arm = ctre.WPI_TalonFX(9)

    def update(self, controller: wpilib.XboxController):
        self.arm.set(controller.getRightY())
