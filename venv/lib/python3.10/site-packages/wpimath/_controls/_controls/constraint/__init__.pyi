from __future__ import annotations
import wpimath._controls._controls.constraint
import typing
import wpimath._controls._controls.controller
import wpimath.geometry._geometry
import wpimath.kinematics._kinematics

__all__ = [
    "CentripetalAccelerationConstraint",
    "DifferentialDriveKinematicsConstraint",
    "DifferentialDriveVoltageConstraint",
    "EllipticalRegionConstraint",
    "MaxVelocityConstraint",
    "MecanumDriveKinematicsConstraint",
    "RectangularRegionConstraint",
    "SwerveDrive2KinematicsConstraint",
    "SwerveDrive3KinematicsConstraint",
    "SwerveDrive4KinematicsConstraint",
    "SwerveDrive6KinematicsConstraint",
    "TrajectoryConstraint"
]


class TrajectoryConstraint():
    """
    An interface for defining user-defined velocity and acceleration constraints
    while generating trajectories.
    """
    class MinMax():
        """
        Represents a minimum and maximum acceleration.
        """
        def __init__(self) -> None: ...
        @property
        def maxAcceleration(self) -> meters_per_second_squared:
            """
            :type: meters_per_second_squared
            """
        @maxAcceleration.setter
        def maxAcceleration(self, arg0: meters_per_second_squared) -> None:
            pass
        @property
        def minAcceleration(self) -> meters_per_second_squared:
            """
            :type: meters_per_second_squared
            """
        @minAcceleration.setter
        def minAcceleration(self, arg0: meters_per_second_squared) -> None:
            pass
        pass
    def __init__(self) -> None: ...
    def maxVelocity(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, velocity: meters_per_second) -> meters_per_second: 
        """
        Returns the max velocity given the current pose and curvature.

        :param pose:      The pose at the current point in the trajectory.
        :param curvature: The curvature at the current point in the trajectory.
        :param velocity:  The velocity at the current point in the trajectory before
                          constraints are applied.

        :returns: The absolute maximum velocity.
        """
    def minMaxAcceleration(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, speed: meters_per_second) -> TrajectoryConstraint.MinMax: 
        """
        Returns the minimum and maximum allowable acceleration for the trajectory
        given pose, curvature, and speed.

        :param pose:      The pose at the current point in the trajectory.
        :param curvature: The curvature at the current point in the trajectory.
        :param speed:     The speed at the current point in the trajectory.

        :returns: The min and max acceleration bounds.
        """
    pass
class DifferentialDriveKinematicsConstraint(TrajectoryConstraint):
    """
    A class that enforces constraints on the differential drive kinematics.
    This can be used to ensure that the trajectory is constructed so that the
    commanded velocities for both sides of the drivetrain stay below a certain
    limit.
    """
    def __init__(self, kinematics: wpimath.kinematics._kinematics.DifferentialDriveKinematics, maxSpeed: meters_per_second) -> None: ...
    @staticmethod
    def fromFps(kinematics: wpimath.kinematics._kinematics.DifferentialDriveKinematics, maxSpeed: feet_per_second) -> DifferentialDriveKinematicsConstraint: ...
    def maxVelocity(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, velocity: meters_per_second) -> meters_per_second: ...
    def minMaxAcceleration(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, speed: meters_per_second) -> TrajectoryConstraint.MinMax: ...
    pass
class DifferentialDriveVoltageConstraint(TrajectoryConstraint):
    """
    A class that enforces constraints on differential drive voltage expenditure
    based on the motor dynamics and the drive kinematics.  Ensures that the
    acceleration of any wheel of the robot while following the trajectory is
    never higher than what can be achieved with the given maximum voltage.
    """
    def __init__(self, feedforward: wpimath._controls._controls.controller.SimpleMotorFeedforwardMeters, kinematics: wpimath.kinematics._kinematics.DifferentialDriveKinematics, maxVoltage: volts) -> None: 
        """
        Creates a new DifferentialDriveVoltageConstraint.

        :param feedforward: A feedforward component describing the behavior of the
                            drive.
        :param kinematics:  A kinematics component describing the drive geometry.
        :param maxVoltage:  The maximum voltage available to the motors while
                            following the path. Should be somewhat less than the nominal battery
                            voltage (12V) to account for "voltage sag" due to current draw.
        """
    def maxVelocity(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, velocity: meters_per_second) -> meters_per_second: ...
    def minMaxAcceleration(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, speed: meters_per_second) -> TrajectoryConstraint.MinMax: ...
    pass
