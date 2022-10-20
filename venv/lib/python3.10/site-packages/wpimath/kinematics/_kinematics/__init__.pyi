from __future__ import annotations
import wpimath.kinematics._kinematics
import typing
import wpimath.geometry._geometry

__all__ = [
    "ChassisSpeeds",
    "DifferentialDriveKinematics",
    "DifferentialDriveOdometry",
    "DifferentialDriveWheelSpeeds",
    "MecanumDriveKinematics",
    "MecanumDriveOdometry",
    "MecanumDriveWheelSpeeds",
    "SwerveDrive2Kinematics",
    "SwerveDrive2Odometry",
    "SwerveDrive3Kinematics",
    "SwerveDrive3Odometry",
    "SwerveDrive4Kinematics",
    "SwerveDrive4Odometry",
    "SwerveDrive6Kinematics",
    "SwerveDrive6Odometry",
    "SwerveModuleState"
]


class ChassisSpeeds():
    """
    Represents the speed of a robot chassis. Although this struct contains
    similar members compared to a Twist2d, they do NOT represent the same thing.
    Whereas a Twist2d represents a change in pose w.r.t to the robot frame of
    reference, this ChassisSpeeds struct represents a velocity w.r.t to the robot
    frame of reference.

    A strictly non-holonomic drivetrain, such as a differential drive, should
    never have a dy component because it can never move sideways. Holonomic
    drivetrains such as swerve and mecanum will often have all three components.
    """
    def __init__(self, vx: meters_per_second = 0, vy: meters_per_second = 0, omega: radians_per_second = 0) -> None: ...
    def __repr__(self) -> str: ...
    @staticmethod
    def fromFeet(vx: feet_per_second = 0, vy: feet_per_second = 0, omega: radians_per_second = 0) -> ChassisSpeeds: ...
    @staticmethod
    def fromFieldRelativeSpeeds(vx: meters_per_second, vy: meters_per_second, omega: radians_per_second, robotAngle: wpimath.geometry._geometry.Rotation2d) -> ChassisSpeeds: 
        """
        Converts a user provided field-relative set of speeds into a robot-relative
        ChassisSpeeds object.

        :param vx:         The component of speed in the x direction relative to the field.
                           Positive x is away from your alliance wall.
        :param vy:         The component of speed in the y direction relative to the field.
                           Positive y is to your left when standing behind the alliance wall.
        :param omega:      The angular rate of the robot.
        :param robotAngle: The angle of the robot as measured by a gyroscope. The
                           robot's angle is considered to be zero when it is facing directly away from
                           your alliance station wall. Remember that this should be CCW positive.

        :returns: ChassisSpeeds object representing the speeds in the robot's frame
                  of reference.
        """
    @property
    def omega(self) -> radians_per_second:
        """
        Represents the angular velocity of the robot frame. (CCW is +)

        :type: radians_per_second
        """
    @omega.setter
    def omega(self, arg0: radians_per_second) -> None:
        """
        Represents the angular velocity of the robot frame. (CCW is +)
        """
    @property
    def omega_dps(self) -> degrees_per_second:
        """
        :type: degrees_per_second
        """
    @omega_dps.setter
    def omega_dps(self, arg1: degrees_per_second) -> None:
        pass
    @property
    def vx(self) -> meters_per_second:
        """
        Represents forward velocity w.r.t the robot frame of reference. (Fwd is +)

        :type: meters_per_second
        """
    @vx.setter
    def vx(self, arg0: meters_per_second) -> None:
        """
        Represents forward velocity w.r.t the robot frame of reference. (Fwd is +)
        """
    @property
    def vx_fps(self) -> feet_per_second:
        """
        :type: feet_per_second
        """
    @vx_fps.setter
    def vx_fps(self, arg1: feet_per_second) -> None:
        pass
    @property
    def vy(self) -> meters_per_second:
        """
        Represents strafe velocity w.r.t the robot frame of reference. (Left is +)

        :type: meters_per_second
        """
    @vy.setter
    def vy(self, arg0: meters_per_second) -> None:
        """
        Represents strafe velocity w.r.t the robot frame of reference. (Left is +)
        """
    @property
    def vy_fps(self) -> feet_per_second:
        """
        :type: feet_per_second
        """
    @vy_fps.setter
    def vy_fps(self, arg1: feet_per_second) -> None:
        pass
    pass
class DifferentialDriveKinematics():
    """
    Helper class that converts a chassis velocity (dx and dtheta components) to
    left and right wheel velocities for a differential drive.

    Inverse kinematics converts a desired chassis speed into left and right
    velocity components whereas forward kinematics converts left and right
    component velocities into a linear and angular chassis speed.
    """
    def __init__(self, trackWidth: meters) -> None: 
        """
        Constructs a differential drive kinematics object.

        :param trackWidth: The track width of the drivetrain. Theoretically, this is
                           the distance between the left wheels and right wheels. However, the
                           empirical value may be larger than the physical measured value due to
                           scrubbing effects.
        """
    def toChassisSpeeds(self, wheelSpeeds: DifferentialDriveWheelSpeeds) -> ChassisSpeeds: 
        """
        Returns a chassis speed from left and right component velocities using
        forward kinematics.

        :param wheelSpeeds: The left and right velocities.

        :returns: The chassis speed.
        """
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds) -> DifferentialDriveWheelSpeeds: 
        """
        Returns left and right component velocities from a chassis speed using
        inverse kinematics.

        :param chassisSpeeds: The linear and angular (dx and dtheta) components that
                              represent the chassis' speed.

        :returns: The left and right velocities.
        """
    @property
    def trackWidth(self) -> meters:
        """
        :type: meters
        """
    pass
