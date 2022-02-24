import wpilib
import ctre

class Robot(wpilib.TimedRobot):

    leftDriveMotor1 = None
    leftDriveMotor2 = None
    rightDriveMotor3 = None
    rightDriveMotor4 = None
    motor5 = None
    motor6 = None
    motor7 = None
    motor8 = None
    controller1 = None

    def robotInit(self):

        self.leftDriveMotor1 = ctre.WPI_TalonFX(1, "rio")
        self.leftDriveMotor2 = ctre.WPI_TalonFX(2, "rio")
        self.rightDriveMotor3 = ctre.WPI_TalonFX(3, "rio")
        self.rightDriveMotor4 = ctre.WPI_TalonFX(4, "rio")

        self.motor5 = ctre.WPI_TalonFX(5, "rio")
        self.motor6 = ctre.WPI_VictorSPX(6)
        self.motor7 = ctre.WPI_VictorSPX(7)
        self.motor8 = ctre.WPI_VictorSPX(8)

        self.controller1 = wpilib.XboxController(0)


        self.components = {
            'motor5': self.motor5,
            'motor6': self.motor6,
            'motor7': self.motor7,
            'motor8': self.motor8,
            'leftDriveMotor1': self.leftDriveMotor1,
            'leftDriveMotor2': self.leftDriveMotor2,
            'rightDriveMotor3': self.rightDriveMotor3,
            'rightDriveMotor4': self.rightDriveMotor4
        }

    def teleopInit(self):
        self.leftDriveMotor1.set(0)
        self.leftDriveMotor2.set(0)
        self.rightDriveMotor3.set(0)
        self.rightDriveMotor4.set(0)
        self.motor5.set(0)
        self.motor6.set(0)
        self.motor7.set(0)
        self.motor8.set(0)
        self.motor5.setInverted(True)
        self.motor6.setInverted(True)


    def teleopPeriodic(self):
        self.leftDriveMotor1.set(self.controller1.getLeftY())
        self.leftDriveMotor2.set(self.controller1.getLeftY())
        self.rightDriveMotor3.set(self.controller1.getRightY())
        self.rightDriveMotor4.set(self.controller1.getRightY())
        self.motor5.set(float(self.controller1.getYButton()) * 0.7)
        self.motor6.set(float(self.controller1.getYButton()) * 1)
        self.motor7.set(float(self.controller1.getRightBumper()) * 1)
        self.motor8.set(float(self.controller1.getRightBumper()) * 1)


if __name__ == '__main__':
    wpilib.run(Robot)
