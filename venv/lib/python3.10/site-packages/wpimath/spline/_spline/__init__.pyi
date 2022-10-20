from __future__ import annotations
import wpimath.spline._spline
import typing
import wpimath.geometry._geometry

__all__ = [
    "CubicHermiteSpline",
    "QuinticHermiteSpline",
    "Spline3",
    "Spline5",
    "SplineHelper",
    "SplineParameterizer"
]


class Spline3():
    """
    Represents a two-dimensional parametric spline that interpolates between two
    points.

    @tparam Degree The degree of the spline.
    """
    class ControlVector():
        """
        Represents a control vector for a spline.

        Each element in each array represents the value of the derivative at the
        index. For example, the value of x[2] is the second derivative in the x
        dimension.
        """
        def __init__(self, x: typing.Tuple[float, float], y: typing.Tuple[float, float]) -> None: ...
        @property
        def x(self) -> typing.Tuple[float, float]:
            """
            :type: typing.Tuple[float, float]
            """
        @x.setter
        def x(self, arg0: typing.Tuple[float, float]) -> None:
            pass
        @property
        def y(self) -> typing.Tuple[float, float]:
            """
            :type: typing.Tuple[float, float]
            """
        @y.setter
        def y(self, arg0: typing.Tuple[float, float]) -> None:
            pass
        pass
    def __init__(self) -> None: ...
    def getPoint(self, t: float) -> typing.Tuple[wpimath.geometry._geometry.Pose2d, radians_per_meter]: 
        """
        Gets the pose and curvature at some point t on the spline.

        :param t: The point t

        :returns: The pose and curvature at that point.
        """
    pass
class Spline5():
    """
    Represents a two-dimensional parametric spline that interpolates between two
    points.

    @tparam Degree The degree of the spline.
    """
    class ControlVector():
        """
        Represents a control vector for a spline.

        Each element in each array represents the value of the derivative at the
        index. For example, the value of x[2] is the second derivative in the x
        dimension.
        """
        def __init__(self, x: typing.Tuple[float, float, float], y: typing.Tuple[float, float, float]) -> None: ...
        @property
        def x(self) -> typing.Tuple[float, float, float]:
            """
            :type: typing.Tuple[float, float, float]
            """
        @x.setter
        def x(self, arg0: typing.Tuple[float, float, float]) -> None:
            pass
        @property
        def y(self) -> typing.Tuple[float, float, float]:
            """
            :type: typing.Tuple[float, float, float]
            """
        @y.setter
        def y(self, arg0: typing.Tuple[float, float, float]) -> None:
            pass
        pass
    def __init__(self) -> None: ...
    def getPoint(self, t: float) -> typing.Tuple[wpimath.geometry._geometry.Pose2d, radians_per_meter]: 
        """
        Gets the pose and curvature at some point t on the spline.

        :param t: The point t

        :returns: The pose and curvature at that point.
        """
    pass
class CubicHermiteSpline(Spline3):
    """
    Represents a hermite spline of degree 3.
    """
    def __init__(self, xInitialControlVector: typing.Tuple[float, float], xFinalControlVector: typing.Tuple[float, float], yInitialControlVector: typing.Tuple[float, float], yFinalControlVector: typing.Tuple[float, float]) -> None: 
        """
        Constructs a cubic hermite spline with the specified control vectors. Each
        control vector contains info about the location of the point and its first
        derivative.

        :param xInitialControlVector: The control vector for the initial point in
                                      the x dimension.
        :param xFinalControlVector:   The control vector for the final point in
                                      the x dimension.
        :param yInitialControlVector: The control vector for the initial point in
                                      the y dimension.
        :param yFinalControlVector:   The control vector for the final point in
                                      the y dimension.
        """
    pass
class QuinticHermiteSpline(Spline5):
    """
    Represents a hermite spline of degree 5.
    """
    def __init__(self, xInitialControlVector: typing.Tuple[float, float, float], xFinalControlVector: typing.Tuple[float, float, float], yInitialControlVector: typing.Tuple[float, float, float], yFinalControlVector: typing.Tuple[float, float, float]) -> None: 
        """
        Constructs a quintic hermite spline with the specified control vectors.
        Each control vector contains into about the location of the point, its
        first derivative, and its second derivative.

        :param xInitialControlVector: The control vector for the initial point in
                                      the x dimension.
        :param xFinalControlVector:   The control vector for the final point in
                                      the x dimension.
        :param yInitialControlVector: The control vector for the initial point in
                                      the y dimension.
        :param yFinalControlVector:   The control vector for the final point in
                                      the y dimension.
        """
    pass