class DifferentialDriveOdometry():
    """
    Class for differential drive odometry. Odometry allows you to track the
    robot's position on the field over the course of a match using readings from
    2 encoders and a gyroscope.

    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.

    It is important that you reset your encoders to zero before using this class.
    Any subsequent pose resets also require the encoders to be reset to zero.
    """
    def __init__(self, gyroAngle: wpimath.geometry._geometry.Rotation2d, initialPose: wpimath.geometry._geometry.Pose2d = Pose2d(Translation2d(x=0.000000, y=0.000000), Rotation2d(0.000000))) -> None: 
        """
        Constructs a DifferentialDriveOdometry object.

        :param gyroAngle:   The angle reported by the gyroscope.
        :param initialPose: The starting position of the robot on the field.
        """
    def getPose(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Returns the position of the robot on the field.

        :returns: The pose of the robot.
        """
    def resetPosition(self, pose: wpimath.geometry._geometry.Pose2d, gyroAngle: wpimath.geometry._geometry.Rotation2d) -> None: 
        """
        Resets the robot's position on the field.

        You NEED to reset your encoders (to zero) when calling this method.

        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.

        :param pose:      The position on the field that your robot is at.
        :param gyroAngle: The angle reported by the gyroscope.
        """
    def update(self, gyroAngle: wpimath.geometry._geometry.Rotation2d, leftDistance: meters, rightDistance: meters) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the robot position on the field using distance measurements from
        encoders. This method is more numerically accurate than using velocities to
        integrate the pose and is also advantageous for teams that are using lower
        CPR encoders.

        :param gyroAngle:     The angle reported by the gyroscope.
        :param leftDistance:  The distance traveled by the left encoder.
        :param rightDistance: The distance traveled by the right encoder.

        :returns: The new pose of the robot.
        """
    pass
class DifferentialDriveWheelSpeeds():
    """
    Represents the wheel speeds for a differential drive drivetrain.
    """
    def __init__(self, left: meters_per_second = 0, right: meters_per_second = 0) -> None: ...
    def __repr__(self) -> str: ...
    def desaturate(self, attainableMaxSpeed: meters_per_second) -> None: 
        """
        Renormalizes the wheel speeds if either side is above the specified
        maximum.

        Sometimes, after inverse kinematics, the requested speed from one or more
        wheels may be above the max attainable speed for the driving motor on that
        wheel. To fix this issue, one can reduce all the wheel speeds to make sure
        that all requested module speeds are at-or-below the absolute threshold,
        while maintaining the ratio of speeds between wheels.

        :param attainableMaxSpeed: The absolute max speed that a wheel can reach.
        """
    @staticmethod
    def fromFeet(left: feet_per_second, right: feet_per_second) -> DifferentialDriveWheelSpeeds: ...
    @property
    def left(self) -> meters_per_second:
        """
        Speed of the left side of the robot.

        :type: meters_per_second
        """
    @left.setter
    def left(self, arg0: meters_per_second) -> None:
        """
        Speed of the left side of the robot.
        """
    @property
    def left_fps(self) -> feet_per_second:
        """
        :type: feet_per_second
        """
    @left_fps.setter
    def left_fps(self, arg1: feet_per_second) -> None:
        pass
    @property
    def right(self) -> meters_per_second:
        """
        Speed of the right side of the robot.

        :type: meters_per_second
        """
    @right.setter
    def right(self, arg0: meters_per_second) -> None:
        """
        Speed of the right side of the robot.
        """
    @property
    def right_fps(self) -> feet_per_second:
        """
        :type: feet_per_second
        """
    @right_fps.setter
    def right_fps(self, arg1: feet_per_second) -> None:
        pass
    pass
class MecanumDriveKinematics():
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual wheel speeds.

    The inverse kinematics (converting from a desired chassis velocity to
    individual wheel speeds) uses the relative locations of the wheels with
    respect to the center of rotation. The center of rotation for inverse
    kinematics is also variable. This means that you can set your set your center
    of rotation in a corner of the robot to perform special evasion maneuvers.

    Forward kinematics (converting an array of wheel speeds into the overall
    chassis motion) is performs the exact opposite of what inverse kinematics
    does. Since this is an overdetermined system (more equations than variables),
    we use a least-squares approximation.

    The inverse kinematics: [wheelSpeeds] = [wheelLocations] * [chassisSpeeds]
    We take the Moore-Penrose pseudoinverse of [wheelLocations] and then
    multiply by [wheelSpeeds] to get our chassis speeds.

    Forward kinematics is also used for odometry -- determining the position of
    the robot on the field using encoders and a gyro.
    """
    def __init__(self, frontLeftWheel: wpimath.geometry._geometry.Translation2d, frontRightWheel: wpimath.geometry._geometry.Translation2d, rearLeftWheel: wpimath.geometry._geometry.Translation2d, rearRightWheel: wpimath.geometry._geometry.Translation2d) -> None: 
        """
        Constructs a mecanum drive kinematics object.

        :param frontLeftWheel:  The location of the front-left wheel relative to the
                                physical center of the robot.
        :param frontRightWheel: The location of the front-right wheel relative to
                                the physical center of the robot.
        :param rearLeftWheel:   The location of the rear-left wheel relative to the
                                physical center of the robot.
        :param rearRightWheel:  The location of the rear-right wheel relative to the
                                physical center of the robot.
        """
    def toChassisSpeeds(self, wheelSpeeds: MecanumDriveWheelSpeeds) -> ChassisSpeeds: 
        """
        Performs forward kinematics to return the resulting chassis state from the
        given wheel speeds. This method is often used for odometry -- determining
        the robot's position on the field using data from the real-world speed of
        each wheel on the robot.

        :param wheelSpeeds: The current mecanum drive wheel speeds.

        :returns: The resulting chassis speed.
        """
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds, centerOfRotation: wpimath.geometry._geometry.Translation2d = Translation2d(x=0.000000, y=0.000000)) -> MecanumDriveWheelSpeeds: 
        """
        Performs inverse kinematics to return the wheel speeds from a desired
        chassis velocity. This method is often used to convert joystick values into
        wheel speeds.

        This function also supports variable centers of rotation. During normal
        operations, the center of rotation is usually the same as the physical
        center of the robot; therefore, the argument is defaulted to that use case.
        However, if you wish to change the center of rotation for evasive
        maneuvers, vision alignment, or for any other use case, you can do so.

        :param chassisSpeeds:    The desired chassis speed.
        :param centerOfRotation: The center of rotation. For example, if you set the
                                 center of rotation at one corner of the robot and
                                 provide a chassis speed that only has a dtheta
                                 component, the robot will rotate around that
                                 corner.

        :returns: The wheel speeds. Use caution because they are not normalized.
                  Sometimes, a user input may cause one of the wheel speeds to go
                  above the attainable max velocity. Use the
                  :meth:`MecanumDriveWheelSpeeds.normalize` method to rectify
                  this issue. In addition, you can use Python unpacking syntax
                  to directly assign the wheel speeds to variables::

                    fl, fr, bl, br = kinematics.toWheelSpeeds(chassisSpeeds)
        """
    pass
class MecanumDriveOdometry():
    """
    Class for mecanum drive odometry. Odometry allows you to track the robot's
    position on the field over a course of a match using readings from your
    mecanum wheel encoders.

    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    """
    def __init__(self, kinematics: MecanumDriveKinematics, gyroAngle: wpimath.geometry._geometry.Rotation2d, initialPose: wpimath.geometry._geometry.Pose2d = Pose2d(Translation2d(x=0.000000, y=0.000000), Rotation2d(0.000000))) -> None: 
        """
        Constructs a MecanumDriveOdometry object.

        :param kinematics:  The mecanum drive kinematics for your drivetrain.
        :param gyroAngle:   The angle reported by the gyroscope.
        :param initialPose: The starting position of the robot on the field.
        """
    def getPose(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Returns the position of the robot on the field.

        :returns: The pose of the robot.
        """
    def resetPosition(self, pose: wpimath.geometry._geometry.Pose2d, gyroAngle: wpimath.geometry._geometry.Rotation2d) -> None: 
        """
        Resets the robot's position on the field.

        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.

        :param pose:      The position on the field that your robot is at.
        :param gyroAngle: The angle reported by the gyroscope.
        """
    def update(self, gyroAngle: wpimath.geometry._geometry.Rotation2d, wheelSpeeds: MecanumDriveWheelSpeeds) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method automatically calculates
        the current time to calculate period (difference between two timestamps).
        The period is used to calculate the change in distance from a velocity.
        This also takes in an angle parameter which is used instead of the
        angular rate that is calculated from forward kinematics.

        :param gyroAngle:   The angle reported by the gyroscope.
        :param wheelSpeeds: The current wheel speeds.

        :returns: The new pose of the robot.
        """
    def updateWithTime(self, currentTime: seconds, gyroAngle: wpimath.geometry._geometry.Rotation2d, wheelSpeeds: MecanumDriveWheelSpeeds) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method takes in the current time as
        a parameter to calculate period (difference between two timestamps). The
        period is used to calculate the change in distance from a velocity. This
        also takes in an angle parameter which is used instead of the
        angular rate that is calculated from forward kinematics.

        :param currentTime: The current time.
        :param gyroAngle:   The angle reported by the gyroscope.
        :param wheelSpeeds: The current wheel speeds.

        :returns: The new pose of the robot.
        """
    pass
class MecanumDriveWheelSpeeds():
    """
    Represents the wheel speeds for a mecanum drive drivetrain.
    """
    def __init__(self, frontLeft: meters_per_second = 0, frontRight: meters_per_second = 0, rearLeft: meters_per_second = 0, rearRight: meters_per_second = 0) -> None: ...
    def __repr__(self) -> str: ...
    def desaturate(self, attainableMaxSpeed: meters_per_second) -> None: 
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum.

        Sometimes, after inverse kinematics, the requested speed from one or
        more wheels may be above the max attainable speed for the driving motor on
        that wheel. To fix this issue, one can reduce all the wheel speeds to make
        sure that all requested module speeds are at-or-below the absolute
        threshold, while maintaining the ratio of speeds between wheels.

        :param attainableMaxSpeed: The absolute max speed that a wheel can reach.
        """
    @staticmethod
    def fromFeet(frontLeft: feet_per_second, frontRight: feet_per_second, rearLeft: feet_per_second, rearRight: feet_per_second) -> MecanumDriveWheelSpeeds: ...
    @property
    def frontLeft(self) -> meters_per_second:
        """
        Speed of the front-left wheel.

        :type: meters_per_second
        """
    @frontLeft.setter
    def frontLeft(self, arg0: meters_per_second) -> None:
        """
        Speed of the front-left wheel.
        """
    @property
    def frontLeft_fps(self) -> feet_per_second:
        """
        :type: feet_per_second
        """
    @frontLeft_fps.setter
    def frontLeft_fps(self, arg1: feet_per_second) -> None:
        pass
    @property
    def frontRight(self) -> meters_per_second:
        """
        Speed of the front-right wheel.

        :type: meters_per_second
        """
    @frontRight.setter
    def frontRight(self, arg0: meters_per_second) -> None:
        """
        Speed of the front-right wheel.
        """
    @property
    def frontRight_fps(self) -> feet_per_second:
        """
        :type: feet_per_second
        """
    @frontRight_fps.setter
    def frontRight_fps(self, arg1: feet_per_second) -> None:
        pass
    @property
    def rearLeft(self) -> meters_per_second:
        """
        Speed of the rear-left wheel.

        :type: meters_per_second
        """
    @rearLeft.setter
    def rearLeft(self, arg0: meters_per_second) -> None:
        """
        Speed of the rear-left wheel.
        """
    @property
    def rearLeft_fps(self) -> feet_per_second:
        """
        :type: feet_per_second
        """
    @rearLeft_fps.setter
    def rearLeft_fps(self, arg1: feet_per_second) -> None:
        pass
    @property
    def rearRight(self) -> meters_per_second:
        """
        Speed of the rear-right wheel.

        :type: meters_per_second
        """
    @rearRight.setter
    def rearRight(self, arg0: meters_per_second) -> None:
        """
        Speed of the rear-right wheel.
        """
    @property
    def rearRight_fps(self) -> feet_per_second:
        """
        :type: feet_per_second
        """
    @rearRight_fps.setter
    def rearRight_fps(self, arg1: feet_per_second) -> None:
        pass
    pass
class SwerveDrive2Kinematics():
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual module states (speed and angle).

    The inverse kinematics (converting from a desired chassis velocity to
    individual module states) uses the relative locations of the modules with
    respect to the center of rotation. The center of rotation for inverse
    kinematics is also variable. This means that you can set your set your center
    of rotation in a corner of the robot to perform special evasion maneuvers.

    Forward kinematics (converting an array of module states into the overall
    chassis motion) is performs the exact opposite of what inverse kinematics
    does. Since this is an overdetermined system (more equations than variables),
    we use a least-squares approximation.

    The inverse kinematics: [moduleStates] = [moduleLocations] * [chassisSpeeds]
    We take the Moore-Penrose pseudoinverse of [moduleLocations] and then
    multiply by [moduleStates] to get our chassis speeds.

    Forward kinematics is also used for odometry -- determining the position of
    the robot on the field using encoders and a gyro.
    """
    def __init__(self, arg0: wpimath.geometry._geometry.Translation2d, arg1: wpimath.geometry._geometry.Translation2d) -> None: ...
    @staticmethod
    def desaturateWheelSpeeds(moduleStates: typing.Tuple[SwerveModuleState, SwerveModuleState], attainableMaxSpeed: meters_per_second) -> typing.Tuple[SwerveModuleState, SwerveModuleState]: 
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum.

        Sometimes, after inverse kinematics, the requested speed
        from one or more modules may be above the max attainable speed for the
        driving motor on that module. To fix this issue, one can reduce all the
        wheel speeds to make sure that all requested module speeds are at-or-below
        the absolute threshold, while maintaining the ratio of speeds between
        modules.

        :param moduleStates:       Reference to array of module states. The array will be
                                   mutated with the normalized speeds!
        :param attainableMaxSpeed: The absolute max speed that a module can reach.
        """
    def toChassisSpeeds(self, moduleStates: typing.Tuple[SwerveModuleState, SwerveModuleState]) -> ChassisSpeeds: 
        """
        Performs forward kinematics to return the resulting chassis state from the
        given module states. This method is often used for odometry -- determining
        the robot's position on the field using data from the real-world speed and
        angle of each module on the robot.

        :param moduleStates: The state of the modules as an wpi::array of type
                             SwerveModuleState, NumModules long as measured from respective encoders
                             and gyros. The order of the swerve module states should be same as passed
                             into the constructor of this class.

        :returns: The resulting chassis speed.
        """
    def toSwerveModuleStates(self, chassisSpeeds: ChassisSpeeds, centerOfRotation: wpimath.geometry._geometry.Translation2d = Translation2d(x=0.000000, y=0.000000)) -> typing.Tuple[SwerveModuleState, SwerveModuleState]: 
        """
        Performs inverse kinematics to return the module states from a desired
        chassis velocity. This method is often used to convert joystick values into
        module speeds and angles.

        This function also supports variable centers of rotation. During normal
        operations, the center of rotation is usually the same as the physical
        center of the robot; therefore, the argument is defaulted to that use case.
        However, if you wish to change the center of rotation for evasive
        maneuvers, vision alignment, or for any other use case, you can do so.

        :param chassisSpeeds:    The desired chassis speed.
        :param centerOfRotation: The center of rotation. For example, if you set the
         center of rotation at one corner of the robot and provide a chassis speed
         that only has a dtheta component, the robot will rotate around that corner.

        :returns: An array containing the module states. Use caution because these
                  module states are not normalized. Sometimes, a user input may cause one of
                  the module speeds to go above the attainable max velocity. Use the
                  :meth:`desaturateWheelSpeeds` function to rectify this issue.
                  In addition, you can use Python unpacking syntax
                  to directly assign the module states to variables::

                    fl, fr, bl, br = kinematics.toSwerveModuleStates(chassisSpeeds)
        """
    pass
class SwerveDrive2Odometry():
    """
    Class for swerve drive odometry. Odometry allows you to track the robot's
    position on the field over a course of a match using readings from your
    swerve drive encoders and swerve azimuth encoders.

    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    """
    def __init__(self, kinematics: SwerveDrive2Kinematics, gyroAngle: wpimath.geometry._geometry.Rotation2d, initialPose: wpimath.geometry._geometry.Pose2d = Pose2d(Translation2d(x=0.000000, y=0.000000), Rotation2d(0.000000))) -> None: 
        """
        Constructs a SwerveDriveOdometry object.

        :param kinematics:  The swerve drive kinematics for your drivetrain.
        :param gyroAngle:   The angle reported by the gyroscope.
        :param initialPose: The starting position of the robot on the field.
        """
    def getPose(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Returns the position of the robot on the field.

        :returns: The pose of the robot.
        """
    def resetPosition(self, pose: wpimath.geometry._geometry.Pose2d, gyroAngle: wpimath.geometry._geometry.Rotation2d) -> None: 
        """
        Resets the robot's position on the field.

        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.

        :param pose:      The position on the field that your robot is at.
        :param gyroAngle: The angle reported by the gyroscope.
        """
    def update(self, arg0: wpimath.geometry._geometry.Rotation2d, arg1: SwerveModuleState, arg2: SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method automatically calculates
        the current time to calculate period (difference between two timestamps).
        The period is used to calculate the change in distance from a velocity.
        This also takes in an angle parameter which is used instead of the
        angular rate that is calculated from forward kinematics.

        :param gyroAngle:    The angle reported by the gyroscope.
        :param moduleStates: The current state of all swerve modules. Please provide
                             the states in the same order in which you instantiated
                             your SwerveDriveKinematics.

        :returns: The new pose of the robot.
        """
    def updateWithTime(self, arg0: seconds, arg1: wpimath.geometry._geometry.Rotation2d, arg2: SwerveModuleState, arg3: SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method takes in the current time as
        a parameter to calculate period (difference between two timestamps). The
        period is used to calculate the change in distance from a velocity. This
        also takes in an angle parameter which is used instead of the
        angular rate that is calculated from forward kinematics.

        :param currentTime:  The current time.
        :param gyroAngle:    The angle reported by the gyroscope.
        :param moduleStates: The current state of all swerve modules. Please provide
                             the states in the same order in which you instantiated
                             your SwerveDriveKinematics.

        :returns: The new pose of the robot.
        """
    pass
class SwerveDrive3Kinematics():
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual module states (speed and angle).

    The inverse kinematics (converting from a desired chassis velocity to
    individual module states) uses the relative locations of the modules with
    respect to the center of rotation. The center of rotation for inverse
    kinematics is also variable. This means that you can set your set your center
    of rotation in a corner of the robot to perform special evasion maneuvers.

    Forward kinematics (converting an array of module states into the overall
    chassis motion) is performs the exact opposite of what inverse kinematics
    does. Since this is an overdetermined system (more equations than variables),
    we use a least-squares approximation.

    The inverse kinematics: [moduleStates] = [moduleLocations] * [chassisSpeeds]
    We take the Moore-Penrose pseudoinverse of [moduleLocations] and then
    multiply by [moduleStates] to get our chassis speeds.

    Forward kinematics is also used for odometry -- determining the position of
    the robot on the field using encoders and a gyro.
    """
    def __init__(self, arg0: wpimath.geometry._geometry.Translation2d, arg1: wpimath.geometry._geometry.Translation2d, arg2: wpimath.geometry._geometry.Translation2d) -> None: ...
    @staticmethod
    def desaturateWheelSpeeds(moduleStates: typing.Tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState], attainableMaxSpeed: meters_per_second) -> typing.Tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState]: 
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum.

        Sometimes, after inverse kinematics, the requested speed
        from one or more modules may be above the max attainable speed for the
        driving motor on that module. To fix this issue, one can reduce all the
        wheel speeds to make sure that all requested module speeds are at-or-below
        the absolute threshold, while maintaining the ratio of speeds between
        modules.

        :param moduleStates:       Reference to array of module states. The array will be
                                   mutated with the normalized speeds!
        :param attainableMaxSpeed: The absolute max speed that a module can reach.
        """
    def toChassisSpeeds(self, moduleStates: typing.Tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState]) -> ChassisSpeeds: 
        """
        Performs forward kinematics to return the resulting chassis state from the
        given module states. This method is often used for odometry -- determining
        the robot's position on the field using data from the real-world speed and
        angle of each module on the robot.

        :param moduleStates: The state of the modules as an wpi::array of type
                             SwerveModuleState, NumModules long as measured from respective encoders
                             and gyros. The order of the swerve module states should be same as passed
                             into the constructor of this class.

        :returns: The resulting chassis speed.
        """
    def toSwerveModuleStates(self, chassisSpeeds: ChassisSpeeds, centerOfRotation: wpimath.geometry._geometry.Translation2d = Translation2d(x=0.000000, y=0.000000)) -> typing.Tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState]: 
        """
        Performs inverse kinematics to return the module states from a desired
        chassis velocity. This method is often used to convert joystick values into
        module speeds and angles.

        This function also supports variable centers of rotation. During normal
        operations, the center of rotation is usually the same as the physical
        center of the robot; therefore, the argument is defaulted to that use case.
        However, if you wish to change the center of rotation for evasive
        maneuvers, vision alignment, or for any other use case, you can do so.

        :param chassisSpeeds:    The desired chassis speed.
        :param centerOfRotation: The center of rotation. For example, if you set the
         center of rotation at one corner of the robot and provide a chassis speed
         that only has a dtheta component, the robot will rotate around that corner.

        :returns: An array containing the module states. Use caution because these
                  module states are not normalized. Sometimes, a user input may cause one of
                  the module speeds to go above the attainable max velocity. Use the
                  :meth:`desaturateWheelSpeeds` function to rectify this issue.
                  In addition, you can use Python unpacking syntax
                  to directly assign the module states to variables::

                    fl, fr, bl, br = kinematics.toSwerveModuleStates(chassisSpeeds)
        """
    pass
