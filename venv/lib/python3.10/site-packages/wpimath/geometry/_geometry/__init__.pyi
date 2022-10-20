from __future__ import annotations
import wpimath.geometry._geometry
import typing

__all__ = [
    "Pose2d",
    "Rotation2d",
    "Transform2d",
    "Translation2d",
    "Twist2d"
]


class Pose2d():
    """
    Represents a 2d pose containing translational and rotational elements.
    """
    def X(self) -> meters: 
        """
        Returns the X component of the pose's translation.

        :returns: The x component of the pose's translation.
        """
    def Y(self) -> meters: 
        """
        Returns the Y component of the pose's translation.

        :returns: The y component of the pose's translation.
        """
    def __add__(self, arg0: Transform2d) -> Pose2d: 
        """
        Transforms the pose by the given transformation and returns the new
        transformed pose.

        [x_new]    [cos, -sin, 0][transform.x]
        [y_new] += [sin,  cos, 0][transform.y]
        [t_new]    [0,    0,   1][transform.t]

        :param other: The transform to transform the pose by.

        :returns: The transformed pose.
        """
    def __eq__(self, arg0: Pose2d) -> bool: 
        """
        Checks equality between this Pose2d and another object.

        :param other: The other object.

        :returns: Whether the two objects are equal.
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Constructs a pose at the origin facing toward the positive X axis.
        (Translation2d{0, 0} and Rotation{0})

        Constructs a pose with the specified translation and rotation.

        :param translation: The translational component of the pose.
        :param rotation:    The rotational component of the pose.

        Convenience constructors that takes in x and y values directly instead of
        having to construct a Translation2d.

        :param x:        The x component of the translational component of the pose.
        :param y:        The y component of the translational component of the pose.
        :param rotation: The rotational component of the pose.
        """
    @typing.overload
    def __init__(self, translation: Translation2d, rotation: Rotation2d) -> None: ...
    @typing.overload
    def __init__(self, x: meters, y: meters, angle: radians) -> None: ...
    @typing.overload
    def __init__(self, x: meters, y: meters, rotation: Rotation2d) -> None: ...
    def __ne__(self, arg0: Pose2d) -> bool: 
        """
        Checks inequality between this Pose2d and another object.

        :param other: The other object.

        :returns: Whether the two objects are not equal.
        """
    def __repr__(self) -> str: ...
    def __sub__(self, arg0: Pose2d) -> Transform2d: 
        """
        Returns the Transform2d that maps the one pose to another.

        :param other: The initial pose of the transformation.

        :returns: The transform that maps the other pose to the current pose.
        """
    def exp(self, twist: Twist2d) -> Pose2d: 
        """
        Obtain a new Pose2d from a (constant curvature) velocity.

        See https://file.tavsys.net/control/controls-engineering-in-frc.pdf section
        10.2 "Pose exponential" for a derivation.

        The twist is a change in pose in the robot's coordinate frame since the
        previous pose update. When the user runs exp() on the previous known
        field-relative pose with the argument being the twist, the user will
        receive the new field-relative pose.

        "Exp" represents the pose exponential, which is solving a differential
        equation moving the pose forward in time.

        :param twist: The change in pose in the robot's coordinate frame since the
                      previous pose update. For example, if a non-holonomic robot moves forward
                      0.01 meters and changes angle by 0.5 degrees since the previous pose
                      update, the twist would be Twist2d{0.01, 0.0, toRadians(0.5)}

        :returns: The new pose of the robot.
        """
    @staticmethod
    @typing.overload
    def fromFeet(x: feet, y: feet, angle: radians) -> Pose2d: ...
    @staticmethod
    @typing.overload
    def fromFeet(x: feet, y: feet, r: Rotation2d) -> Pose2d: ...
    def log(self, end: Pose2d) -> Twist2d: 
        """
        Returns a Twist2d that maps this pose to the end pose. If c is the output
        of a.Log(b), then a.Exp(c) would yield b.

        :param end: The end pose for the transformation.

        :returns: The twist that maps this to end.
        """
    def relativeTo(self, other: Pose2d) -> Pose2d: 
        """
        Returns the other pose relative to the current pose.

        This function can often be used for trajectory tracking or pose
        stabilization algorithms to get the error between the reference and the
        current pose.

        :param other: The pose that is the origin of the new coordinate frame that
                      the current pose will be converted into.

        :returns: The current pose relative to the new origin pose.
        """
    def rotation(self) -> Rotation2d: 
        """
        Returns the underlying rotation.

        :returns: Reference to the rotational component of the pose.
        """
    def transformBy(self, other: Transform2d) -> Pose2d: 
        """
        Transforms the pose by the given transformation and returns the new pose.
        See + operator for the matrix multiplication performed.

        :param other: The transform to transform the pose by.

        :returns: The transformed pose.
        """
    def translation(self) -> Translation2d: 
        """
        Returns the underlying translation.

        :returns: Reference to the translational component of the pose.
        """
    __hash__ = None
    pass
