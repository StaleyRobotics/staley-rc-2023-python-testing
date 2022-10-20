import wpilib


class Robot(wpilib.TimedRobot):

    def robotInit(self):
        print("Robot Initialized")

    def autonomousInit(self):
        print("Started Autonomous")

    def autonomousPeriodic(self):
        pass

    def autonomousExit(self):
        print("Exited Autonomous")


if __name__ == "__main__":
    wpilib.run(Robot)