class SwerveDrive3Odometry():
    """
    Class for swerve drive odometry. Odometry allows you to track the robot's
    position on the field over a course of a match using readings from your
    swerve drive encoders and swerve azimuth encoders.

    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    """
    def __init__(self, kinematics: SwerveDrive3Kinematics, gyroAngle: wpimath.geometry._geometry.Rotation2d, initialPose: wpimath.geometry._geometry.Pose2d = Pose2d(Translation2d(x=0.000000, y=0.000000), Rotation2d(0.000000))) -> None: 
        """
        Constructs a SwerveDriveOdometry object.

        :param kinematics:  The swerve drive kinematics for your drivetrain.
        :param gyroAngle:   The angle reported by the gyroscope.
        :param initialPose: The starting position of the robot on the field.
        """
    def getPose(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Returns the position of the robot on the field.

        :returns: The pose of the robot.
        """
    def resetPosition(self, pose: wpimath.geometry._geometry.Pose2d, gyroAngle: wpimath.geometry._geometry.Rotation2d) -> None: 
        """
        Resets the robot's position on the field.

        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.

        :param pose:      The position on the field that your robot is at.
        :param gyroAngle: The angle reported by the gyroscope.
        """
    def update(self, arg0: wpimath.geometry._geometry.Rotation2d, arg1: SwerveModuleState, arg2: SwerveModuleState, arg3: SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method automatically calculates
        the current time to calculate period (difference between two timestamps).
        The period is used to calculate the change in distance from a velocity.
        This also takes in an angle parameter which is used instead of the
        angular rate that is calculated from forward kinematics.

        :param gyroAngle:    The angle reported by the gyroscope.
        :param moduleStates: The current state of all swerve modules. Please provide
                             the states in the same order in which you instantiated
                             your SwerveDriveKinematics.

        :returns: The new pose of the robot.
        """
    def updateWithTime(self, arg0: seconds, arg1: wpimath.geometry._geometry.Rotation2d, arg2: SwerveModuleState, arg3: SwerveModuleState, arg4: SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method takes in the current time as
        a parameter to calculate period (difference between two timestamps). The
        period is used to calculate the change in distance from a velocity. This
        also takes in an angle parameter which is used instead of the
        angular rate that is calculated from forward kinematics.

        :param currentTime:  The current time.
        :param gyroAngle:    The angle reported by the gyroscope.
        :param moduleStates: The current state of all swerve modules. Please provide
                             the states in the same order in which you instantiated
                             your SwerveDriveKinematics.

        :returns: The new pose of the robot.
        """
    pass
class SwerveDrive4Kinematics():
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual module states (speed and angle).

    The inverse kinematics (converting from a desired chassis velocity to
    individual module states) uses the relative locations of the modules with
    respect to the center of rotation. The center of rotation for inverse
    kinematics is also variable. This means that you can set your set your center
    of rotation in a corner of the robot to perform special evasion maneuvers.

    Forward kinematics (converting an array of module states into the overall
    chassis motion) is performs the exact opposite of what inverse kinematics
    does. Since this is an overdetermined system (more equations than variables),
    we use a least-squares approximation.

    The inverse kinematics: [moduleStates] = [moduleLocations] * [chassisSpeeds]
    We take the Moore-Penrose pseudoinverse of [moduleLocations] and then
    multiply by [moduleStates] to get our chassis speeds.

    Forward kinematics is also used for odometry -- determining the position of
    the robot on the field using encoders and a gyro.
    """
    def __init__(self, arg0: wpimath.geometry._geometry.Translation2d, arg1: wpimath.geometry._geometry.Translation2d, arg2: wpimath.geometry._geometry.Translation2d, arg3: wpimath.geometry._geometry.Translation2d) -> None: ...
    @staticmethod
    def desaturateWheelSpeeds(moduleStates: typing.Tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState], attainableMaxSpeed: meters_per_second) -> typing.Tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]: 
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum.

        Sometimes, after inverse kinematics, the requested speed
        from one or more modules may be above the max attainable speed for the
        driving motor on that module. To fix this issue, one can reduce all the
        wheel speeds to make sure that all requested module speeds are at-or-below
        the absolute threshold, while maintaining the ratio of speeds between
        modules.

        :param moduleStates:       Reference to array of module states. The array will be
                                   mutated with the normalized speeds!
        :param attainableMaxSpeed: The absolute max speed that a module can reach.
        """
    def toChassisSpeeds(self, moduleStates: typing.Tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]) -> ChassisSpeeds: 
        """
        Performs forward kinematics to return the resulting chassis state from the
        given module states. This method is often used for odometry -- determining
        the robot's position on the field using data from the real-world speed and
        angle of each module on the robot.

        :param moduleStates: The state of the modules as an wpi::array of type
                             SwerveModuleState, NumModules long as measured from respective encoders
                             and gyros. The order of the swerve module states should be same as passed
                             into the constructor of this class.

        :returns: The resulting chassis speed.
        """
    def toSwerveModuleStates(self, chassisSpeeds: ChassisSpeeds, centerOfRotation: wpimath.geometry._geometry.Translation2d = Translation2d(x=0.000000, y=0.000000)) -> typing.Tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]: 
        """
        Performs inverse kinematics to return the module states from a desired
        chassis velocity. This method is often used to convert joystick values into
        module speeds and angles.

        This function also supports variable centers of rotation. During normal
        operations, the center of rotation is usually the same as the physical
        center of the robot; therefore, the argument is defaulted to that use case.
        However, if you wish to change the center of rotation for evasive
        maneuvers, vision alignment, or for any other use case, you can do so.

        :param chassisSpeeds:    The desired chassis speed.
        :param centerOfRotation: The center of rotation. For example, if you set the
         center of rotation at one corner of the robot and provide a chassis speed
         that only has a dtheta component, the robot will rotate around that corner.

        :returns: An array containing the module states. Use caution because these
                  module states are not normalized. Sometimes, a user input may cause one of
                  the module speeds to go above the attainable max velocity. Use the
                  :meth:`desaturateWheelSpeeds` function to rectify this issue.
                  In addition, you can use Python unpacking syntax
                  to directly assign the module states to variables::

                    fl, fr, bl, br = kinematics.toSwerveModuleStates(chassisSpeeds)
        """
    pass
class SwerveDrive4Odometry():
    """
    Class for swerve drive odometry. Odometry allows you to track the robot's
    position on the field over a course of a match using readings from your
    swerve drive encoders and swerve azimuth encoders.

    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    """
    def __init__(self, kinematics: SwerveDrive4Kinematics, gyroAngle: wpimath.geometry._geometry.Rotation2d, initialPose: wpimath.geometry._geometry.Pose2d = Pose2d(Translation2d(x=0.000000, y=0.000000), Rotation2d(0.000000))) -> None: 
        """
        Constructs a SwerveDriveOdometry object.

        :param kinematics:  The swerve drive kinematics for your drivetrain.
        :param gyroAngle:   The angle reported by the gyroscope.
        :param initialPose: The starting position of the robot on the field.
        """
    def getPose(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Returns the position of the robot on the field.

        :returns: The pose of the robot.
        """
    def resetPosition(self, pose: wpimath.geometry._geometry.Pose2d, gyroAngle: wpimath.geometry._geometry.Rotation2d) -> None: 
        """
        Resets the robot's position on the field.

        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.

        :param pose:      The position on the field that your robot is at.
        :param gyroAngle: The angle reported by the gyroscope.
        """
    def update(self, arg0: wpimath.geometry._geometry.Rotation2d, arg1: SwerveModuleState, arg2: SwerveModuleState, arg3: SwerveModuleState, arg4: SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method automatically calculates
        the current time to calculate period (difference between two timestamps).
        The period is used to calculate the change in distance from a velocity.
        This also takes in an angle parameter which is used instead of the
        angular rate that is calculated from forward kinematics.

        :param gyroAngle:    The angle reported by the gyroscope.
        :param moduleStates: The current state of all swerve modules. Please provide
                             the states in the same order in which you instantiated
                             your SwerveDriveKinematics.

        :returns: The new pose of the robot.
        """
    def updateWithTime(self, arg0: seconds, arg1: wpimath.geometry._geometry.Rotation2d, arg2: SwerveModuleState, arg3: SwerveModuleState, arg4: SwerveModuleState, arg5: SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method takes in the current time as
        a parameter to calculate period (difference between two timestamps). The
        period is used to calculate the change in distance from a velocity. This
        also takes in an angle parameter which is used instead of the
        angular rate that is calculated from forward kinematics.

        :param currentTime:  The current time.
        :param gyroAngle:    The angle reported by the gyroscope.
        :param moduleStates: The current state of all swerve modules. Please provide
                             the states in the same order in which you instantiated
                             your SwerveDriveKinematics.

        :returns: The new pose of the robot.
        """
    pass
class SwerveDrive6Kinematics():
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual module states (speed and angle).

    The inverse kinematics (converting from a desired chassis velocity to
    individual module states) uses the relative locations of the modules with
    respect to the center of rotation. The center of rotation for inverse
    kinematics is also variable. This means that you can set your set your center
    of rotation in a corner of the robot to perform special evasion maneuvers.

    Forward kinematics (converting an array of module states into the overall
    chassis motion) is performs the exact opposite of what inverse kinematics
    does. Since this is an overdetermined system (more equations than variables),
    we use a least-squares approximation.

    The inverse kinematics: [moduleStates] = [moduleLocations] * [chassisSpeeds]
    We take the Moore-Penrose pseudoinverse of [moduleLocations] and then
    multiply by [moduleStates] to get our chassis speeds.

    Forward kinematics is also used for odometry -- determining the position of
    the robot on the field using encoders and a gyro.
    """
    def __init__(self, arg0: wpimath.geometry._geometry.Translation2d, arg1: wpimath.geometry._geometry.Translation2d, arg2: wpimath.geometry._geometry.Translation2d, arg3: wpimath.geometry._geometry.Translation2d, arg4: wpimath.geometry._geometry.Translation2d, arg5: wpimath.geometry._geometry.Translation2d) -> None: ...
    @staticmethod
    def desaturateWheelSpeeds(moduleStates: typing.Tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState], attainableMaxSpeed: meters_per_second) -> typing.Tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]: 
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum.

        Sometimes, after inverse kinematics, the requested speed
        from one or more modules may be above the max attainable speed for the
        driving motor on that module. To fix this issue, one can reduce all the
        wheel speeds to make sure that all requested module speeds are at-or-below
        the absolute threshold, while maintaining the ratio of speeds between
        modules.

        :param moduleStates:       Reference to array of module states. The array will be
                                   mutated with the normalized speeds!
        :param attainableMaxSpeed: The absolute max speed that a module can reach.
        """
    def toChassisSpeeds(self, moduleStates: typing.Tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]) -> ChassisSpeeds: 
        """
        Performs forward kinematics to return the resulting chassis state from the
        given module states. This method is often used for odometry -- determining
        the robot's position on the field using data from the real-world speed and
        angle of each module on the robot.

        :param moduleStates: The state of the modules as an wpi::array of type
                             SwerveModuleState, NumModules long as measured from respective encoders
                             and gyros. The order of the swerve module states should be same as passed
                             into the constructor of this class.

        :returns: The resulting chassis speed.
        """
    def toSwerveModuleStates(self, chassisSpeeds: ChassisSpeeds, centerOfRotation: wpimath.geometry._geometry.Translation2d = Translation2d(x=0.000000, y=0.000000)) -> typing.Tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]: 
        """
        Performs inverse kinematics to return the module states from a desired
        chassis velocity. This method is often used to convert joystick values into
        module speeds and angles.

        This function also supports variable centers of rotation. During normal
        operations, the center of rotation is usually the same as the physical
        center of the robot; therefore, the argument is defaulted to that use case.
        However, if you wish to change the center of rotation for evasive
        maneuvers, vision alignment, or for any other use case, you can do so.

        :param chassisSpeeds:    The desired chassis speed.
        :param centerOfRotation: The center of rotation. For example, if you set the
         center of rotation at one corner of the robot and provide a chassis speed
         that only has a dtheta component, the robot will rotate around that corner.

        :returns: An array containing the module states. Use caution because these
                  module states are not normalized. Sometimes, a user input may cause one of
                  the module speeds to go above the attainable max velocity. Use the
                  :meth:`desaturateWheelSpeeds` function to rectify this issue.
                  In addition, you can use Python unpacking syntax
                  to directly assign the module states to variables::

                    fl, fr, bl, br = kinematics.toSwerveModuleStates(chassisSpeeds)
        """
    pass