class Rotation2d():
    """
    A rotation in a 2d coordinate frame represented a point on the unit circle
    (cosine and sine).
    """
    def __add__(self, arg0: Rotation2d) -> Rotation2d: 
        """
        Adds two rotations together, with the result being bounded between -pi and
        pi.

        For example, Rotation2d.FromDegrees(30) + Rotation2d.FromDegrees(60) =
        Rotation2d{-pi/2}

        :param other: The rotation to add.

        :returns: The sum of the two rotations.
        """
    def __eq__(self, arg0: Rotation2d) -> bool: 
        """
        Checks equality between this Rotation2d and another object.

        :param other: The other object.

        :returns: Whether the two objects are equal.
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Constructs a Rotation2d with a default angle of 0 degrees.

        Constructs a Rotation2d with the given radian value.

        :param value: The value of the angle in radians.

        Constructs a Rotation2d with the given x and y (cosine and sine)
        components. The x and y don't have to be normalized.

        :param x: The x component or cosine of the rotation.
        :param y: The y component or sine of the rotation.
        """
    @typing.overload
    def __init__(self, value: radians) -> None: ...
    @typing.overload
    def __init__(self, x: float, y: float) -> None: ...
    def __mul__(self, arg0: float) -> Rotation2d: 
        """
        Multiplies the current rotation by a scalar.

        :param scalar: The scalar.

        :returns: The new scaled Rotation2d.
        """
    def __ne__(self, arg0: Rotation2d) -> bool: 
        """
        Checks inequality between this Rotation2d and another object.

        :param other: The other object.

        :returns: Whether the two objects are not equal.
        """
    def __neg__(self) -> Rotation2d: 
        """
        Takes the inverse of the current rotation. This is simply the negative of
        the current angular value.

        :returns: The inverse of the current rotation.
        """
    def __repr__(self) -> str: ...
    def __sub__(self, arg0: Rotation2d) -> Rotation2d: 
        """
        Subtracts the new rotation from the current rotation and returns the new
        rotation.

        For example, Rotation2d.FromDegrees(10) - Rotation2d.FromDegrees(100) =
        Rotation2d{-pi/2}

        :param other: The rotation to subtract.

        :returns: The difference between the two rotations.
        """
    def cos(self) -> float: 
        """
        Returns the cosine of the rotation.

        :returns: The cosine of the rotation.
        """
    def degrees(self) -> degrees: 
        """
        Returns the degree value of the rotation.

        :returns: The degree value of the rotation.
        """
    @staticmethod
    def fromDegrees(value: degrees) -> Rotation2d: ...
    def radians(self) -> radians: 
        """
        Returns the radian value of the rotation.

        :returns: The radian value of the rotation.
        """
    def rotateBy(self, other: Rotation2d) -> Rotation2d: 
        """
        Adds the new rotation to the current rotation using a rotation matrix.

        ::

          [cos_new]   [other.cos, -other.sin][cos]
          [sin_new] = [other.sin,  other.cos][sin]
          value_new = std::atan2(sin_new, cos_new)

        :param other: The rotation to rotate by.

        :returns: The new rotated Rotation2d.
        """
    def sin(self) -> float: 
        """
        Returns the sine of the rotation.

        :returns: The sine of the rotation.
        """
    def tan(self) -> float: 
        """
        Returns the tangent of the rotation.

        :returns: The tangent of the rotation.
        """
    __hash__ = None
    pass
