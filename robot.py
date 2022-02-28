import wpilib
import wpilib.drive

from drivetrain import Drivetrain
from launcher import Launcher


class Robot(wpilib.TimedRobot):
    time: wpilib.Timer
    drivetrain: Drivetrain
    controller: wpilib.XboxController
    launcher: Launcher

    def robotInit(self):
        self.drivetrain = Drivetrain()
        self.controller = wpilib.XboxController(0)
        self.launcher = Launcher()
        self.time = wpilib.Timer()

    def teleopInit(self):
        self.time.start()

    def teleopPeriodic(self):
        self.drivetrain.drive(self.controller.getLeftX(), self.controller.getLeftY())
        self.launcher.update(self.time.get(), self.controller)

    def teleopExit(self):
        self.time.stop()


if __name__ == "__main__":
    wpilib.run(Robot)