class SwerveDrive6Odometry():
    """
    Class for swerve drive odometry. Odometry allows you to track the robot's
    position on the field over a course of a match using readings from your
    swerve drive encoders and swerve azimuth encoders.

    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    """
    def __init__(self, kinematics: SwerveDrive6Kinematics, gyroAngle: wpimath.geometry._geometry.Rotation2d, initialPose: wpimath.geometry._geometry.Pose2d = Pose2d(Translation2d(x=0.000000, y=0.000000), Rotation2d(0.000000))) -> None: 
        """
        Constructs a SwerveDriveOdometry object.

        :param kinematics:  The swerve drive kinematics for your drivetrain.
        :param gyroAngle:   The angle reported by the gyroscope.
        :param initialPose: The starting position of the robot on the field.
        """
    def getPose(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Returns the position of the robot on the field.

        :returns: The pose of the robot.
        """
    def resetPosition(self, pose: wpimath.geometry._geometry.Pose2d, gyroAngle: wpimath.geometry._geometry.Rotation2d) -> None: 
        """
        Resets the robot's position on the field.

        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.

        :param pose:      The position on the field that your robot is at.
        :param gyroAngle: The angle reported by the gyroscope.
        """
    def update(self, arg0: wpimath.geometry._geometry.Rotation2d, arg1: SwerveModuleState, arg2: SwerveModuleState, arg3: SwerveModuleState, arg4: SwerveModuleState, arg5: SwerveModuleState, arg6: SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method automatically calculates
        the current time to calculate period (difference between two timestamps).
        The period is used to calculate the change in distance from a velocity.
        This also takes in an angle parameter which is used instead of the
        angular rate that is calculated from forward kinematics.

        :param gyroAngle:    The angle reported by the gyroscope.
        :param moduleStates: The current state of all swerve modules. Please provide
                             the states in the same order in which you instantiated
                             your SwerveDriveKinematics.

        :returns: The new pose of the robot.
        """
    def updateWithTime(self, arg0: seconds, arg1: wpimath.geometry._geometry.Rotation2d, arg2: SwerveModuleState, arg3: SwerveModuleState, arg4: SwerveModuleState, arg5: SwerveModuleState, arg6: SwerveModuleState, arg7: SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method takes in the current time as
        a parameter to calculate period (difference between two timestamps). The
        period is used to calculate the change in distance from a velocity. This
        also takes in an angle parameter which is used instead of the
        angular rate that is calculated from forward kinematics.

        :param currentTime:  The current time.
        :param gyroAngle:    The angle reported by the gyroscope.
        :param moduleStates: The current state of all swerve modules. Please provide
                             the states in the same order in which you instantiated
                             your SwerveDriveKinematics.

        :returns: The new pose of the robot.
        """
    pass
class SwerveModuleState():
    """
    Represents the state of one swerve module.
    """
    def __init__(self, speed: meters_per_second = 0, angle: wpimath.geometry._geometry.Rotation2d = Rotation2d(0.000000)) -> None: ...
    def __repr__(self) -> str: ...
    @staticmethod
    def optimize(desiredState: SwerveModuleState, currentAngle: wpimath.geometry._geometry.Rotation2d) -> SwerveModuleState: 
        """
        Minimize the change in heading the desired swerve module state would
        require by potentially reversing the direction the wheel spins. If this is
        used with the PIDController class's continuous input functionality, the
        furthest a wheel will ever rotate is 90 degrees.

        :param desiredState: The desired state.
        :param currentAngle: The current module angle.
        """
    @property
    def angle(self) -> wpimath.geometry._geometry.Rotation2d:
        """
        Angle of the module.

        :type: wpimath.geometry._geometry.Rotation2d
        """
    @angle.setter
    def angle(self, arg0: wpimath.geometry._geometry.Rotation2d) -> None:
        """
        Angle of the module.
        """
    @property
    def speed(self) -> meters_per_second:
        """
        Speed of the wheel of the module.

        :type: meters_per_second
        """
    @speed.setter
    def speed(self, arg0: meters_per_second) -> None:
        """
        Speed of the wheel of the module.
        """
    @property
    def speed_fps(self) -> feet_per_second:
        """
        :type: feet_per_second
        """
    @speed_fps.setter
    def speed_fps(self, arg1: feet_per_second) -> None:
        pass
    pass
