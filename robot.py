import random

import wpilib
import wpilib.drive

from arm import Arm
from drivetrain import Drivetrain
from launcher import Launcher


class Robot(wpilib.TimedRobot):

    time: wpilib.Timer
    drivetrain: Drivetrain
    controller1: wpilib.XboxController
    controller2: wpilib.XboxController
    launcher: Launcher
    arm: Arm

    def robotInit(self):
        self.drivetrain = Drivetrain()
        self.controller1 = wpilib.XboxController(0)
        self.controller2 = wpilib.XboxController(1)
        self.launcher = Launcher()
        self.arm = Arm()
        self.time = wpilib.Timer()
        # wpilib.CameraServer.launch("limelight.py:launch")

    def autonomousInit(self):
        self.time.reset()
        self.time.start()

    def autonomousPeriodic(self):
        if self.time.get() < 1:
            self.launcher.shooter.set(-0.675)
            self.launcher.storage.set(1)
        elif self.time.get() < 2:
            self.launcher.barrel.set(-1)
        elif self.time.get() < 3:
            self.launcher.shooter.set(0)
            self.launcher.barrel.set(0)
            self.launcher.storage.set(1)
            self.launcher.intake.set(1)
            self.drivetrain.drive(-0.35, 0)
        elif self.time.get() < 3.5:
            self.drivetrain.drive(0, 0)
        elif self.time.get() < 4.5:
            self.drivetrain.drive(0.35, 0)
            self.launcher.intake.set(0)
        elif self.time.get() < 5:
            self.launcher.shooter.set(-0.675)
            self.drivetrain.drive(0, 0)
        elif self.time.get() < 6.5:
            self.launcher.barrel.set(-1)
        else:
            self.launcher.shooter.set(0)
            self.launcher.barrel.set(0)
            self.launcher.storage.set(0)

    def autonomousExit(self):
        self.time.stop()

    def teleopInit(self):
        self.time.start()

    def teleopPeriodic(self):
        self.drivetrain.drive(self.controller1.getLeftY(), self.controller1.getLeftX())
        self.launcher.update(self.time.get(), self.controller2)
        self.arm.update(self.controller1)

    def teleopExit(self):
        self.time.stop()


if __name__ == "__main__":
    wpilib.run(Robot)
