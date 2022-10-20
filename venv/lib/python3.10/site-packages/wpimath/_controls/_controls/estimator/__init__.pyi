from __future__ import annotations
import wpimath._controls._controls.estimator
import typing
import wpimath._controls._controls.system
import wpimath.geometry._geometry
import wpimath.kinematics._kinematics

__all__ = [
    "DifferentialDrivePoseEstimator",
    "ExtendedKalmanFilter_1_1_1",
    "ExtendedKalmanFilter_2_1_1",
    "ExtendedKalmanFilter_2_2_2",
    "KalmanFilter_1_1_1",
    "KalmanFilter_2_1_1",
    "KalmanFilter_2_2_2",
    "MecanumDrivePoseEstimator",
    "SwerveDrive2PoseEstimator",
    "SwerveDrive3PoseEstimator",
    "SwerveDrive4PoseEstimator",
    "SwerveDrive6PoseEstimator"
]


class DifferentialDrivePoseEstimator():
    """
    This class wraps an Unscented Kalman Filter to fuse latency-compensated
    vision measurements with differential drive encoder measurements. It will
    correct for noisy vision measurements and encoder drift. It is intended to be
    an easy drop-in for :class:`DifferentialDriveOdometry`. In fact, if you never call
    :meth:`addVisionMeasurement`, and only call :meth:`update`, this will behave exactly the
    same as DifferentialDriveOdometry.

    :meth:`update` should be called every robot loop (if your robot loops are faster or
    slower than the default, then you should change the nominal delta time via
    the constructor).

    :meth:`addVisionMeasurement` can be called as infrequently as you want; if you
    never call it, then this class will behave like regular encoder odometry.

    The state-space system used internally has the following states (x), inputs
    (u), and outputs (y):

    :math:`x = [x, y, \theta, dist_l, dist_r]^T` in the field coordinate
    system containing x position, y position, heading, left encoder distance,
    and right encoder distance.

    :math:`u = [v_l, v_r, d\theta]^T` containing left wheel velocity,
    right wheel velocity, and change in gyro heading.

    NB: Using velocities make things considerably easier, because it means that
    teams don't have to worry about getting an accurate model. Basically, we
    suspect that it's easier for teams to get good encoder data than it is for
    them to perform system identification well enough to get a good model.

    :math:`y = [x, y, \theta]^T` from vision containing x position, y
    position, and heading; or :math:`y = [dist_l, dist_r, \theta]^T`
    containing left encoder position, right encoder position, and gyro heading.
    """
    def __init__(self, gyroAngle: wpimath.geometry._geometry.Rotation2d, initialPose: wpimath.geometry._geometry.Pose2d, stateStdDevs: typing.Tuple[float, float, float, float, float], localMeasurementStdDevs: typing.Tuple[float, float, float], visionMeasurementStdDevs: typing.Tuple[float, float, float], nominalDt: seconds = 0.02) -> None: 
        """
        Constructs a DifferentialDrivePoseEstimator.

        :param gyroAngle:                The gyro angle of the robot.
        :param initialPose:              The estimated initial pose.
        :param stateStdDevs:             Standard deviations of model states.
                                         Increase these numbers to trust your
                                         model's state estimates less. This matrix
                                         is in the form
                                         [x, y, theta, dist_l, dist_r]ᵀ,
                                         with units in meters and radians.
        :param localMeasurementStdDevs:  Standard deviations of the encoder and gyro
                                         measurements. Increase these numbers to
                                         trust sensor readings from
                                         encoders and gyros less.
                                         This matrix is in the form
                                         [dist_l, dist_r, theta]ᵀ, with units in
                                         meters and radians.
        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from
                                         vision less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        :param nominalDt:                The period of the loop calling Update().
        """
    @typing.overload
    def addVisionMeasurement(self, visionRobotPose: wpimath.geometry._geometry.Pose2d, timestamp: seconds) -> None: 
        """
        Adds a vision measurement to the Unscented Kalman Filter. This will correct
        the odometry pose estimate while still accounting for measurement noise.

        This method can be called as infrequently as you want, as long as you are
        calling Update() every loop.

        :param visionRobotPose: The pose of the robot as measured by the vision
                                camera.
        :param timestamp:       The timestamp of the vision measurement in seconds.
                                Note that if you don't use your own time source by
                                calling UpdateWithTime(), then you must use a
                                timestamp with an epoch since FPGA startup (i.e. the
                                epoch of this timestamp is the same epoch as
                                frc::Timer::GetFPGATimestamp(). This means that
                                you should use frc::Timer::GetFPGATimestamp() as
                                your time source in this case.

        Adds a vision measurement to the Unscented Kalman Filter. This will correct
        the odometry pose estimate while still accounting for measurement noise.

        This method can be called as infrequently as you want, as long as you are
        calling Update() every loop.

        Note that the vision measurement standard deviations passed into this
        method will continue to apply to future measurements until a subsequent
        call to SetVisionMeasurementStdDevs() or this method.

        :param visionRobotPose:          The pose of the robot as measured by the
                                         vision camera.
        :param timestamp:                The timestamp of the vision measurement in
                                         seconds. Note that if you don't use your
                                         own time source by calling
                                         UpdateWithTime(), then you must use a
                                         timestamp with an epoch since FPGA startup
                                         (i.e. the epoch of this timestamp is the
                                         same epoch as
                                         frc::Timer::GetFPGATimestamp(). This means
                                         that you should use
                                         frc::Timer::GetFPGATimestamp() as your
                                         time source in this case.
        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        """
    @typing.overload
    def addVisionMeasurement(self, visionRobotPose: wpimath.geometry._geometry.Pose2d, timestamp: seconds, visionMeasurementStdDevs: typing.Tuple[float, float, float]) -> None: ...
    def getEstimatedPosition(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Returns the pose of the robot at the current time as estimated by the
        Unscented Kalman Filter.

        :returns: The estimated robot pose.
        """
    def resetPosition(self, pose: wpimath.geometry._geometry.Pose2d, gyroAngle: wpimath.geometry._geometry.Rotation2d) -> None: 
        """
        Resets the robot's position on the field.

        You NEED to reset your encoders to zero when calling this method. The
        gyroscope angle does not need to be reset here on the user's robot code.
        The library automatically takes care of offsetting the gyro angle.

        :param pose:      The estimated pose of the robot on the field.
        :param gyroAngle: The current gyro angle.
        """
    def setVisionMeasurementStdDevs(self, visionMeasurementStdDevs: typing.Tuple[float, float, float]) -> None: 
        """
        Sets the pose estimator's trust of global measurements. This might be used
        to change trust in vision measurements after the autonomous period, or to
        change trust as distance to a vision target increases.

        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        """
    def update(self, gyroAngle: wpimath.geometry._geometry.Rotation2d, wheelSpeeds: wpimath.kinematics._kinematics.DifferentialDriveWheelSpeeds, leftDistance: meters, rightDistance: meters) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the Unscented Kalman Filter using only wheel encoder information.
        Note that this should be called every loop iteration.

        :param gyroAngle:     The current gyro angle.
        :param wheelSpeeds:   The velocities of the wheels in meters per second.
        :param leftDistance:  The distance traveled by the left encoder.
        :param rightDistance: The distance traveled by the right encoder.

        :returns: The estimated pose of the robot.
        """
    def updateWithTime(self, currentTime: seconds, gyroAngle: wpimath.geometry._geometry.Rotation2d, wheelSpeeds: wpimath.kinematics._kinematics.DifferentialDriveWheelSpeeds, leftDistance: meters, rightDistance: meters) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the Unscented Kalman Filter using only wheel encoder information.
        Note that this should be called every loop iteration.

        :param currentTime:   The time at which this method was called.
        :param gyroAngle:     The current gyro angle.
        :param wheelSpeeds:   The velocities of the wheels in meters per second.
        :param leftDistance:  The distance traveled by the left encoder.
        :param rightDistance: The distance traveled by the right encoder.

        :returns: The estimated pose of the robot.
        """
    pass
class ExtendedKalmanFilter_1_1_1():
    """
    A Kalman filter combines predictions from a model and measurements to give an
    estimate of the true system state. This is useful because many states cannot
    be measured directly as a result of sensor noise, or because the state is
    "hidden".

    Kalman filters use a K gain matrix to determine whether to trust the model or
    measurements more. Kalman filter theory uses statistics to compute an optimal
    K gain which minimizes the sum of squares error in the state estimate. This K
    gain is used to correct the state estimate by some amount of the difference
    between the actual measurements and the measurements predicted by the model.

    An extended Kalman filter supports nonlinear state and measurement models. It
    propagates the error covariance by linearizing the models around the state
    estimate, then applying the linear Kalman filter equations.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf chapter 9
    "Stochastic control theory".

    @tparam States The number of states.
    @tparam Inputs The number of inputs.
    @tparam Outputs The number of outputs.
    """
    @typing.overload
    def P(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the error covariance matrix P.

        Returns an element of the error covariance matrix P.

        :param i: Row of P.
        :param j: Column of P.
        """
    @typing.overload
    def P(self, i: int, j: int) -> float: ...
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[1, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], h: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[1, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], stateStdDevs: typing.Tuple[float], measurementStdDevs: typing.Tuple[float], dt: seconds) -> None: 
        """
        Constructs an extended Kalman filter.

        :param f:                  A vector-valued function of x and u that returns
                                   the derivative of the state vector.
        :param h:                  A vector-valued function of x and u that returns
                                   the measurement vector.
        :param stateStdDevs:       Standard deviations of model states.
        :param measurementStdDevs: Standard deviations of measurements.
        :param dt:                 Nominal discretization timestep.

        Constructs an extended Kalman filter.

        :param f:                  A vector-valued function of x and u that returns
                                   the derivative of the state vector.
        :param h:                  A vector-valued function of x and u that returns
                                   the measurement vector.
        :param stateStdDevs:       Standard deviations of model states.
        :param measurementStdDevs: Standard deviations of measurements.
        :param residualFuncY:      A function that computes the residual of two
                                   measurement vectors (i.e. it subtracts them.)
        :param addFuncX:           A function that adds two state vectors.
        :param dt:                 Nominal discretization timestep.
        """
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[1, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], h: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[1, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], stateStdDevs: typing.Tuple[float], measurementStdDevs: typing.Tuple[float], residualFuncY: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[1, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], addFuncX: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[1, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], dt: seconds) -> None: ...
    def correct(self, u: numpy.ndarray[numpy.float64, _Shape[1, 1]], y: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> None: 
        """
        Correct the state estimate x-hat using the measurements in y.

        :param u: Same control input used in the predict step.
        :param y: Measurement vector.
        """
    def predict(self, u: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: 
        """
        Project the model into the future with a new control input u.

        :param u:  New control input from controller.
        :param dt: Timestep for prediction.
        """
    def reset(self) -> None: 
        """
        Resets the observer.
        """
    def setP(self, P: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> None: 
        """
        Set the current error covariance matrix P.

        :param P: The error covariance matrix P.
        """
    @typing.overload
    def setXhat(self, i: int, value: float) -> None: 
        """
        Set initial state estimate x-hat.

        :param xHat: The state estimate x-hat.

        Set an element of the initial state estimate x-hat.

        :param i:     Row of x-hat.
        :param value: Value for element of x-hat.
        """
    @typing.overload
    def setXhat(self, xHat: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> None: ...
    @typing.overload
    def xhat(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the state estimate x-hat.

        Returns an element of the state estimate x-hat.

        :param i: Row of x-hat.
        """
    @typing.overload
    def xhat(self, i: int) -> float: ...
    pass
class ExtendedKalmanFilter_2_1_1():
    """
    A Kalman filter combines predictions from a model and measurements to give an
    estimate of the true system state. This is useful because many states cannot
    be measured directly as a result of sensor noise, or because the state is
    "hidden".

    Kalman filters use a K gain matrix to determine whether to trust the model or
    measurements more. Kalman filter theory uses statistics to compute an optimal
    K gain which minimizes the sum of squares error in the state estimate. This K
    gain is used to correct the state estimate by some amount of the difference
    between the actual measurements and the measurements predicted by the model.

    An extended Kalman filter supports nonlinear state and measurement models. It
    propagates the error covariance by linearizing the models around the state
    estimate, then applying the linear Kalman filter equations.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf chapter 9
    "Stochastic control theory".

    @tparam States The number of states.
    @tparam Inputs The number of inputs.
    @tparam Outputs The number of outputs.
    """
    @typing.overload
    def P(self) -> numpy.ndarray[numpy.float64, _Shape[2, 2]]: 
        """
        Returns the error covariance matrix P.

        Returns an element of the error covariance matrix P.

        :param i: Row of P.
        :param j: Column of P.
        """
    @typing.overload
    def P(self, i: int, j: int) -> float: ...
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], h: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], stateStdDevs: typing.Tuple[float, float], measurementStdDevs: typing.Tuple[float], dt: seconds) -> None: 
        """
        Constructs an extended Kalman filter.

        :param f:                  A vector-valued function of x and u that returns
                                   the derivative of the state vector.
        :param h:                  A vector-valued function of x and u that returns
                                   the measurement vector.
        :param stateStdDevs:       Standard deviations of model states.
        :param measurementStdDevs: Standard deviations of measurements.
        :param dt:                 Nominal discretization timestep.

        Constructs an extended Kalman filter.

        :param f:                  A vector-valued function of x and u that returns
                                   the derivative of the state vector.
        :param h:                  A vector-valued function of x and u that returns
                                   the measurement vector.
        :param stateStdDevs:       Standard deviations of model states.
        :param measurementStdDevs: Standard deviations of measurements.
        :param residualFuncY:      A function that computes the residual of two
                                   measurement vectors (i.e. it subtracts them.)
        :param addFuncX:           A function that adds two state vectors.
        :param dt:                 Nominal discretization timestep.
        """
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], h: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], stateStdDevs: typing.Tuple[float, float], measurementStdDevs: typing.Tuple[float], residualFuncY: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[1, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], addFuncX: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], dt: seconds) -> None: ...
    def correct(self, u: numpy.ndarray[numpy.float64, _Shape[1, 1]], y: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> None: 
        """
        Correct the state estimate x-hat using the measurements in y.

        :param u: Same control input used in the predict step.
        :param y: Measurement vector.
        """
    def predict(self, u: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: 
        """
        Project the model into the future with a new control input u.

        :param u:  New control input from controller.
        :param dt: Timestep for prediction.
        """
    def reset(self) -> None: 
        """
        Resets the observer.
        """
    def setP(self, P: numpy.ndarray[numpy.float64, _Shape[2, 2]]) -> None: 
        """
        Set the current error covariance matrix P.

        :param P: The error covariance matrix P.
        """
    @typing.overload
    def setXhat(self, i: int, value: float) -> None: 
        """
        Set initial state estimate x-hat.

        :param xHat: The state estimate x-hat.

        Set an element of the initial state estimate x-hat.

        :param i:     Row of x-hat.
        :param value: Value for element of x-hat.
        """
    @typing.overload
    def setXhat(self, xHat: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def xhat(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the state estimate x-hat.

        Returns an element of the state estimate x-hat.

        :param i: Row of x-hat.
        """
    @typing.overload
    def xhat(self, i: int) -> float: ...
    pass
class ExtendedKalmanFilter_2_2_2():
    """
    A Kalman filter combines predictions from a model and measurements to give an
    estimate of the true system state. This is useful because many states cannot
    be measured directly as a result of sensor noise, or because the state is
    "hidden".

    Kalman filters use a K gain matrix to determine whether to trust the model or
    measurements more. Kalman filter theory uses statistics to compute an optimal
    K gain which minimizes the sum of squares error in the state estimate. This K
    gain is used to correct the state estimate by some amount of the difference
    between the actual measurements and the measurements predicted by the model.

    An extended Kalman filter supports nonlinear state and measurement models. It
    propagates the error covariance by linearizing the models around the state
    estimate, then applying the linear Kalman filter equations.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf chapter 9
    "Stochastic control theory".

    @tparam States The number of states.
    @tparam Inputs The number of inputs.
    @tparam Outputs The number of outputs.
    """
    @typing.overload
    def P(self) -> numpy.ndarray[numpy.float64, _Shape[2, 2]]: 
        """
        Returns the error covariance matrix P.

        Returns an element of the error covariance matrix P.

        :param i: Row of P.
        :param j: Column of P.
        """
    @typing.overload
    def P(self, i: int, j: int) -> float: ...
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], h: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], stateStdDevs: typing.Tuple[float, float], measurementStdDevs: typing.Tuple[float, float], dt: seconds) -> None: 
        """
        Constructs an extended Kalman filter.

        :param f:                  A vector-valued function of x and u that returns
                                   the derivative of the state vector.
        :param h:                  A vector-valued function of x and u that returns
                                   the measurement vector.
        :param stateStdDevs:       Standard deviations of model states.
        :param measurementStdDevs: Standard deviations of measurements.
        :param dt:                 Nominal discretization timestep.

        Constructs an extended Kalman filter.

        :param f:                  A vector-valued function of x and u that returns
                                   the derivative of the state vector.
        :param h:                  A vector-valued function of x and u that returns
                                   the measurement vector.
        :param stateStdDevs:       Standard deviations of model states.
        :param measurementStdDevs: Standard deviations of measurements.
        :param residualFuncY:      A function that computes the residual of two
                                   measurement vectors (i.e. it subtracts them.)
        :param addFuncX:           A function that adds two state vectors.
        :param dt:                 Nominal discretization timestep.
        """
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], h: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], stateStdDevs: typing.Tuple[float, float], measurementStdDevs: typing.Tuple[float, float], residualFuncY: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], addFuncX: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], dt: seconds) -> None: ...
    def correct(self, u: numpy.ndarray[numpy.float64, _Shape[2, 1]], y: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: 
        """
        Correct the state estimate x-hat using the measurements in y.

        :param u: Same control input used in the predict step.
        :param y: Measurement vector.
        """
    def predict(self, u: numpy.ndarray[numpy.float64, _Shape[2, 1]], dt: seconds) -> None: 
        """
        Project the model into the future with a new control input u.

        :param u:  New control input from controller.
        :param dt: Timestep for prediction.
        """
    def reset(self) -> None: 
        """
        Resets the observer.
        """
    def setP(self, P: numpy.ndarray[numpy.float64, _Shape[2, 2]]) -> None: 
        """
        Set the current error covariance matrix P.

        :param P: The error covariance matrix P.
        """
    @typing.overload
    def setXhat(self, i: int, value: float) -> None: 
        """
        Set initial state estimate x-hat.

        :param xHat: The state estimate x-hat.

        Set an element of the initial state estimate x-hat.

        :param i:     Row of x-hat.
        :param value: Value for element of x-hat.
        """
    @typing.overload
    def setXhat(self, xHat: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def xhat(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the state estimate x-hat.

        Returns an element of the state estimate x-hat.

        :param i: Row of x-hat.
        """
    @typing.overload
    def xhat(self, i: int) -> float: ...
    pass
class KalmanFilter_1_1_1():
    def __init__(self, plant: wpimath._controls._controls.system.LinearSystem_1_1_1, stateStdDevs: typing.Tuple[float], measurementStdDevs: typing.Tuple[float], dt: seconds) -> None: 
        """
        Constructs a state-space observer with the given plant.

        :param plant:              The plant used for the prediction step.
        :param stateStdDevs:       Standard deviations of model states.
        :param measurementStdDevs: Standard deviations of measurements.
        :param dt:                 Nominal discretization timestep.
        """
    pass
class KalmanFilter_2_1_1():
    def __init__(self, plant: wpimath._controls._controls.system.LinearSystem_2_1_1, stateStdDevs: typing.Tuple[float, float], measurementStdDevs: typing.Tuple[float], dt: seconds) -> None: 
        """
        Constructs a state-space observer with the given plant.

        :param plant:              The plant used for the prediction step.
        :param stateStdDevs:       Standard deviations of model states.
        :param measurementStdDevs: Standard deviations of measurements.
        :param dt:                 Nominal discretization timestep.
        """
    pass
class KalmanFilter_2_2_2():
    def __init__(self, plant: wpimath._controls._controls.system.LinearSystem_2_2_2, stateStdDevs: typing.Tuple[float, float], measurementStdDevs: typing.Tuple[float, float], dt: seconds) -> None: 
        """
        Constructs a state-space observer with the given plant.

        :param plant:              The plant used for the prediction step.
        :param stateStdDevs:       Standard deviations of model states.
        :param measurementStdDevs: Standard deviations of measurements.
        :param dt:                 Nominal discretization timestep.
        """
    pass
class MecanumDrivePoseEstimator():
    """
    This class wraps an Unscented Kalman Filter to fuse latency-compensated
    vision measurements with mecanum drive encoder velocity measurements. It will
    correct for noisy measurements and encoder drift. It is intended to be an
    easy but more accurate drop-in for :class:`MecanumDriveOdometry`.

    :meth:`update` should be called every robot loop. If your loops are faster or
    slower than the default of 0.02s, then you should change the nominal delta
    time by specifying it in the constructor.

    :meth:`addVisionMeasurement` can be called as infrequently as you want; if you
    never call it, then this class will behave mostly like regular encoder
    odometry.

    The state-space system used internally has the following states (x), inputs
    (u), and outputs (y):

    :math:`x = [x, y, \theta]^T` in the field-coordinate system
    containing x position, y position, and heading.

    :math:`u = [v_x, v_y, \omega]^T` containing x velocity, y velocity,
    and angular velocity in the field-coordinate system.

    :math:`y = [x, y, \theta]^T` from vision containing x position, y
    position, and heading; or :math:`y = [theta]^T` containing gyro
    heading.
    """
    def __init__(self, gyroAngle: wpimath.geometry._geometry.Rotation2d, initialPose: wpimath.geometry._geometry.Pose2d, kinematics: wpimath.kinematics._kinematics.MecanumDriveKinematics, stateStdDevs: typing.Tuple[float, float, float], localMeasurementStdDevs: typing.Tuple[float], visionMeasurementStdDevs: typing.Tuple[float, float, float], nominalDt: seconds = 0.02) -> None: 
        """
        Constructs a MecanumDrivePoseEstimator.

        :param gyroAngle:                The current gyro angle.
        :param initialPose:              The starting pose estimate.
        :param kinematics:               A correctly-configured kinematics object
                                         for your drivetrain.
        :param stateStdDevs:             Standard deviations of model states.
                                         Increase these numbers to trust your
                                         model's state estimates less. This matrix
                                         is in the form [x, y, theta]ᵀ, with units
                                         in meters and radians.
        :param localMeasurementStdDevs:  Standard deviations of the encoder and gyro
                                         measurements. Increase these numbers to
                                         trust sensor readings from encoders
                                         and gyros less. This matrix is in the form
                                         [theta], with units in radians.
        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        :param nominalDt:                The time in seconds between each robot
                                         loop.
        """
    @typing.overload
    def addVisionMeasurement(self, visionRobotPose: wpimath.geometry._geometry.Pose2d, timestamp: seconds) -> None: 
        """
        Add a vision measurement to the Unscented Kalman Filter. This will correct
        the odometry pose estimate while still accounting for measurement noise.

        This method can be called as infrequently as you want, as long as you are
        calling Update() every loop.

        :param visionRobotPose: The pose of the robot as measured by the vision
                                camera.
        :param timestamp:       The timestamp of the vision measurement in seconds.
                                Note that if you don't use your own time source by
                                calling UpdateWithTime() then you must use a
                                timestamp with an epoch since FPGA startup
                                (i.e. the epoch of this timestamp is the same
                                epoch as Timer#GetFPGATimestamp.) This means
                                that you should use Timer#GetFPGATimestamp as your
                                time source or sync the epochs.

        Adds a vision measurement to the Unscented Kalman Filter. This will correct
        the odometry pose estimate while still accounting for measurement noise.

        This method can be called as infrequently as you want, as long as you are
        calling Update() every loop.

        Note that the vision measurement standard deviations passed into this
        method will continue to apply to future measurements until a subsequent
        call to SetVisionMeasurementStdDevs() or this method.

        :param visionRobotPose:          The pose of the robot as measured by the
                                         vision camera.
        :param timestamp:                The timestamp of the vision measurement in
                                         seconds. Note that if you don't use your
                                         own time source by calling
                                         UpdateWithTime(), then you must use a
                                         timestamp with an epoch since FPGA startup
                                         (i.e. the epoch of this timestamp is the
                                         same epoch as
                                         frc::Timer::GetFPGATimestamp(). This means
                                         that you should use
                                         frc::Timer::GetFPGATimestamp() as your
                                         time source in this case.
        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        """
    @typing.overload
    def addVisionMeasurement(self, visionRobotPose: wpimath.geometry._geometry.Pose2d, timestamp: seconds, visionMeasurementStdDevs: typing.Tuple[float, float, float]) -> None: ...
    def getEstimatedPosition(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Gets the pose of the robot at the current time as estimated by the Extended
        Kalman Filter.

        :returns: The estimated robot pose in meters.
        """
    def resetPosition(self, pose: wpimath.geometry._geometry.Pose2d, gyroAngle: wpimath.geometry._geometry.Rotation2d) -> None: 
        """
        Resets the robot's position on the field.

        You NEED to reset your encoders (to zero) when calling this method.

        The gyroscope angle does not need to be reset in the user's robot code.
        The library automatically takes care of offsetting the gyro angle.

        :param pose:      The position on the field that your robot is at.
        :param gyroAngle: The angle reported by the gyroscope.
        """
    def setVisionMeasurementStdDevs(self, visionMeasurementStdDevs: typing.Tuple[float, float, float]) -> None: 
        """
        Sets the pose estimator's trust of global measurements. This might be used
        to change trust in vision measurements after the autonomous period, or to
        change trust as distance to a vision target increases.

        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        """
    def update(self, gyroAngle: wpimath.geometry._geometry.Rotation2d, wheelSpeeds: wpimath.kinematics._kinematics.MecanumDriveWheelSpeeds) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the the Unscented Kalman Filter using only wheel encoder
        information. This should be called every loop, and the correct loop period
        must be passed into the constructor of this class.

        :param gyroAngle:   The current gyro angle.
        :param wheelSpeeds: The current speeds of the mecanum drive wheels.

        :returns: The estimated pose of the robot in meters.
        """
    def updateWithTime(self, currentTime: seconds, gyroAngle: wpimath.geometry._geometry.Rotation2d, wheelSpeeds: wpimath.kinematics._kinematics.MecanumDriveWheelSpeeds) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the the Unscented Kalman Filter using only wheel encoder
        information. This should be called every loop, and the correct loop period
        must be passed into the constructor of this class.

        :param currentTime: Time at which this method was called, in seconds.
        :param gyroAngle:   The current gyroscope angle.
        :param wheelSpeeds: The current speeds of the mecanum drive wheels.

        :returns: The estimated pose of the robot in meters.
        """
    pass
class SwerveDrive2PoseEstimator():
    """
    This class wraps an Unscented Kalman Filter to fuse latency-compensated
    vision measurements with swerve drive encoder velocity measurements. It will
    correct for noisy measurements and encoder drift. It is intended to be an
    easy but more accurate drop-in for :class:`SwerveDriveOdometry`.

    :meth:`update` should be called every robot loop. If your loops are faster or
    slower than the default of 0.02s, then you should change the nominal delta
    time by specifying it in the constructor.

    :meth:`addVisionMeasurement` can be called as infrequently as you want; if you
    never call it, then this class will behave mostly like regular encoder
    odometry.

    The state-space system used internally has the following states (x), inputs
    (u), and outputs (y):

    :math:`x = [x, y, \theta]^T` in the field-coordinate system
    containing x position, y position, and heading.

    :math:`u = [v_x, v_y, \omega]^T` containing x velocity, y velocity,
    and angular velocity in the field-coordinate system.

    :math:`y = [x, y, \theta]^T` from vision containing x position, y
    position, and heading; or :math:`y = [theta]^T` containing gyro
    heading.
    """
    def __init__(self, gyroAngle: wpimath.geometry._geometry.Rotation2d, initialPose: wpimath.geometry._geometry.Pose2d, kinematics: wpimath.kinematics._kinematics.SwerveDrive2Kinematics, stateStdDevs: typing.Tuple[float, float, float], localMeasurementStdDevs: typing.Tuple[float], visionMeasurementStdDevs: typing.Tuple[float, float, float], nominalDt: seconds = 0.02) -> None: 
        """
        Constructs a SwerveDrivePoseEstimator.

        :param gyroAngle:                The current gyro angle.
        :param initialPose:              The starting pose estimate.
        :param kinematics:               A correctly-configured kinematics object
                                         for your drivetrain.
        :param stateStdDevs:             Standard deviations of model states.
                                         Increase these numbers to trust your
                                         model's state estimates less. This matrix
                                         is in the form [x, y, theta]ᵀ, with units
                                         in meters and radians.
        :param localMeasurementStdDevs:  Standard deviations of the encoder and gyro
                                         measurements. Increase these numbers to
                                         trust sensor readings from encoders
                                         and gyros less. This matrix is in the form
                                         [theta], with units in radians.
        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        :param nominalDt:                The time in seconds between each robot
                                         loop.
        """
    @typing.overload
    def addVisionMeasurement(self, visionRobotPose: wpimath.geometry._geometry.Pose2d, timestamp: seconds) -> None: 
        """
        Add a vision measurement to the Unscented Kalman Filter. This will correct
        the odometry pose estimate while still accounting for measurement noise.

        This method can be called as infrequently as you want, as long as you are
        calling Update() every loop.

        :param visionRobotPose: The pose of the robot as measured by the vision
                                camera.
        :param timestamp:       The timestamp of the vision measurement in seconds.
                                Note that if you don't use your own time source by
                                calling UpdateWithTime() then you must use a
                                timestamp with an epoch since FPGA startup
                                (i.e. the epoch of this timestamp is the same
                                epoch as Timer#GetFPGATimestamp.) This means
                                that you should use Timer#GetFPGATimestamp as your
                                time source or sync the epochs.

        Adds a vision measurement to the Unscented Kalman Filter. This will correct
        the odometry pose estimate while still accounting for measurement noise.

        This method can be called as infrequently as you want, as long as you are
        calling Update() every loop.

        Note that the vision measurement standard deviations passed into this
        method will continue to apply to future measurements until a subsequent
        call to SetVisionMeasurementStdDevs() or this method.

        :param visionRobotPose:          The pose of the robot as measured by the
                                         vision camera.
        :param timestamp:                The timestamp of the vision measurement in
                                         seconds. Note that if you don't use your
                                         own time source by calling
                                         UpdateWithTime(), then you must use a
                                         timestamp with an epoch since FPGA startup
                                         (i.e. the epoch of this timestamp is the
                                         same epoch as
                                         frc::Timer::GetFPGATimestamp(). This means
                                         that you should use
                                         frc::Timer::GetFPGATimestamp() as your
                                         time source in this case.
        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        """
    @typing.overload
    def addVisionMeasurement(self, visionRobotPose: wpimath.geometry._geometry.Pose2d, timestamp: seconds, visionMeasurementStdDevs: typing.Tuple[float, float, float]) -> None: ...
    def getEstimatedPosition(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Gets the pose of the robot at the current time as estimated by the Extended
        Kalman Filter.

        :returns: The estimated robot pose in meters.
        """
    def resetPosition(self, pose: wpimath.geometry._geometry.Pose2d, gyroAngle: wpimath.geometry._geometry.Rotation2d) -> None: 
        """
        Resets the robot's position on the field.

        You NEED to reset your encoders (to zero) when calling this method.

        The gyroscope angle does not need to be reset in the user's robot code.
        The library automatically takes care of offsetting the gyro angle.

        :param pose:      The position on the field that your robot is at.
        :param gyroAngle: The angle reported by the gyroscope.
        """
    def setVisionMeasurementStdDevs(self, visionMeasurementStdDevs: typing.Tuple[float, float, float]) -> None: 
        """
        Sets the pose estimator's trust of global measurements. This might be used
        to change trust in vision measurements after the autonomous period, or to
        change trust as distance to a vision target increases.

        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        """
    def update(self, arg0: wpimath.geometry._geometry.Rotation2d, arg1: wpimath.kinematics._kinematics.SwerveModuleState, arg2: wpimath.kinematics._kinematics.SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the the Unscented Kalman Filter using only wheel encoder
        information. This should be called every loop, and the correct loop period
        must be passed into the constructor of this class.

        :param gyroAngle:    The current gyro angle.
        :param moduleStates: The current velocities and rotations of the swerve
                             modules.

        :returns: The estimated pose of the robot in meters.
        """
    def updateWithTime(self, arg0: seconds, arg1: wpimath.geometry._geometry.Rotation2d, arg2: wpimath.kinematics._kinematics.SwerveModuleState, arg3: wpimath.kinematics._kinematics.SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the the Unscented Kalman Filter using only wheel encoder
        information. This should be called every loop, and the correct loop period
        must be passed into the constructor of this class.

        :param currentTime:  Time at which this method was called, in seconds.
        :param gyroAngle:    The current gyroscope angle.
        :param moduleStates: The current velocities and rotations of the swerve
                             modules.

        :returns: The estimated pose of the robot in meters.
        """
    pass
class SwerveDrive3PoseEstimator():
    """
    This class wraps an Unscented Kalman Filter to fuse latency-compensated
    vision measurements with swerve drive encoder velocity measurements. It will
    correct for noisy measurements and encoder drift. It is intended to be an
    easy but more accurate drop-in for :class:`SwerveDriveOdometry`.

    :meth:`update` should be called every robot loop. If your loops are faster or
    slower than the default of 0.02s, then you should change the nominal delta
    time by specifying it in the constructor.

    :meth:`addVisionMeasurement` can be called as infrequently as you want; if you
    never call it, then this class will behave mostly like regular encoder
    odometry.

    The state-space system used internally has the following states (x), inputs
    (u), and outputs (y):

    :math:`x = [x, y, \theta]^T` in the field-coordinate system
    containing x position, y position, and heading.

    :math:`u = [v_x, v_y, \omega]^T` containing x velocity, y velocity,
    and angular velocity in the field-coordinate system.

    :math:`y = [x, y, \theta]^T` from vision containing x position, y
    position, and heading; or :math:`y = [theta]^T` containing gyro
    heading.
    """
    def __init__(self, gyroAngle: wpimath.geometry._geometry.Rotation2d, initialPose: wpimath.geometry._geometry.Pose2d, kinematics: wpimath.kinematics._kinematics.SwerveDrive3Kinematics, stateStdDevs: typing.Tuple[float, float, float], localMeasurementStdDevs: typing.Tuple[float], visionMeasurementStdDevs: typing.Tuple[float, float, float], nominalDt: seconds = 0.02) -> None: 
        """
        Constructs a SwerveDrivePoseEstimator.

        :param gyroAngle:                The current gyro angle.
        :param initialPose:              The starting pose estimate.
        :param kinematics:               A correctly-configured kinematics object
                                         for your drivetrain.
        :param stateStdDevs:             Standard deviations of model states.
                                         Increase these numbers to trust your
                                         model's state estimates less. This matrix
                                         is in the form [x, y, theta]ᵀ, with units
                                         in meters and radians.
        :param localMeasurementStdDevs:  Standard deviations of the encoder and gyro
                                         measurements. Increase these numbers to
                                         trust sensor readings from encoders
                                         and gyros less. This matrix is in the form
                                         [theta], with units in radians.
        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        :param nominalDt:                The time in seconds between each robot
                                         loop.
        """
    @typing.overload
    def addVisionMeasurement(self, visionRobotPose: wpimath.geometry._geometry.Pose2d, timestamp: seconds) -> None: 
        """
        Add a vision measurement to the Unscented Kalman Filter. This will correct
        the odometry pose estimate while still accounting for measurement noise.

        This method can be called as infrequently as you want, as long as you are
        calling Update() every loop.

        :param visionRobotPose: The pose of the robot as measured by the vision
                                camera.
        :param timestamp:       The timestamp of the vision measurement in seconds.
                                Note that if you don't use your own time source by
                                calling UpdateWithTime() then you must use a
                                timestamp with an epoch since FPGA startup
                                (i.e. the epoch of this timestamp is the same
                                epoch as Timer#GetFPGATimestamp.) This means
                                that you should use Timer#GetFPGATimestamp as your
                                time source or sync the epochs.

        Adds a vision measurement to the Unscented Kalman Filter. This will correct
        the odometry pose estimate while still accounting for measurement noise.

        This method can be called as infrequently as you want, as long as you are
        calling Update() every loop.

        Note that the vision measurement standard deviations passed into this
        method will continue to apply to future measurements until a subsequent
        call to SetVisionMeasurementStdDevs() or this method.

        :param visionRobotPose:          The pose of the robot as measured by the
                                         vision camera.
        :param timestamp:                The timestamp of the vision measurement in
                                         seconds. Note that if you don't use your
                                         own time source by calling
                                         UpdateWithTime(), then you must use a
                                         timestamp with an epoch since FPGA startup
                                         (i.e. the epoch of this timestamp is the
                                         same epoch as
                                         frc::Timer::GetFPGATimestamp(). This means
                                         that you should use
                                         frc::Timer::GetFPGATimestamp() as your
                                         time source in this case.
        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        """
    @typing.overload
    def addVisionMeasurement(self, visionRobotPose: wpimath.geometry._geometry.Pose2d, timestamp: seconds, visionMeasurementStdDevs: typing.Tuple[float, float, float]) -> None: ...
    def getEstimatedPosition(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Gets the pose of the robot at the current time as estimated by the Extended
        Kalman Filter.

        :returns: The estimated robot pose in meters.
        """
    def resetPosition(self, pose: wpimath.geometry._geometry.Pose2d, gyroAngle: wpimath.geometry._geometry.Rotation2d) -> None: 
        """
        Resets the robot's position on the field.

        You NEED to reset your encoders (to zero) when calling this method.

        The gyroscope angle does not need to be reset in the user's robot code.
        The library automatically takes care of offsetting the gyro angle.

        :param pose:      The position on the field that your robot is at.
        :param gyroAngle: The angle reported by the gyroscope.
        """
    def setVisionMeasurementStdDevs(self, visionMeasurementStdDevs: typing.Tuple[float, float, float]) -> None: 
        """
        Sets the pose estimator's trust of global measurements. This might be used
        to change trust in vision measurements after the autonomous period, or to
        change trust as distance to a vision target increases.

        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        """
    def update(self, arg0: wpimath.geometry._geometry.Rotation2d, arg1: wpimath.kinematics._kinematics.SwerveModuleState, arg2: wpimath.kinematics._kinematics.SwerveModuleState, arg3: wpimath.kinematics._kinematics.SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the the Unscented Kalman Filter using only wheel encoder
        information. This should be called every loop, and the correct loop period
        must be passed into the constructor of this class.

        :param gyroAngle:    The current gyro angle.
        :param moduleStates: The current velocities and rotations of the swerve
                             modules.

        :returns: The estimated pose of the robot in meters.
        """
    def updateWithTime(self, arg0: seconds, arg1: wpimath.geometry._geometry.Rotation2d, arg2: wpimath.kinematics._kinematics.SwerveModuleState, arg3: wpimath.kinematics._kinematics.SwerveModuleState, arg4: wpimath.kinematics._kinematics.SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the the Unscented Kalman Filter using only wheel encoder
        information. This should be called every loop, and the correct loop period
        must be passed into the constructor of this class.

        :param currentTime:  Time at which this method was called, in seconds.
        :param gyroAngle:    The current gyroscope angle.
        :param moduleStates: The current velocities and rotations of the swerve
                             modules.

        :returns: The estimated pose of the robot in meters.
        """
    pass
class SwerveDrive4PoseEstimator():
    """
    This class wraps an Unscented Kalman Filter to fuse latency-compensated
    vision measurements with swerve drive encoder velocity measurements. It will
    correct for noisy measurements and encoder drift. It is intended to be an
    easy but more accurate drop-in for :class:`SwerveDriveOdometry`.

    :meth:`update` should be called every robot loop. If your loops are faster or
    slower than the default of 0.02s, then you should change the nominal delta
    time by specifying it in the constructor.

    :meth:`addVisionMeasurement` can be called as infrequently as you want; if you
    never call it, then this class will behave mostly like regular encoder
    odometry.

    The state-space system used internally has the following states (x), inputs
    (u), and outputs (y):

    :math:`x = [x, y, \theta]^T` in the field-coordinate system
    containing x position, y position, and heading.

    :math:`u = [v_x, v_y, \omega]^T` containing x velocity, y velocity,
    and angular velocity in the field-coordinate system.

    :math:`y = [x, y, \theta]^T` from vision containing x position, y
    position, and heading; or :math:`y = [theta]^T` containing gyro
    heading.
    """
    def __init__(self, gyroAngle: wpimath.geometry._geometry.Rotation2d, initialPose: wpimath.geometry._geometry.Pose2d, kinematics: wpimath.kinematics._kinematics.SwerveDrive4Kinematics, stateStdDevs: typing.Tuple[float, float, float], localMeasurementStdDevs: typing.Tuple[float], visionMeasurementStdDevs: typing.Tuple[float, float, float], nominalDt: seconds = 0.02) -> None: 
        """
        Constructs a SwerveDrivePoseEstimator.

        :param gyroAngle:                The current gyro angle.
        :param initialPose:              The starting pose estimate.
        :param kinematics:               A correctly-configured kinematics object
                                         for your drivetrain.
        :param stateStdDevs:             Standard deviations of model states.
                                         Increase these numbers to trust your
                                         model's state estimates less. This matrix
                                         is in the form [x, y, theta]ᵀ, with units
                                         in meters and radians.
        :param localMeasurementStdDevs:  Standard deviations of the encoder and gyro
                                         measurements. Increase these numbers to
                                         trust sensor readings from encoders
                                         and gyros less. This matrix is in the form
                                         [theta], with units in radians.
        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        :param nominalDt:                The time in seconds between each robot
                                         loop.
        """
    @typing.overload
    def addVisionMeasurement(self, visionRobotPose: wpimath.geometry._geometry.Pose2d, timestamp: seconds) -> None: 
        """
        Add a vision measurement to the Unscented Kalman Filter. This will correct
        the odometry pose estimate while still accounting for measurement noise.

        This method can be called as infrequently as you want, as long as you are
        calling Update() every loop.

        :param visionRobotPose: The pose of the robot as measured by the vision
                                camera.
        :param timestamp:       The timestamp of the vision measurement in seconds.
                                Note that if you don't use your own time source by
                                calling UpdateWithTime() then you must use a
                                timestamp with an epoch since FPGA startup
                                (i.e. the epoch of this timestamp is the same
                                epoch as Timer#GetFPGATimestamp.) This means
                                that you should use Timer#GetFPGATimestamp as your
                                time source or sync the epochs.

        Adds a vision measurement to the Unscented Kalman Filter. This will correct
        the odometry pose estimate while still accounting for measurement noise.

        This method can be called as infrequently as you want, as long as you are
        calling Update() every loop.

        Note that the vision measurement standard deviations passed into this
        method will continue to apply to future measurements until a subsequent
        call to SetVisionMeasurementStdDevs() or this method.

        :param visionRobotPose:          The pose of the robot as measured by the
                                         vision camera.
        :param timestamp:                The timestamp of the vision measurement in
                                         seconds. Note that if you don't use your
                                         own time source by calling
                                         UpdateWithTime(), then you must use a
                                         timestamp with an epoch since FPGA startup
                                         (i.e. the epoch of this timestamp is the
                                         same epoch as
                                         frc::Timer::GetFPGATimestamp(). This means
                                         that you should use
                                         frc::Timer::GetFPGATimestamp() as your
                                         time source in this case.
        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        """
    @typing.overload
    def addVisionMeasurement(self, visionRobotPose: wpimath.geometry._geometry.Pose2d, timestamp: seconds, visionMeasurementStdDevs: typing.Tuple[float, float, float]) -> None: ...
    def getEstimatedPosition(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Gets the pose of the robot at the current time as estimated by the Extended
        Kalman Filter.

        :returns: The estimated robot pose in meters.
        """
    def resetPosition(self, pose: wpimath.geometry._geometry.Pose2d, gyroAngle: wpimath.geometry._geometry.Rotation2d) -> None: 
        """
        Resets the robot's position on the field.

        You NEED to reset your encoders (to zero) when calling this method.

        The gyroscope angle does not need to be reset in the user's robot code.
        The library automatically takes care of offsetting the gyro angle.

        :param pose:      The position on the field that your robot is at.
        :param gyroAngle: The angle reported by the gyroscope.
        """
    def setVisionMeasurementStdDevs(self, visionMeasurementStdDevs: typing.Tuple[float, float, float]) -> None: 
        """
        Sets the pose estimator's trust of global measurements. This might be used
        to change trust in vision measurements after the autonomous period, or to
        change trust as distance to a vision target increases.

        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        """
    def update(self, arg0: wpimath.geometry._geometry.Rotation2d, arg1: wpimath.kinematics._kinematics.SwerveModuleState, arg2: wpimath.kinematics._kinematics.SwerveModuleState, arg3: wpimath.kinematics._kinematics.SwerveModuleState, arg4: wpimath.kinematics._kinematics.SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the the Unscented Kalman Filter using only wheel encoder
        information. This should be called every loop, and the correct loop period
        must be passed into the constructor of this class.

        :param gyroAngle:    The current gyro angle.
        :param moduleStates: The current velocities and rotations of the swerve
                             modules.

        :returns: The estimated pose of the robot in meters.
        """
    def updateWithTime(self, arg0: seconds, arg1: wpimath.geometry._geometry.Rotation2d, arg2: wpimath.kinematics._kinematics.SwerveModuleState, arg3: wpimath.kinematics._kinematics.SwerveModuleState, arg4: wpimath.kinematics._kinematics.SwerveModuleState, arg5: wpimath.kinematics._kinematics.SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the the Unscented Kalman Filter using only wheel encoder
        information. This should be called every loop, and the correct loop period
        must be passed into the constructor of this class.

        :param currentTime:  Time at which this method was called, in seconds.
        :param gyroAngle:    The current gyroscope angle.
        :param moduleStates: The current velocities and rotations of the swerve
                             modules.

        :returns: The estimated pose of the robot in meters.
        """
    pass
class SwerveDrive6PoseEstimator():
    """
    This class wraps an Unscented Kalman Filter to fuse latency-compensated
    vision measurements with swerve drive encoder velocity measurements. It will
    correct for noisy measurements and encoder drift. It is intended to be an
    easy but more accurate drop-in for :class:`SwerveDriveOdometry`.

    :meth:`update` should be called every robot loop. If your loops are faster or
    slower than the default of 0.02s, then you should change the nominal delta
    time by specifying it in the constructor.

    :meth:`addVisionMeasurement` can be called as infrequently as you want; if you
    never call it, then this class will behave mostly like regular encoder
    odometry.

    The state-space system used internally has the following states (x), inputs
    (u), and outputs (y):

    :math:`x = [x, y, \theta]^T` in the field-coordinate system
    containing x position, y position, and heading.

    :math:`u = [v_x, v_y, \omega]^T` containing x velocity, y velocity,
    and angular velocity in the field-coordinate system.

    :math:`y = [x, y, \theta]^T` from vision containing x position, y
    position, and heading; or :math:`y = [theta]^T` containing gyro
    heading.
    """
    def __init__(self, gyroAngle: wpimath.geometry._geometry.Rotation2d, initialPose: wpimath.geometry._geometry.Pose2d, kinematics: wpimath.kinematics._kinematics.SwerveDrive6Kinematics, stateStdDevs: typing.Tuple[float, float, float], localMeasurementStdDevs: typing.Tuple[float], visionMeasurementStdDevs: typing.Tuple[float, float, float], nominalDt: seconds = 0.02) -> None: 
        """
        Constructs a SwerveDrivePoseEstimator.

        :param gyroAngle:                The current gyro angle.
        :param initialPose:              The starting pose estimate.
        :param kinematics:               A correctly-configured kinematics object
                                         for your drivetrain.
        :param stateStdDevs:             Standard deviations of model states.
                                         Increase these numbers to trust your
                                         model's state estimates less. This matrix
                                         is in the form [x, y, theta]ᵀ, with units
                                         in meters and radians.
        :param localMeasurementStdDevs:  Standard deviations of the encoder and gyro
                                         measurements. Increase these numbers to
                                         trust sensor readings from encoders
                                         and gyros less. This matrix is in the form
                                         [theta], with units in radians.
        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        :param nominalDt:                The time in seconds between each robot
                                         loop.
        """
    @typing.overload
    def addVisionMeasurement(self, visionRobotPose: wpimath.geometry._geometry.Pose2d, timestamp: seconds) -> None: 
        """
        Add a vision measurement to the Unscented Kalman Filter. This will correct
        the odometry pose estimate while still accounting for measurement noise.

        This method can be called as infrequently as you want, as long as you are
        calling Update() every loop.

        :param visionRobotPose: The pose of the robot as measured by the vision
                                camera.
        :param timestamp:       The timestamp of the vision measurement in seconds.
                                Note that if you don't use your own time source by
                                calling UpdateWithTime() then you must use a
                                timestamp with an epoch since FPGA startup
                                (i.e. the epoch of this timestamp is the same
                                epoch as Timer#GetFPGATimestamp.) This means
                                that you should use Timer#GetFPGATimestamp as your
                                time source or sync the epochs.

        Adds a vision measurement to the Unscented Kalman Filter. This will correct
        the odometry pose estimate while still accounting for measurement noise.

        This method can be called as infrequently as you want, as long as you are
        calling Update() every loop.

        Note that the vision measurement standard deviations passed into this
        method will continue to apply to future measurements until a subsequent
        call to SetVisionMeasurementStdDevs() or this method.

        :param visionRobotPose:          The pose of the robot as measured by the
                                         vision camera.
        :param timestamp:                The timestamp of the vision measurement in
                                         seconds. Note that if you don't use your
                                         own time source by calling
                                         UpdateWithTime(), then you must use a
                                         timestamp with an epoch since FPGA startup
                                         (i.e. the epoch of this timestamp is the
                                         same epoch as
                                         frc::Timer::GetFPGATimestamp(). This means
                                         that you should use
                                         frc::Timer::GetFPGATimestamp() as your
                                         time source in this case.
        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        """
    @typing.overload
    def addVisionMeasurement(self, visionRobotPose: wpimath.geometry._geometry.Pose2d, timestamp: seconds, visionMeasurementStdDevs: typing.Tuple[float, float, float]) -> None: ...
    def getEstimatedPosition(self) -> wpimath.geometry._geometry.Pose2d: 
        """
        Gets the pose of the robot at the current time as estimated by the Extended
        Kalman Filter.

        :returns: The estimated robot pose in meters.
        """
    def resetPosition(self, pose: wpimath.geometry._geometry.Pose2d, gyroAngle: wpimath.geometry._geometry.Rotation2d) -> None: 
        """
        Resets the robot's position on the field.

        You NEED to reset your encoders (to zero) when calling this method.

        The gyroscope angle does not need to be reset in the user's robot code.
        The library automatically takes care of offsetting the gyro angle.

        :param pose:      The position on the field that your robot is at.
        :param gyroAngle: The angle reported by the gyroscope.
        """
    def setVisionMeasurementStdDevs(self, visionMeasurementStdDevs: typing.Tuple[float, float, float]) -> None: 
        """
        Sets the pose estimator's trust of global measurements. This might be used
        to change trust in vision measurements after the autonomous period, or to
        change trust as distance to a vision target increases.

        :param visionMeasurementStdDevs: Standard deviations of the vision
                                         measurements. Increase these numbers to
                                         trust global measurements from vision
                                         less. This matrix is in the form
                                         [x, y, theta]ᵀ, with units in meters and
                                         radians.
        """
    def update(self, arg0: wpimath.geometry._geometry.Rotation2d, arg1: wpimath.kinematics._kinematics.SwerveModuleState, arg2: wpimath.kinematics._kinematics.SwerveModuleState, arg3: wpimath.kinematics._kinematics.SwerveModuleState, arg4: wpimath.kinematics._kinematics.SwerveModuleState, arg5: wpimath.kinematics._kinematics.SwerveModuleState, arg6: wpimath.kinematics._kinematics.SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the the Unscented Kalman Filter using only wheel encoder
        information. This should be called every loop, and the correct loop period
        must be passed into the constructor of this class.

        :param gyroAngle:    The current gyro angle.
        :param moduleStates: The current velocities and rotations of the swerve
                             modules.

        :returns: The estimated pose of the robot in meters.
        """
    def updateWithTime(self, arg0: seconds, arg1: wpimath.geometry._geometry.Rotation2d, arg2: wpimath.kinematics._kinematics.SwerveModuleState, arg3: wpimath.kinematics._kinematics.SwerveModuleState, arg4: wpimath.kinematics._kinematics.SwerveModuleState, arg5: wpimath.kinematics._kinematics.SwerveModuleState, arg6: wpimath.kinematics._kinematics.SwerveModuleState, arg7: wpimath.kinematics._kinematics.SwerveModuleState) -> wpimath.geometry._geometry.Pose2d: 
        """
        Updates the the Unscented Kalman Filter using only wheel encoder
        information. This should be called every loop, and the correct loop period
        must be passed into the constructor of this class.

        :param currentTime:  Time at which this method was called, in seconds.
        :param gyroAngle:    The current gyroscope angle.
        :param moduleStates: The current velocities and rotations of the swerve
                             modules.

        :returns: The estimated pose of the robot in meters.
        """
    pass
