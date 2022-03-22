import ctre
import wpilib


class Arm:

    def __init__(self):
        self.arm = ctre.WPI_TalonFX(9)
            # ctre.WPI_TalonFX(10)

    def update(self, controller1: wpilib.XboxController):
        # self.arm[0].set(controller1.getRightY() * -0.2)
        self.arm.set(controller1.getRightY() * -0.2)