class EllipticalRegionConstraint(TrajectoryConstraint):
    """
    Enforces a particular constraint only within an elliptical region.
    """
    def __init__(self, center: wpimath.geometry._geometry.Translation2d, xWidth: meters, yWidth: meters, rotation: wpimath.geometry._geometry.Rotation2d, constraint: TrajectoryConstraint) -> None: 
        """
        Constructs a new EllipticalRegionConstraint.

        :param center:     The center of the ellipse in which to enforce the constraint.
        :param xWidth:     The width of the ellipse in which to enforce the constraint.
        :param yWidth:     The height of the ellipse in which to enforce the constraint.
        :param rotation:   The rotation to apply to all radii around the origin.
        :param constraint: The constraint to enforce when the robot is within the
                           region.
        """
    @staticmethod
    def fromFeet(center: wpimath.geometry._geometry.Translation2d, xWidth: feet, yWidth: feet, rotation: wpimath.geometry._geometry.Rotation2d, constraint: TrajectoryConstraint) -> EllipticalRegionConstraint: ...
    def isPoseInRegion(self, pose: wpimath.geometry._geometry.Pose2d) -> bool: 
        """
        Returns whether the specified robot pose is within the region that the
        constraint is enforced in.

        :param pose: The robot pose.

        :returns: Whether the robot pose is within the constraint region.
        """
    def maxVelocity(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, velocity: meters_per_second) -> meters_per_second: ...
    def minMaxAcceleration(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, speed: meters_per_second) -> TrajectoryConstraint.MinMax: ...
    pass
class MaxVelocityConstraint(TrajectoryConstraint):
    """
    Represents a constraint that enforces a max velocity. This can be composed
    with the EllipticalRegionConstraint or RectangularRegionConstraint to enforce
    a max velocity within a region.
    """
    def __init__(self, maxVelocity: meters_per_second) -> None: 
        """
        Constructs a new MaxVelocityConstraint.

        :param maxVelocity: The max velocity.
        """
    @staticmethod
    def fromFps(maxVelocity: feet_per_second) -> MaxVelocityConstraint: ...
    def maxVelocity(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, velocity: meters_per_second) -> meters_per_second: ...
    def minMaxAcceleration(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, speed: meters_per_second) -> TrajectoryConstraint.MinMax: ...
    pass
class MecanumDriveKinematicsConstraint(TrajectoryConstraint):
    """
    A class that enforces constraints on the mecanum drive kinematics.
    This can be used to ensure that the trajectory is constructed so that the
    commanded velocities for wheels of the drivetrain stay below a certain
    limit.
    """
    def __init__(self, kinematics: wpimath.kinematics._kinematics.MecanumDriveKinematics, maxSpeed: meters_per_second) -> None: ...
    @staticmethod
    def fromFps(kinematics: wpimath.kinematics._kinematics.MecanumDriveKinematics, maxSpeed: feet_per_second) -> MecanumDriveKinematicsConstraint: ...
    def maxVelocity(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, velocity: meters_per_second) -> meters_per_second: ...
    def minMaxAcceleration(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, speed: meters_per_second) -> TrajectoryConstraint.MinMax: ...
    pass
class RectangularRegionConstraint(TrajectoryConstraint):
    """
    Enforces a particular constraint only within a rectangular region.
    """
    def __init__(self, bottomLeftPoint: wpimath.geometry._geometry.Translation2d, topRightPoint: wpimath.geometry._geometry.Translation2d, constraint: TrajectoryConstraint) -> None: 
        """
        Constructs a new RectangularRegionConstraint.

        :param bottomLeftPoint: The bottom left point of the rectangular region in
                                which to enforce the constraint.
        :param topRightPoint:   The top right point of the rectangular region in which
                                to enforce the constraint.
        :param constraint:      The constraint to enforce when the robot is within the
                                region.
        """
    def isPoseInRegion(self, pose: wpimath.geometry._geometry.Pose2d) -> bool: 
        """
        Returns whether the specified robot pose is within the region that the
        constraint is enforced in.

        :param pose: The robot pose.

        :returns: Whether the robot pose is within the constraint region.
        """
    def maxVelocity(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, velocity: meters_per_second) -> meters_per_second: ...
    def minMaxAcceleration(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, speed: meters_per_second) -> TrajectoryConstraint.MinMax: ...
    pass
