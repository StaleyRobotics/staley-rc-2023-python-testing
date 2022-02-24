import wpilib
#from wpilib.drive import DifferentialDrive
#import wpilib.drive
import ctre
#from robotpy_ext.autonomous import AutonomousModeSelector

class MyRobot(wpilib.TimedRobot):

    motor1 = None
    controller1 = None

    def robotInit(self):
        self.motor1 = ctre.WPI_TalonFX(9, "rio")
        self.controller1 = wpilib.XboxController(0)

        self.components = {
            'motor1': self.motor1,
        }

        #self.automodes = AutonomousModeSelector('autonomous', self.components)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        self.automodes.run()

    def teleopInit(self):
        self.motor1.set(0)

    def teleopPeriodic(self):
        self.motor1.set(self.controller1.getLeftY())


if __name__ == '__main__':
    wpilib.run(MyRobot)