class Transform2d():
    """
    Represents a transformation for a Pose2d.
    """
    def X(self) -> meters: 
        """
        Returns the X component of the transformation's translation.

        :returns: The x component of the transformation's translation.
        """
    def Y(self) -> meters: 
        """
        Returns the Y component of the transformation's translation.

        :returns: The y component of the transformation's translation.
        """
    def __add__(self, arg0: Transform2d) -> Transform2d: 
        """
        Composes two transformations.

        :param other: The transform to compose with this one.

        :returns: The composition of the two transformations.
        """
    def __eq__(self, arg0: Transform2d) -> bool: 
        """
        Checks equality between this Transform2d and another object.

        :param other: The other object.

        :returns: Whether the two objects are equal.
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Constructs the transform that maps the initial pose to the final pose.

        :param initial: The initial pose for the transformation.
        :param final:   The final pose for the transformation.

        Constructs a transform with the given translation and rotation components.

        :param translation: Translational component of the transform.
        :param rotation:    Rotational component of the transform.

        Constructs the identity transform -- maps an initial pose to itself.
        """
    @typing.overload
    def __init__(self, initial: Pose2d, final: Pose2d) -> None: ...
    @typing.overload
    def __init__(self, translation: Translation2d, rotation: Rotation2d) -> None: ...
    @typing.overload
    def __init__(self, x: meters, y: meters, angle: radians) -> None: ...
    def __mul__(self, arg0: float) -> Transform2d: 
        """
        Scales the transform by the scalar.

        :param scalar: The scalar.

        :returns: The scaled Transform2d.
        """
    def __ne__(self, arg0: Transform2d) -> bool: 
        """
        Checks inequality between this Transform2d and another object.

        :param other: The other object.

        :returns: Whether the two objects are not equal.
        """
    def __repr__(self) -> str: ...
    @staticmethod
    def fromFeet(x: feet, y: feet, angle: radians) -> Transform2d: ...
    def inverse(self) -> Transform2d: 
        """
        Invert the transformation. This is useful for undoing a transformation.

        :returns: The inverted transformation.
        """
    def rotation(self) -> Rotation2d: 
        """
        Returns the rotational component of the transformation.

        :returns: Reference to the rotational component of the transform.
        """
    def translation(self) -> Translation2d: 
        """
        Returns the translation component of the transformation.

        :returns: Reference to the translational component of the transform.
        """
    __hash__ = None
    pass
class Translation2d():
    """
    Represents a translation in 2d space.
    This object can be used to represent a point or a vector.

    This assumes that you are using conventional mathematical axes.
    When the robot is placed on the origin, facing toward the X direction,
    moving forward increases the X, whereas moving to the left increases the Y.
    """
    def X(self) -> meters: 
        """
        Returns the X component of the translation.

        :returns: The x component of the translation.
        """
    def Y(self) -> meters: 
        """
        Returns the Y component of the translation.

        :returns: The y component of the translation.
        """
    def __abs__(self) -> meters: ...
    def __add__(self, arg0: Translation2d) -> Translation2d: 
        """
        Adds two translations in 2d space and returns the sum. This is similar to
        vector addition.

        For example, Translation2d{1.0, 2.5} + Translation2d{2.0, 5.5} =
        Translation2d{3.0, 8.0}

        :param other: The translation to add.

        :returns: The sum of the translations.
        """
    def __eq__(self, arg0: Translation2d) -> bool: 
        """
        Checks equality between this Translation2d and another object.

        :param other: The other object.

        :returns: Whether the two objects are equal.
        """
    def __getitem__(self, arg0: int) -> meters: ...
    @typing.overload
    def __init__(self) -> None: 
        """
        Constructs a Translation2d with X and Y components equal to zero.

        Constructs a Translation2d with the X and Y components equal to the
        provided values.

        :param x: The x component of the translation.
        :param y: The y component of the translation.

        Constructs a Translation2d with the provided distance and angle. This is
        essentially converting from polar coordinates to Cartesian coordinates.

        :param distance: The distance from the origin to the end of the translation.
        :param angle:    The angle between the x-axis and the translation vector.
        """
    @typing.overload
    def __init__(self, distance: meters, angle: Rotation2d) -> None: ...
    @typing.overload
    def __init__(self, x: meters, y: meters) -> None: ...
    def __len__(self) -> int: ...
    def __mul__(self, arg0: float) -> Translation2d: 
        """
        Multiplies the translation by a scalar and returns the new translation.

        For example, Translation2d{2.0, 2.5} * 2 = Translation2d{4.0, 5.0}

        :param scalar: The scalar to multiply by.

        :returns: The scaled translation.
        """
    def __ne__(self, arg0: Translation2d) -> bool: 
        """
        Checks inequality between this Translation2d and another object.

        :param other: The other object.

        :returns: Whether the two objects are not equal.
        """
    def __neg__(self) -> Translation2d: 
        """
        Returns the inverse of the current translation. This is equivalent to
        rotating by 180 degrees, flipping the point over both axes, or simply
        negating both components of the translation.

        :returns: The inverse of the current translation.
        """
    def __repr__(self) -> str: ...
    def __sub__(self, arg0: Translation2d) -> Translation2d: 
        """
        Subtracts the other translation from the other translation and returns the
        difference.

        For example, Translation2d{5.0, 4.0} - Translation2d{1.0, 2.0} =
        Translation2d{4.0, 2.0}

        :param other: The translation to subtract.

        :returns: The difference between the two translations.
        """
    def __truediv__(self, arg0: float) -> Translation2d: 
        """
        Divides the translation by a scalar and returns the new translation.

        For example, Translation2d{2.0, 2.5} / 2 = Translation2d{1.0, 1.25}

        :param scalar: The scalar to divide by.

        :returns: The scaled translation.
        """
    def distance(self, other: Translation2d) -> meters: 
        """
        Calculates the distance between two translations in 2d space.

        This function uses the pythagorean theorem to calculate the distance.
        distance = std::sqrt((x2 - x1)^2 + (y2 - y1)^2)

        :param other: The translation to compute the distance to.

        :returns: The distance between the two translations.
        """
    def distanceFeet(self, arg0: Translation2d) -> feet: ...
    @staticmethod
    def fromFeet(x: feet, y: feet) -> Translation2d: ...
    def norm(self) -> meters: 
        """
        Returns the norm, or distance from the origin to the translation.

        :returns: The norm of the translation.
        """
    def normFeet(self) -> feet: ...
    def rotateBy(self, other: Rotation2d) -> Translation2d: 
        """
        Applies a rotation to the translation in 2d space.

        This multiplies the translation vector by a counterclockwise rotation
        matrix of the given angle.

        [x_new]   [other.cos, -other.sin][x]
        [y_new] = [other.sin,  other.cos][y]

        For example, rotating a Translation2d of {2, 0} by 90 degrees will return a
        Translation2d of {0, 2}.

        :param other: The rotation to rotate the translation by.

        :returns: The new rotated translation.
        """
    @property
    def x(self) -> meters:
        """
        :type: meters
        """
    @property
    def x_feet(self) -> feet:
        """
        :type: feet
        """
    @property
    def y(self) -> meters:
        """
        :type: meters
        """
    @property
    def y_feet(self) -> feet:
        """
        :type: feet
        """
    __hash__ = None
    pass
