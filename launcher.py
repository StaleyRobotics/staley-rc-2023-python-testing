import ctre
import wpilib


class Launcher:

    def __init__(self):
        self.intake_toggle: bool = False
        self.shooter = ctre.WPI_TalonFX(5, "rio")
        self.barrel = ctre.WPI_VictorSPX(6)
        self.storage = ctre.WPI_VictorSPX(7)
        self.intake = ctre.WPI_VictorSPX(8)

    def update(self, time: float, controller: wpilib.XboxController):
        if controller.getRightBumper():
            self.intake_toggle = not self.intake_toggle
        self.intake.set(float(self.intake_toggle))
        self.storage.set(float(self.intake_toggle))
        self.shooter.set(controller.getRightTriggerAxis())
        if controller.getYButton():
            self.barrel.set(0.5)
        else:
            self.barrel.set(0.5)