class SplineHelper():
    """
    Helper class that is used to generate cubic and quintic splines from user
    provided waypoints.
    """
    def __init__(self) -> None: ...
    @staticmethod
    def cubicControlVectorsFromWaypoints(start: wpimath.geometry._geometry.Pose2d, interiorWaypoints: typing.List[wpimath.geometry._geometry.Translation2d], end: wpimath.geometry._geometry.Pose2d) -> typing.Tuple[Spline3.ControlVector, Spline3.ControlVector]: 
        """
        Returns 2 cubic control vectors from a set of exterior waypoints and
        interior translations.

        :param start:             The starting pose.
        :param interiorWaypoints: The interior waypoints.
        :param end:               The ending pose.

        :returns: 2 cubic control vectors.
        """
    @staticmethod
    def cubicSplinesFromControlVectors(start: Spline3.ControlVector, waypoints: typing.List[wpimath.geometry._geometry.Translation2d], end: Spline3.ControlVector) -> typing.List[CubicHermiteSpline]: 
        """
        Returns a set of cubic splines corresponding to the provided control
        vectors. The user is free to set the direction of the start and end
        point. The directions for the middle waypoints are determined
        automatically to ensure continuous curvature throughout the path.

        The derivation for the algorithm used can be found here:
        <https://www.uio.no/studier/emner/matnat/ifi/nedlagte-emner/INF-MAT4350/h08/undervisningsmateriale/chap7alecture.pdf>

        :param start:     The starting control vector.
        :param waypoints: The middle waypoints. This can be left blank if you
                          only wish to create a path with two waypoints.
        :param end:       The ending control vector.

        :returns: A vector of cubic hermite splines that interpolate through the
                  provided waypoints.
        """
    @staticmethod
    def quinticSplinesFromControlVectors(controlVectors: typing.List[Spline5.ControlVector]) -> typing.List[QuinticHermiteSpline]: 
        """
        Returns a set of quintic splines corresponding to the provided control
        vectors. The user is free to set the direction of all waypoints. Continuous
        curvature is guaranteed throughout the path.

        :param controlVectors: The control vectors.

        :returns: A vector of quintic hermite splines that interpolate through the
                  provided waypoints.
        """
    @staticmethod
    def quinticSplinesFromWaypoints(waypoints: typing.List[wpimath.geometry._geometry.Pose2d]) -> typing.List[QuinticHermiteSpline]: 
        """
        Returns quintic splines from a set of waypoints.

        :param waypoints: The waypoints

        :returns: List of quintic splines.
        """
    pass
class SplineParameterizer():
    """
    Class used to parameterize a spline by its arc length.
    """
    @staticmethod
    @typing.overload
    def parameterize(spline: Spline3, t0: float = 0.0, t1: float = 1.0) -> typing.List[typing.Tuple[wpimath.geometry._geometry.Pose2d, radians_per_meter]]: 
        """
        Parameterizes the spline. This method breaks up the spline into various
        arcs until their dx, dy, and dtheta are within specific tolerances.

        :param spline: The spline to parameterize.
        :param t0:     Starting internal spline parameter. It is recommended to leave
                       this as default.
        :param t1:     Ending internal spline parameter. It is recommended to leave this
                       as default.

        :returns: A vector of poses and curvatures that represents various points on
                  the spline.

        Parameterizes the spline. This method breaks up the spline into various
        arcs until their dx, dy, and dtheta are within specific tolerances.

        :param spline: The spline to parameterize.
        :param t0:     Starting internal spline parameter. It is recommended to leave
                       this as default.
        :param t1:     Ending internal spline parameter. It is recommended to leave this
                       as default.

        :returns: A vector of poses and curvatures that represents various points on
                  the spline.
        """
    @staticmethod
    @typing.overload
    def parameterize(spline: Spline5, t0: float = 0.0, t1: float = 1.0) -> typing.List[typing.Tuple[wpimath.geometry._geometry.Pose2d, radians_per_meter]]: ...
    pass
