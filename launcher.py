import ctre
import wpilib


class Launcher:

    def __init__(self):
        self.intake_toggle: bool = False
        #self.intake_pressed: bool = False
        self.shooter = ctre.WPI_TalonFX(5, "rio")
        self.barrel = ctre.WPI_VictorSPX(6)
        self.storage = ctre.WPI_VictorSPX(7)
        self.intake = ctre.WPI_VictorSPX(8)

    def update(self, time: float, controller2: wpilib.XboxController):

        # Toggle intake
        if controller2.getRightBumperPressed():
            self.intake_toggle = not self.intake_toggle   #Toggle Right Bumper
        self.intake.set(float(self.intake_toggle))
        self.storage.set(float(self.intake_toggle))

        if controller2.getLeftTrigger() > 0.2:
            self.intake.set(1)

        if controller2.getLeftBumper():
            self.storage.set(1)



        # Set speed for analog launch
        #if controller2.getRightTriggerAxis():
            #self.shooter.set(-controller2.getRightTriggerAxis())

        # Launch
        if controller2.getYButton():
            self.barrel.set(-1)
        else:
            self.barrel.set(0)

        if controller2.getAButton():
            self.shooter.set(-0.7)    #High Shoot
        elif controller2.getBButton():
            self.shooter.set(-0.4)    #Low Shoot
        elif controller2.getRightTriggerAxis():
            self.shooter.set(-controller2.getRightTriggerAxis())  # Analog Shoot
        else:
            self.shooter.set(0)