class SwerveDrive2KinematicsConstraint(TrajectoryConstraint):
    """
    A class that enforces constraints on the swerve drive kinematics.
    This can be used to ensure that the trajectory is constructed so that the
    commanded velocities of the wheels stay below a certain limit.
    """
    def __init__(self, kinematics: wpimath.kinematics._kinematics.SwerveDrive2Kinematics, maxSpeed: meters_per_second) -> None: ...
    @staticmethod
    def fromFps(kinematics: wpimath.kinematics._kinematics.SwerveDrive2Kinematics, maxSpeed: feet_per_second) -> SwerveDrive2KinematicsConstraint: ...
    def maxVelocity(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, velocity: meters_per_second) -> meters_per_second: ...
    def minMaxAcceleration(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, speed: meters_per_second) -> TrajectoryConstraint.MinMax: ...
    pass
class SwerveDrive3KinematicsConstraint(TrajectoryConstraint):
    """
    A class that enforces constraints on the swerve drive kinematics.
    This can be used to ensure that the trajectory is constructed so that the
    commanded velocities of the wheels stay below a certain limit.
    """
    def __init__(self, kinematics: wpimath.kinematics._kinematics.SwerveDrive3Kinematics, maxSpeed: meters_per_second) -> None: ...
    @staticmethod
    def fromFps(kinematics: wpimath.kinematics._kinematics.SwerveDrive3Kinematics, maxSpeed: feet_per_second) -> SwerveDrive3KinematicsConstraint: ...
    def maxVelocity(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, velocity: meters_per_second) -> meters_per_second: ...
    def minMaxAcceleration(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, speed: meters_per_second) -> TrajectoryConstraint.MinMax: ...
    pass
class SwerveDrive4KinematicsConstraint(TrajectoryConstraint):
    """
    A class that enforces constraints on the swerve drive kinematics.
    This can be used to ensure that the trajectory is constructed so that the
    commanded velocities of the wheels stay below a certain limit.
    """
    def __init__(self, kinematics: wpimath.kinematics._kinematics.SwerveDrive4Kinematics, maxSpeed: meters_per_second) -> None: ...
    @staticmethod
    def fromFps(kinematics: wpimath.kinematics._kinematics.SwerveDrive4Kinematics, maxSpeed: feet_per_second) -> SwerveDrive4KinematicsConstraint: ...
    def maxVelocity(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, velocity: meters_per_second) -> meters_per_second: ...
    def minMaxAcceleration(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, speed: meters_per_second) -> TrajectoryConstraint.MinMax: ...
    pass
class SwerveDrive6KinematicsConstraint(TrajectoryConstraint):
    """
    A class that enforces constraints on the swerve drive kinematics.
    This can be used to ensure that the trajectory is constructed so that the
    commanded velocities of the wheels stay below a certain limit.
    """
    def __init__(self, kinematics: wpimath.kinematics._kinematics.SwerveDrive6Kinematics, maxSpeed: meters_per_second) -> None: ...
    @staticmethod
    def fromFps(kinematics: wpimath.kinematics._kinematics.SwerveDrive6Kinematics, maxSpeed: feet_per_second) -> SwerveDrive6KinematicsConstraint: ...
    def maxVelocity(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, velocity: meters_per_second) -> meters_per_second: ...
    def minMaxAcceleration(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, speed: meters_per_second) -> TrajectoryConstraint.MinMax: ...
    pass
class CentripetalAccelerationConstraint(TrajectoryConstraint):
    """
    A constraint on the maximum absolute centripetal acceleration allowed when
    traversing a trajectory. The centripetal acceleration of a robot is defined
    as the velocity squared divided by the radius of curvature.

    Effectively, limiting the maximum centripetal acceleration will cause the
    robot to slow down around tight turns, making it easier to track trajectories
    with sharp turns.
    """
    def __init__(self, maxCentripetalAcceleration: meters_per_second_squared) -> None: ...
    @staticmethod
    def fromFps(maxCentripetalAcceleration: feet_per_second_squared) -> CentripetalAccelerationConstraint: ...
    def maxVelocity(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, velocity: meters_per_second) -> meters_per_second: ...
    def minMaxAcceleration(self, pose: wpimath.geometry._geometry.Pose2d, curvature: radians_per_meter, speed: meters_per_second) -> TrajectoryConstraint.MinMax: ...
    pass