class Twist2d():
    """
    A change in distance along arc since the last pose update. We can use ideas
    from differential calculus to create new Pose2ds from a Twist2d and vise
    versa.

    A Twist can be used to represent a difference between two poses.
    """
    def __eq__(self, arg0: Twist2d) -> bool: 
        """
        Checks equality between this Twist2d and another object.

        :param other: The other object.

        :returns: Whether the two objects are equal.
        """
    def __init__(self, dx: meters = 0, dy: meters = 0, dtheta: radians = 0) -> None: ...
    def __ne__(self, arg0: Twist2d) -> bool: 
        """
        Checks inequality between this Twist2d and another object.

        :param other: The other object.

        :returns: Whether the two objects are not equal.
        """
    def __repr__(self) -> str: ...
    @staticmethod
    def fromFeet(dx: feet = 0, dy: feet = 0, dtheta: radians = 0) -> Twist2d: ...
    @property
    def dtheta(self) -> radians:
        """
        Angular "dtheta" component (radians)

        :type: radians
        """
    @dtheta.setter
    def dtheta(self, arg0: radians) -> None:
        """
        Angular "dtheta" component (radians)
        """
    @property
    def dtheta_degrees(self) -> degrees:
        """
        :type: degrees
        """
    @dtheta_degrees.setter
    def dtheta_degrees(self, arg1: degrees) -> None:
        pass
    @property
    def dx(self) -> meters:
        """
        Linear "dx" component

        :type: meters
        """
    @dx.setter
    def dx(self, arg0: meters) -> None:
        """
        Linear "dx" component
        """
    @property
    def dx_feet(self) -> feet:
        """
        :type: feet
        """
    @dx_feet.setter
    def dx_feet(self, arg1: feet) -> None:
        pass
    @property
    def dy(self) -> meters:
        """
        Linear "dy" component

        :type: meters
        """
    @dy.setter
    def dy(self, arg0: meters) -> None:
        """
        Linear "dy" component
        """
    @property
    def dy_feet(self) -> feet:
        """
        :type: feet
        """
    @dy_feet.setter
    def dy_feet(self, arg1: feet) -> None:
        pass
    __hash__ = None
    pass
