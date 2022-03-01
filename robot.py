import random

import wpilib
import wpilib.drive

from arm import Arm
from drivetrain import Drivetrain
from launcher import Launcher


class Robot(wpilib.TimedRobot):

    time: wpilib.Timer
    drivetrain: Drivetrain
    controller: wpilib.XboxController
    launcher: Launcher
    arm: Arm
    rot: float

    def robotInit(self):
        self.drivetrain = Drivetrain()
        self.controller = wpilib.XboxController(0)
        self.launcher = Launcher()
        self.arm = Arm()
        self.time = wpilib.Timer()
        self.rot = 0

    def teleopInit(self):
        self.time.start()

    def teleopPeriodic(self):
        self.drivetrain.drive(self.controller.getLeftY(), self.controller.getLeftX())
        self.launcher.update(self.time.get(), self.controller)
        self.arm.update(self.controller)

    def teleopExit(self):
        self.time.stop()

    def autonomousInit(self):
        self.time.start()

    def autonomousPeriodic(self):
        self.rot += random.randint(-2, 2) / 100
        if self.rot > 1.0:
            self.rot = 1.0
        if self.rot < -1.0:
            self.rot = -1.0
        self.drivetrain.drive(0.5, self.rot)

    def autonomousExit(self):
        self.time.stop()

if __name__ == "__main__":
    wpilib.run(Robot)
