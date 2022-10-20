from __future__ import annotations
import wpimath._controls._controls.controller
import typing
import wpimath._controls._controls.system
import wpimath.geometry._geometry
import wpimath.kinematics._kinematics
import wpiutil._wpiutil

__all__ = [
    "ArmFeedforward",
    "BangBangController",
    "ControlAffinePlantInversionFeedforward_1_1",
    "ControlAffinePlantInversionFeedforward_2_1",
    "ControlAffinePlantInversionFeedforward_2_2",
    "ElevatorFeedforward",
    "HolonomicDriveController",
    "LinearPlantInversionFeedforward_1_1",
    "LinearPlantInversionFeedforward_2_1",
    "LinearPlantInversionFeedforward_2_2",
    "LinearQuadraticRegulator_1_1",
    "LinearQuadraticRegulator_2_1",
    "LinearQuadraticRegulator_2_2",
    "PIDController",
    "ProfiledPIDController",
    "ProfiledPIDControllerRadians",
    "RamseteController",
    "SimpleMotorFeedforwardMeters"
]


class ArmFeedforward():
    """
    A helper class that computes feedforward outputs for a simple arm (modeled as
    a motor acting against the force of gravity on a beam suspended at an angle).
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates a new ArmFeedforward with the specified gains.

        :param kS: The static gain, in volts.
        :param kG: The gravity gain, in volts.
        :param kV: The velocity gain, in volt seconds per radian.
        :param kA: The acceleration gain, in volt seconds^2 per radian.
        """
    @typing.overload
    def __init__(self, kS: volts, kG: volts, kV: volt_seconds_per_radian, kA: volt_seconds_squared_per_radian = 0.0) -> None: ...
    def calculate(self, angle: radians, velocity: radians_per_second, acceleration: radians_per_second_squared = 0.0) -> volts: 
        """
        Calculates the feedforward from the gains and setpoints.

        :param angle:        The angle setpoint, in radians.
        :param velocity:     The velocity setpoint, in radians per second.
        :param acceleration: The acceleration setpoint, in radians per second^2.

        :returns: The computed feedforward, in volts.
        """
    def maxAchievableAcceleration(self, maxVoltage: volts, angle: radians, velocity: radians_per_second) -> radians_per_second_squared: 
        """
        Calculates the maximum achievable acceleration given a maximum voltage
        supply, a position, and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the arm.
        :param angle:      The angle of the arm
        :param velocity:   The velocity of the arm.

        :returns: The maximum possible acceleration at the given velocity and angle.
        """
    def maxAchievableVelocity(self, maxVoltage: volts, angle: radians, acceleration: radians_per_second_squared) -> radians_per_second: 
        """
        Calculates the maximum achievable velocity given a maximum voltage supply,
        a position, and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the arm.
        :param angle:        The angle of the arm
        :param acceleration: The acceleration of the arm.

        :returns: The maximum possible velocity at the given acceleration and angle.
        """
    def minAchievableAcceleration(self, maxVoltage: volts, angle: radians, velocity: radians_per_second) -> radians_per_second_squared: 
        """
        Calculates the minimum achievable acceleration given a maximum voltage
        supply, a position, and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the arm.
        :param angle:      The angle of the arm
        :param velocity:   The velocity of the arm.

        :returns: The minimum possible acceleration at the given velocity and angle.
        """
    def minAchievableVelocity(self, maxVoltage: volts, angle: radians, acceleration: radians_per_second_squared) -> radians_per_second: 
        """
        Calculates the minimum achievable velocity given a maximum voltage supply,
        a position, and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the arm.
        :param angle:        The angle of the arm
        :param acceleration: The acceleration of the arm.

        :returns: The minimum possible velocity at the given acceleration and angle.
        """
    @property
    def kA(self) -> volt_seconds_squared_per_radian:
        """
        :type: volt_seconds_squared_per_radian
        """
    @kA.setter
    def kA(self, arg0: volt_seconds_squared_per_radian) -> None:
        pass
    @property
    def kG(self) -> volts:
        """
        :type: volts
        """
    @kG.setter
    def kG(self, arg0: volts) -> None:
        pass
    @property
    def kS(self) -> volts:
        """
        :type: volts
        """
    @kS.setter
    def kS(self, arg0: volts) -> None:
        pass
    @property
    def kV(self) -> volt_seconds_per_radian:
        """
        :type: volt_seconds_per_radian
        """
    @kV.setter
    def kV(self, arg0: volt_seconds_per_radian) -> None:
        pass
    pass
class BangBangController(wpiutil._wpiutil.Sendable):
    """
    Implements a bang-bang controller, which outputs either 0 or 1 depending on
    whether the measurement is less than the setpoint. This maximally-aggressive
    control approach works very well for velocity control of high-inertia
    mechanisms, and poorly on most other things.

    Note that this is an *asymmetric* bang-bang controller - it will not exert
    any control effort in the reverse direction (e.g. it won't try to slow down
    an over-speeding shooter wheel). This asymmetry is *extremely important.*
    Bang-bang control is extremely simple, but also potentially hazardous. Always
    ensure that your motor controllers are set to "coast" before attempting to
    control them with a bang-bang controller.
    """
    def __init__(self, tolerance: float = inf) -> None: 
        """
        Creates a new bang-bang controller.

        Always ensure that your motor controllers are set to "coast" before
        attempting to control them with a bang-bang controller.

        :param tolerance: Tolerance for atSetpoint.
        """
    def atSetpoint(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the setpoint.

        :returns: Whether the error is within the acceptable bounds.
        """
    @typing.overload
    def calculate(self, measurement: float) -> float: 
        """
        Returns the calculated control output.

        Always ensure that your motor controllers are set to "coast" before
        attempting to control them with a bang-bang controller.

        :param measurement: The most recent measurement of the process variable.
        :param setpoint:    The setpoint for the process variable.

        :returns: The calculated motor output (0 or 1).

        Returns the calculated control output.

        :param measurement: The most recent measurement of the process variable.

        :returns: The calculated motor output (0 or 1).
        """
    @typing.overload
    def calculate(self, measurement: float, setpoint: float) -> float: ...
    def getError(self) -> float: 
        """
        Returns the current error.

        :returns: The current error.
        """
    def getMeasurement(self) -> float: 
        """
        Returns the current measurement of the process variable.

        :returns: The current measurement of the process variable.
        """
    def getSetpoint(self) -> float: 
        """
        Returns the current setpoint of the bang-bang controller.

        :returns: The current setpoint.
        """
    def getTolerance(self) -> float: 
        """
        Returns the current tolerance of the controller.

        :returns: The current tolerance.
        """
    def initSendable(self, builder: wpiutil._wpiutil.SendableBuilder) -> None: ...
    def setSetpoint(self, setpoint: float) -> None: 
        """
        Sets the setpoint for the bang-bang controller.

        :param setpoint: The desired setpoint.
        """
    def setTolerance(self, tolerance: float) -> None: 
        """
        Sets the error within which AtSetpoint will return true.

        :param tolerance: Position error which is tolerable.
        """
    pass
class ControlAffinePlantInversionFeedforward_1_1():
    """
    Constructs a control-affine plant inversion model-based feedforward from
    given model dynamics.

    If given the vector valued function as f(x, u) where x is the state
    vector and u is the input vector, the B matrix(continuous input matrix)
    is calculated through a NumericalJacobian. In this case f has to be
    control-affine (of the form f(x) + Bu).

    The feedforward is calculated as
    :strong:` u_ff = B:sup:`+` (rDot - f(x)) `, where :strong:`
    B:sup:`+` ` is the pseudoinverse of B.

    This feedforward does not account for a dynamic B matrix, B is either
    determined or supplied when the feedforward is created and remains constant.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States The number of states.
    @tparam Inputs the number of inputs.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[1, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], dt: seconds) -> None: 
        """
        Constructs a feedforward with given model dynamics as a function
        of state and input.

        :param f:  A vector-valued function of x, the state, and
                   u, the input, that returns the derivative of
                   the state vector. HAS to be control-affine
                   (of the form f(x) + Bu).
        :param dt: The timestep between calls of calculate().

        Constructs a feedforward with given model dynamics as a function of state,
        and the plant's B matrix(continuous input matrix).

        :param f:  A vector-valued function of x, the state,
                   that returns the derivative of the state vector.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: The timestep between calls of calculate().
        """
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one set using
        Reset(const Eigen::Vector<double, States>&). If the initial state is not
        set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[1, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param i: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class ControlAffinePlantInversionFeedforward_2_1():
    """
    Constructs a control-affine plant inversion model-based feedforward from
    given model dynamics.

    If given the vector valued function as f(x, u) where x is the state
    vector and u is the input vector, the B matrix(continuous input matrix)
    is calculated through a NumericalJacobian. In this case f has to be
    control-affine (of the form f(x) + Bu).

    The feedforward is calculated as
    :strong:` u_ff = B:sup:`+` (rDot - f(x)) `, where :strong:`
    B:sup:`+` ` is the pseudoinverse of B.

    This feedforward does not account for a dynamic B matrix, B is either
    determined or supplied when the feedforward is created and remains constant.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States The number of states.
    @tparam Inputs the number of inputs.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], dt: seconds) -> None: 
        """
        Constructs a feedforward with given model dynamics as a function
        of state and input.

        :param f:  A vector-valued function of x, the state, and
                   u, the input, that returns the derivative of
                   the state vector. HAS to be control-affine
                   (of the form f(x) + Bu).
        :param dt: The timestep between calls of calculate().

        Constructs a feedforward with given model dynamics as a function of state,
        and the plant's B matrix(continuous input matrix).

        :param f:  A vector-valued function of x, the state,
                   that returns the derivative of the state vector.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: The timestep between calls of calculate().
        """
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], dt: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one set using
        Reset(const Eigen::Vector<double, States>&). If the initial state is not
        set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param i: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class ControlAffinePlantInversionFeedforward_2_2():
    """
    Constructs a control-affine plant inversion model-based feedforward from
    given model dynamics.

    If given the vector valued function as f(x, u) where x is the state
    vector and u is the input vector, the B matrix(continuous input matrix)
    is calculated through a NumericalJacobian. In this case f has to be
    control-affine (of the form f(x) + Bu).

    The feedforward is calculated as
    :strong:` u_ff = B:sup:`+` (rDot - f(x)) `, where :strong:`
    B:sup:`+` ` is the pseudoinverse of B.

    This feedforward does not account for a dynamic B matrix, B is either
    determined or supplied when the feedforward is created and remains constant.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States The number of states.
    @tparam Inputs the number of inputs.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], dt: seconds) -> None: 
        """
        Constructs a feedforward with given model dynamics as a function
        of state and input.

        :param f:  A vector-valued function of x, the state, and
                   u, the input, that returns the derivative of
                   the state vector. HAS to be control-affine
                   (of the form f(x) + Bu).
        :param dt: The timestep between calls of calculate().

        Constructs a feedforward with given model dynamics as a function of state,
        and the plant's B matrix(continuous input matrix).

        :param f:  A vector-valued function of x, the state,
                   that returns the derivative of the state vector.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: The timestep between calls of calculate().
        """
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], dt: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one set using
        Reset(const Eigen::Vector<double, States>&). If the initial state is not
        set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param i: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class ElevatorFeedforward():
    """
    A helper class that computes feedforward outputs for a simple elevator
    (modeled as a motor acting against the force of gravity).
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates a new ElevatorFeedforward with the specified gains.

        :param kS: The static gain, in volts.
        :param kG: The gravity gain, in volts.
        :param kV: The velocity gain, in volt seconds per distance.
        :param kA: The acceleration gain, in volt seconds^2 per distance.
        """
    @typing.overload
    def __init__(self, kS: volts, kG: volts, kV: volt_seconds, kA: volt_seconds_squared = 0.0) -> None: ...
    def calculate(self, velocity: units_per_second, acceleration: units_per_second_squared = 0.0) -> volts: 
        """
        Calculates the feedforward from the gains and setpoints.

        :param velocity:     The velocity setpoint, in distance per second.
        :param acceleration: The acceleration setpoint, in distance per second^2.

        :returns: The computed feedforward, in volts.
        """
    def maxAchievableAcceleration(self, maxVoltage: volts, velocity: units_per_second) -> units_per_second_squared: 
        """
        Calculates the maximum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the elevator.
        :param velocity:   The velocity of the elevator.

        :returns: The maximum possible acceleration at the given velocity.
        """
    def maxAchievableVelocity(self, maxVoltage: volts, acceleration: units_per_second_squared) -> units_per_second: 
        """
        Calculates the maximum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the elevator.
        :param acceleration: The acceleration of the elevator.

        :returns: The maximum possible velocity at the given acceleration.
        """
    def minAchievableAcceleration(self, maxVoltage: volts, velocity: units_per_second) -> units_per_second_squared: 
        """
        Calculates the minimum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the elevator.
        :param velocity:   The velocity of the elevator.

        :returns: The minimum possible acceleration at the given velocity.
        """
    def minAchievableVelocity(self, maxVoltage: volts, acceleration: units_per_second_squared) -> units_per_second: 
        """
        Calculates the minimum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the elevator.
        :param acceleration: The acceleration of the elevator.

        :returns: The minimum possible velocity at the given acceleration.
        """
    @property
    def kA(self) -> volt_seconds_squared:
        """
        :type: volt_seconds_squared
        """
    @kA.setter
    def kA(self, arg0: volt_seconds_squared) -> None:
        pass
    @property
    def kG(self) -> volts:
        """
        :type: volts
        """
    @kG.setter
    def kG(self, arg0: volts) -> None:
        pass
    @property
    def kS(self) -> volts:
        """
        :type: volts
        """
    @kS.setter
    def kS(self, arg0: volts) -> None:
        pass
    @property
    def kV(self) -> volt_seconds:
        """
        :type: volt_seconds
        """
    @kV.setter
    def kV(self, arg0: volt_seconds) -> None:
        pass
    pass
class HolonomicDriveController():
    """
    This holonomic drive controller can be used to follow trajectories using a
    holonomic drivetrain (i.e. swerve or mecanum). Holonomic trajectory following
    is a much simpler problem to solve compared to skid-steer style drivetrains
    because it is possible to individually control forward, sideways, and angular
    velocity.

    The holonomic drive controller takes in one PID controller for each
    direction, forward and sideways, and one profiled PID controller for the
    angular direction. Because the heading dynamics are decoupled from
    translations, users can specify a custom heading that the drivetrain should
    point toward. This heading reference is profiled for smoothness.
    """
    def __init__(self, xController: PIDController, yController: PIDController, thetaController: ProfiledPIDControllerRadians) -> None: 
        """
        Constructs a holonomic drive controller.

        :param xController:     A PID Controller to respond to error in the
                                field-relative x direction.
        :param yController:     A PID Controller to respond to error in the
                                field-relative y direction.
        :param thetaController: A profiled PID controller to respond to error in
                                angle.
        """
    def atReference(self) -> bool: 
        """
        Returns true if the pose error is within tolerance of the reference.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, desiredState: wpimath._controls._controls.trajectory.Trajectory.State, angleRef: wpimath.geometry._geometry.Rotation2d) -> wpimath.kinematics._kinematics.ChassisSpeeds: 
        """
        Returns the next output of the holonomic drive controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:       The current pose.
        :param poseRef:           The desired pose.
        :param linearVelocityRef: The desired linear velocity.
        :param angleRef:          The desired ending angle.

        Returns the next output of the holonomic drive controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:  The current pose.
        :param desiredState: The desired pose, linear velocity, and angular velocity
                             from a trajectory.
        :param angleRef:     The desired ending angle.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, poseRef: wpimath.geometry._geometry.Pose2d, linearVelocityRef: meters_per_second, angleRef: wpimath.geometry._geometry.Rotation2d) -> wpimath.kinematics._kinematics.ChassisSpeeds: ...
    def setEnabled(self, enabled: bool) -> None: 
        """
        Enables and disables the controller for troubleshooting purposes. When
        Calculate() is called on a disabled controller, only feedforward values
        are returned.

        :param enabled: If the controller is enabled or not.
        """
    def setTolerance(self, tolerance: wpimath.geometry._geometry.Pose2d) -> None: 
        """
        Sets the pose error which is considered tolerable for use with
        AtReference().

        :param tolerance: Pose error which is tolerable.
        """
    pass
class LinearPlantInversionFeedforward_1_1():
    """
    Constructs a plant inversion model-based feedforward from a LinearSystem.

    The feedforward is calculated as :strong:` u_ff = B:sup:`+` (r_k+1 - A
    r_k) `, where :strong:` B:sup:`+` ` is the pseudoinverse
    of B.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States The number of states.
    @tparam Inputs The number of inputs.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[1, 1]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: 
        """
        Constructs a feedforward with the given coefficients.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: Discretization timestep.
        """
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_1_1_1, arg1: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_1_1_2, arg1: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one set using
        Reset(const Eigen::Vector<double, States>&). If the initial state is not
        set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[1, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param i: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class LinearPlantInversionFeedforward_2_1():
    """
    Constructs a plant inversion model-based feedforward from a LinearSystem.

    The feedforward is calculated as :strong:` u_ff = B:sup:`+` (r_k+1 - A
    r_k) `, where :strong:` B:sup:`+` ` is the pseudoinverse
    of B.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States The number of states.
    @tparam Inputs The number of inputs.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], dt: seconds) -> None: 
        """
        Constructs a feedforward with the given coefficients.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: Discretization timestep.
        """
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_1_1, arg1: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_1_2, arg1: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one set using
        Reset(const Eigen::Vector<double, States>&). If the initial state is not
        set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param i: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class LinearPlantInversionFeedforward_2_2():
    """
    Constructs a plant inversion model-based feedforward from a LinearSystem.

    The feedforward is calculated as :strong:` u_ff = B:sup:`+` (r_k+1 - A
    r_k) `, where :strong:` B:sup:`+` ` is the pseudoinverse
    of B.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.

    @tparam States The number of states.
    @tparam Inputs The number of inputs.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], dt: seconds) -> None: 
        """
        Constructs a feedforward with the given coefficients.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: Discretization timestep.
        """
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_2_1, arg1: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_2_2, arg1: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one set using
        Reset(const Eigen::Vector<double, States>&). If the initial state is not
        set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param i: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class LinearQuadraticRegulator_1_1():
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[1, 1]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], Q: numpy.ndarray[numpy.float64, _Shape[1, 1]], R: numpy.ndarray[numpy.float64, _Shape[1, 1]], N: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: 
        """
        Constructs a controller with the given coefficients and plant.

        :param A:      Continuous system matrix of the plant being controlled.
        :param B:      Continuous input matrix of the plant being controlled.
        :param Qelems: The maximum desired error tolerance for each state.
        :param Relems: The maximum desired control effort for each input.
        :param dt:     Discretization timestep.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param dt: Discretization timestep.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param N:  The state-input cross-term cost matrix.
        :param dt: Discretization timestep.
        """
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[1, 1]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], Q: numpy.ndarray[numpy.float64, _Shape[1, 1]], R: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[1, 1]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], Qelems: typing.Tuple[float], Relems: typing.Tuple[float], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_1_1_1, arg1: typing.Tuple[float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_1_1_2, arg1: typing.Tuple[float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    pass
class LinearQuadraticRegulator_2_1():
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], Q: numpy.ndarray[numpy.float64, _Shape[2, 2]], R: numpy.ndarray[numpy.float64, _Shape[1, 1]], N: numpy.ndarray[numpy.float64, _Shape[2, 1]], dt: seconds) -> None: 
        """
        Constructs a controller with the given coefficients and plant.

        :param A:      Continuous system matrix of the plant being controlled.
        :param B:      Continuous input matrix of the plant being controlled.
        :param Qelems: The maximum desired error tolerance for each state.
        :param Relems: The maximum desired control effort for each input.
        :param dt:     Discretization timestep.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param dt: Discretization timestep.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param N:  The state-input cross-term cost matrix.
        :param dt: Discretization timestep.
        """
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], Q: numpy.ndarray[numpy.float64, _Shape[2, 2]], R: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], Qelems: typing.Tuple[float, float], Relems: typing.Tuple[float], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_1_1, arg1: typing.Tuple[float, float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_1_2, arg1: typing.Tuple[float, float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    pass
class LinearQuadraticRegulator_2_2():
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], Q: numpy.ndarray[numpy.float64, _Shape[2, 2]], R: numpy.ndarray[numpy.float64, _Shape[2, 2]], N: numpy.ndarray[numpy.float64, _Shape[2, 2]], dt: seconds) -> None: 
        """
        Constructs a controller with the given coefficients and plant.

        :param A:      Continuous system matrix of the plant being controlled.
        :param B:      Continuous input matrix of the plant being controlled.
        :param Qelems: The maximum desired error tolerance for each state.
        :param Relems: The maximum desired control effort for each input.
        :param dt:     Discretization timestep.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param dt: Discretization timestep.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param N:  The state-input cross-term cost matrix.
        :param dt: Discretization timestep.
        """
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], Q: numpy.ndarray[numpy.float64, _Shape[2, 2]], R: numpy.ndarray[numpy.float64, _Shape[2, 2]], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], Qelems: typing.Tuple[float, float], Relems: typing.Tuple[float, float], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_2_1, arg1: typing.Tuple[float, float], arg2: typing.Tuple[float, float], arg3: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_2_2, arg1: typing.Tuple[float, float], arg2: typing.Tuple[float, float], arg3: seconds) -> None: ...
    pass
class PIDController(wpiutil._wpiutil.Sendable):
    """
    Implements a PID control loop.
    """
    def __init__(self, Kp: float, Ki: float, Kd: float, period: seconds = 0.02) -> None: 
        """
        Allocates a PIDController with the given constants for Kp, Ki, and Kd.

        :param Kp:     The proportional coefficient.
        :param Ki:     The integral coefficient.
        :param Kd:     The derivative coefficient.
        :param period: The period between controller updates in seconds. The
                       default is 20 milliseconds. Must be non-zero and positive.
        """
    def atSetpoint(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the setpoint.

        This will return false until at least one input value has been computed.
        """
    @typing.overload
    def calculate(self, measurement: float) -> float: 
        """
        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param setpoint:    The new setpoint of the controller.
        """
    @typing.overload
    def calculate(self, measurement: float, setpoint: float) -> float: ...
    def disableContinuousInput(self) -> None: 
        """
        Disables continuous input.
        """
    def enableContinuousInput(self, minimumInput: float, maximumInput: float) -> None: 
        """
        Enables continuous input.

        Rather then using the max and min input range as constraints, it considers
        them to be the same point and automatically calculates the shortest route
        to the setpoint.

        :param minimumInput: The minimum value expected from the input.
        :param maximumInput: The maximum value expected from the input.
        """
    def getD(self) -> float: 
        """
        Gets the differential coefficient.

        :returns: differential coefficient
        """
    def getI(self) -> float: 
        """
        Gets the integral coefficient.

        :returns: integral coefficient
        """
    def getP(self) -> float: 
        """
        Gets the proportional coefficient.

        :returns: proportional coefficient
        """
    def getPeriod(self) -> seconds: 
        """
        Gets the period of this controller.

        :returns: The period of the controller.
        """
    def getPositionError(self) -> float: 
        """
        Returns the difference between the setpoint and the measurement.
        """
    def getSetpoint(self) -> float: 
        """
        Returns the current setpoint of the PIDController.

        :returns: The current setpoint.
        """
    def getVelocityError(self) -> float: 
        """
        Returns the velocity error.
        """
    def initSendable(self, builder: wpiutil._wpiutil.SendableBuilder) -> None: ...
    def isContinuousInputEnabled(self) -> bool: 
        """
        Returns true if continuous input is enabled.
        """
    def reset(self) -> None: 
        """
        Reset the previous error, the integral term, and disable the controller.
        """
    def setD(self, Kd: float) -> None: 
        """
        Sets the differential coefficient of the PID controller gain.

        :param Kd: differential coefficient
        """
    def setI(self, Ki: float) -> None: 
        """
        Sets the integral coefficient of the PID controller gain.

        :param Ki: integral coefficient
        """
    def setIntegratorRange(self, minimumIntegral: float, maximumIntegral: float) -> None: 
        """
        Sets the minimum and maximum values for the integrator.

        When the cap is reached, the integrator value is added to the controller
        output rather than the integrator value times the integral gain.

        :param minimumIntegral: The minimum value of the integrator.
        :param maximumIntegral: The maximum value of the integrator.
        """
    def setP(self, Kp: float) -> None: 
        """
        Sets the proportional coefficient of the PID controller gain.

        :param Kp: proportional coefficient
        """
    def setPID(self, Kp: float, Ki: float, Kd: float) -> None: 
        """
        Sets the PID Controller gain parameters.

        Sets the proportional, integral, and differential coefficients.

        :param Kp: Proportional coefficient
        :param Ki: Integral coefficient
        :param Kd: Differential coefficient
        """
    def setSetpoint(self, setpoint: float) -> None: 
        """
        Sets the setpoint for the PIDController.

        :param setpoint: The desired setpoint.
        """
    def setTolerance(self, positionTolerance: float, velocityTolerance: float = inf) -> None: 
        """
        Sets the error which is considered tolerable for use with AtSetpoint().

        :param positionTolerance: Position error which is tolerable.
        :param velocityTolerance: Velocity error which is tolerable.
        """
    pass
class ProfiledPIDController(wpiutil._wpiutil.Sendable):
    """
    Implements a PID control loop whose setpoint is constrained by a trapezoid
    profile.
    """
    def __init__(self, Kp: float, Ki: float, Kd: float, constraints: wpimath._controls._controls.trajectory.TrapezoidProfile.Constraints, period: seconds = 0.02) -> None: 
        """
        Allocates a ProfiledPIDController with the given constants for Kp, Ki, and
        Kd. Users should call reset() when they first start running the controller
        to avoid unwanted behavior.

        :param Kp:          The proportional coefficient.
        :param Ki:          The integral coefficient.
        :param Kd:          The derivative coefficient.
        :param constraints: Velocity and acceleration constraints for goal.
        :param period:      The period between controller updates in seconds. The
                            default is 20 milliseconds.
        """
    def atGoal(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the error.

        This will return false until at least one input value has been computed.
        """
    def atSetpoint(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the error.

        Currently this just reports on target as the actual value passes through
        the setpoint. Ideally it should be based on being within the tolerance for
        some period of time.

        This will return false until at least one input value has been computed.
        """
    @typing.overload
    def calculate(self, measurement: float) -> float: 
        """
        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.
        :param constraints: Velocity and acceleration constraints for goal.
        """
    @typing.overload
    def calculate(self, measurement: float, goal: float) -> float: ...
    @typing.overload
    def calculate(self, measurement: float, goal: float, constraints: wpimath._controls._controls.trajectory.TrapezoidProfile.Constraints) -> float: ...
    @typing.overload
    def calculate(self, measurement: float, goal: wpimath._controls._controls.trajectory.TrapezoidProfile.State) -> float: ...
    def disableContinuousInput(self) -> None: 
        """
        Disables continuous input.
        """
    def enableContinuousInput(self, minimumInput: float, maximumInput: float) -> None: 
        """
        Enables continuous input.

        Rather then using the max and min input range as constraints, it considers
        them to be the same point and automatically calculates the shortest route
        to the setpoint.

        :param minimumInput: The minimum value expected from the input.
        :param maximumInput: The maximum value expected from the input.
        """
    def getD(self) -> float: 
        """
        Gets the differential coefficient.

        :returns: differential coefficient
        """
    def getGoal(self) -> wpimath._controls._controls.trajectory.TrapezoidProfile.State: 
        """
        Gets the goal for the ProfiledPIDController.
        """
    def getI(self) -> float: 
        """
        Gets the integral coefficient.

        :returns: integral coefficient
        """
    def getP(self) -> float: 
        """
        Gets the proportional coefficient.

        :returns: proportional coefficient
        """
    def getPeriod(self) -> seconds: 
        """
        Gets the period of this controller.

        :returns: The period of the controller.
        """
    def getPositionError(self) -> float: 
        """
        Returns the difference between the setpoint and the measurement.

        :returns: The error.
        """
    def getSetpoint(self) -> wpimath._controls._controls.trajectory.TrapezoidProfile.State: 
        """
        Returns the current setpoint of the ProfiledPIDController.

        :returns: The current setpoint.
        """
    def getVelocityError(self) -> units_per_second: 
        """
        Returns the change in error per second.
        """
    def initSendable(self, builder: wpiutil._wpiutil.SendableBuilder) -> None: ...
    @typing.overload
    def reset(self, measuredPosition: float) -> None: 
        """
        Reset the previous error and the integral term.

        :param measurement: The current measured State of the system.

        Reset the previous error and the integral term.

        :param measuredPosition: The current measured position of the system.
        :param measuredVelocity: The current measured velocity of the system.

        Reset the previous error and the integral term.

        :param measuredPosition: The current measured position of the system. The
                                 velocity is assumed to be zero.
        """
    @typing.overload
    def reset(self, measuredPosition: float, measuredVelocity: units_per_second) -> None: ...
    @typing.overload
    def reset(self, measurement: wpimath._controls._controls.trajectory.TrapezoidProfile.State) -> None: ...
    def setConstraints(self, constraints: wpimath._controls._controls.trajectory.TrapezoidProfile.Constraints) -> None: 
        """
        Set velocity and acceleration constraints for goal.

        :param constraints: Velocity and acceleration constraints for goal.
        """
    def setD(self, Kd: float) -> None: 
        """
        Sets the differential coefficient of the PID controller gain.

        :param Kd: differential coefficient
        """
    @typing.overload
    def setGoal(self, goal: float) -> None: 
        """
        Sets the goal for the ProfiledPIDController.

        :param goal: The desired unprofiled setpoint.

        Sets the goal for the ProfiledPIDController.

        :param goal: The desired unprofiled setpoint.
        """
    @typing.overload
    def setGoal(self, goal: wpimath._controls._controls.trajectory.TrapezoidProfile.State) -> None: ...
    def setI(self, Ki: float) -> None: 
        """
        Sets the integral coefficient of the PID controller gain.

        :param Ki: integral coefficient
        """
    def setIntegratorRange(self, minimumIntegral: float, maximumIntegral: float) -> None: 
        """
        Sets the minimum and maximum values for the integrator.

        When the cap is reached, the integrator value is added to the controller
        output rather than the integrator value times the integral gain.

        :param minimumIntegral: The minimum value of the integrator.
        :param maximumIntegral: The maximum value of the integrator.
        """
    def setP(self, Kp: float) -> None: 
        """
        Sets the proportional coefficient of the PID controller gain.

        :param Kp: proportional coefficient
        """
    def setPID(self, Kp: float, Ki: float, Kd: float) -> None: 
        """
        Sets the PID Controller gain parameters.

        Sets the proportional, integral, and differential coefficients.

        :param Kp: Proportional coefficient
        :param Ki: Integral coefficient
        :param Kd: Differential coefficient
        """
    def setTolerance(self, positionTolerance: float, velocityTolerance: units_per_second = inf) -> None: 
        """
        Sets the error which is considered tolerable for use with
        AtSetpoint().

        :param positionTolerance: Position error which is tolerable.
        :param velocityTolerance: Velocity error which is tolerable.
        """
    pass
class ProfiledPIDControllerRadians(wpiutil._wpiutil.Sendable):
    """
    Implements a PID control loop whose setpoint is constrained by a trapezoid
    profile.
    """
    def __init__(self, Kp: float, Ki: float, Kd: float, constraints: wpimath._controls._controls.trajectory.TrapezoidProfileRadians.Constraints, period: seconds = 0.02) -> None: 
        """
        Allocates a ProfiledPIDController with the given constants for Kp, Ki, and
        Kd. Users should call reset() when they first start running the controller
        to avoid unwanted behavior.

        :param Kp:          The proportional coefficient.
        :param Ki:          The integral coefficient.
        :param Kd:          The derivative coefficient.
        :param constraints: Velocity and acceleration constraints for goal.
        :param period:      The period between controller updates in seconds. The
                            default is 20 milliseconds.
        """
    def atGoal(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the error.

        This will return false until at least one input value has been computed.
        """
    def atSetpoint(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the error.

        Currently this just reports on target as the actual value passes through
        the setpoint. Ideally it should be based on being within the tolerance for
        some period of time.

        This will return false until at least one input value has been computed.
        """
    @typing.overload
    def calculate(self, measurement: radians) -> float: 
        """
        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.
        :param constraints: Velocity and acceleration constraints for goal.
        """
    @typing.overload
    def calculate(self, measurement: radians, goal: radians) -> float: ...
    @typing.overload
    def calculate(self, measurement: radians, goal: radians, constraints: wpimath._controls._controls.trajectory.TrapezoidProfileRadians.Constraints) -> float: ...
    @typing.overload
    def calculate(self, measurement: radians, goal: wpimath._controls._controls.trajectory.TrapezoidProfileRadians.State) -> float: ...
    def disableContinuousInput(self) -> None: 
        """
        Disables continuous input.
        """
    def enableContinuousInput(self, minimumInput: radians, maximumInput: radians) -> None: 
        """
        Enables continuous input.

        Rather then using the max and min input range as constraints, it considers
        them to be the same point and automatically calculates the shortest route
        to the setpoint.

        :param minimumInput: The minimum value expected from the input.
        :param maximumInput: The maximum value expected from the input.
        """
    def getD(self) -> float: 
        """
        Gets the differential coefficient.

        :returns: differential coefficient
        """
    def getGoal(self) -> wpimath._controls._controls.trajectory.TrapezoidProfileRadians.State: 
        """
        Gets the goal for the ProfiledPIDController.
        """
    def getI(self) -> float: 
        """
        Gets the integral coefficient.

        :returns: integral coefficient
        """
    def getP(self) -> float: 
        """
        Gets the proportional coefficient.

        :returns: proportional coefficient
        """
    def getPeriod(self) -> seconds: 
        """
        Gets the period of this controller.

        :returns: The period of the controller.
        """
    def getPositionError(self) -> radians: 
        """
        Returns the difference between the setpoint and the measurement.

        :returns: The error.
        """
    def getSetpoint(self) -> wpimath._controls._controls.trajectory.TrapezoidProfileRadians.State: 
        """
        Returns the current setpoint of the ProfiledPIDController.

        :returns: The current setpoint.
        """
    def getVelocityError(self) -> radians_per_second: 
        """
        Returns the change in error per second.
        """
    def initSendable(self, builder: wpiutil._wpiutil.SendableBuilder) -> None: ...
    @typing.overload
    def reset(self, measuredPosition: radians) -> None: 
        """
        Reset the previous error and the integral term.

        :param measurement: The current measured State of the system.

        Reset the previous error and the integral term.

        :param measuredPosition: The current measured position of the system.
        :param measuredVelocity: The current measured velocity of the system.

        Reset the previous error and the integral term.

        :param measuredPosition: The current measured position of the system. The
                                 velocity is assumed to be zero.
        """
    @typing.overload
    def reset(self, measuredPosition: radians, measuredVelocity: radians_per_second) -> None: ...
    @typing.overload
    def reset(self, measurement: wpimath._controls._controls.trajectory.TrapezoidProfileRadians.State) -> None: ...
    def setConstraints(self, constraints: wpimath._controls._controls.trajectory.TrapezoidProfileRadians.Constraints) -> None: 
        """
        Set velocity and acceleration constraints for goal.

        :param constraints: Velocity and acceleration constraints for goal.
        """
    def setD(self, Kd: float) -> None: 
        """
        Sets the differential coefficient of the PID controller gain.

        :param Kd: differential coefficient
        """
    @typing.overload
    def setGoal(self, goal: radians) -> None: 
        """
        Sets the goal for the ProfiledPIDController.

        :param goal: The desired unprofiled setpoint.

        Sets the goal for the ProfiledPIDController.

        :param goal: The desired unprofiled setpoint.
        """
    @typing.overload
    def setGoal(self, goal: wpimath._controls._controls.trajectory.TrapezoidProfileRadians.State) -> None: ...
    def setI(self, Ki: float) -> None: 
        """
        Sets the integral coefficient of the PID controller gain.

        :param Ki: integral coefficient
        """
    def setIntegratorRange(self, minimumIntegral: float, maximumIntegral: float) -> None: 
        """
        Sets the minimum and maximum values for the integrator.

        When the cap is reached, the integrator value is added to the controller
        output rather than the integrator value times the integral gain.

        :param minimumIntegral: The minimum value of the integrator.
        :param maximumIntegral: The maximum value of the integrator.
        """
    def setP(self, Kp: float) -> None: 
        """
        Sets the proportional coefficient of the PID controller gain.

        :param Kp: proportional coefficient
        """
    def setPID(self, Kp: float, Ki: float, Kd: float) -> None: 
        """
        Sets the PID Controller gain parameters.

        Sets the proportional, integral, and differential coefficients.

        :param Kp: Proportional coefficient
        :param Ki: Integral coefficient
        :param Kd: Differential coefficient
        """
    def setTolerance(self, positionTolerance: radians, velocityTolerance: radians_per_second = inf) -> None: 
        """
        Sets the error which is considered tolerable for use with
        AtSetpoint().

        :param positionTolerance: Position error which is tolerable.
        :param velocityTolerance: Velocity error which is tolerable.
        """
    pass
class RamseteController():
    """
    Ramsete is a nonlinear time-varying feedback controller for unicycle models
    that drives the model to a desired pose along a two-dimensional trajectory.
    Why would we need a nonlinear control law in addition to the linear ones we
    have used so far like PID? If we use the original approach with PID
    controllers for left and right position and velocity states, the controllers
    only deal with the local pose. If the robot deviates from the path, there is
    no way for the controllers to correct and the robot may not reach the desired
    global pose. This is due to multiple endpoints existing for the robot which
    have the same encoder path arc lengths.

    Instead of using wheel path arc lengths (which are in the robot's local
    coordinate frame), nonlinear controllers like pure pursuit and Ramsete use
    global pose. The controller uses this extra information to guide a linear
    reference tracker like the PID controllers back in by adjusting the
    references of the PID controllers.

    The paper "Control of Wheeled Mobile Robots: An Experimental Overview"
    describes a nonlinear controller for a wheeled vehicle with unicycle-like
    kinematics; a global pose consisting of x, y, and theta; and a desired pose
    consisting of x_d, y_d, and theta_d. We call it Ramsete because that's the
    acronym for the title of the book it came from in Italian ("Robotica
    Articolata e Mobile per i SErvizi e le TEcnologie").

    See <https://file.tavsys.net/control/controls-engineering-in-frc.pdf> section
    on Ramsete unicycle controller for a derivation and analysis.
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a Ramsete unicycle controller. The default arguments for
        b and zeta of 2.0 rad²/m² and 0.7 rad⁻¹ have been well-tested to produce
        desirable results.
        """
    @typing.overload
    def __init__(self, b: float, zeta: float) -> None: ...
    def atReference(self) -> bool: 
        """
        Returns true if the pose error is within tolerance of the reference.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, desiredState: wpimath._controls._controls.trajectory.Trajectory.State) -> wpimath.kinematics._kinematics.ChassisSpeeds: 
        """
        Returns the next output of the Ramsete controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:        The current pose.
        :param poseRef:            The desired pose.
        :param linearVelocityRef:  The desired linear velocity.
        :param angularVelocityRef: The desired angular velocity.

        Returns the next output of the Ramsete controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:  The current pose.
        :param desiredState: The desired pose, linear velocity, and angular velocity
                             from a trajectory.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, poseRef: wpimath.geometry._geometry.Pose2d, linearVelocityRef: meters_per_second, angularVelocityRef: radians_per_second) -> wpimath.kinematics._kinematics.ChassisSpeeds: ...
    def setEnabled(self, enabled: bool) -> None: 
        """
        Enables and disables the controller for troubleshooting purposes.

        :param enabled: If the controller is enabled or not.
        """
    def setTolerance(self, poseTolerance: wpimath.geometry._geometry.Pose2d) -> None: 
        """
        Sets the pose error which is considered tolerable for use with
        AtReference().

        :param poseTolerance: Pose error which is tolerable.
        """
    pass
class SimpleMotorFeedforwardMeters():
    """
    A helper class that computes feedforward voltages for a simple
    permanent-magnet DC motor.
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates a new SimpleMotorFeedforward with the specified gains.

        :param kS: The static gain, in volts.
        :param kV: The velocity gain, in volt seconds per distance.
        :param kA: The acceleration gain, in volt seconds^2 per distance.
        """
    @typing.overload
    def __init__(self, kS: volts, kV: volt_seconds_per_meter, kA: volt_seconds_squared_per_meter = 0.0) -> None: ...
    @typing.overload
    def calculate(self, currentVelocity: meters_per_second, nextVelocity: meters_per_second, dt: seconds) -> volts: 
        """
        Calculates the feedforward from the gains and setpoints.

        :param velocity:     The velocity setpoint, in distance per second.
        :param acceleration: The acceleration setpoint, in distance per second^2.

        :returns: The computed feedforward, in volts.

        Calculates the feedforward from the gains and setpoints.

        :param currentVelocity: The current velocity setpoint, in distance per
                                second.
        :param nextVelocity:    The next velocity setpoint, in distance per second.
        :param dt:              Time between velocity setpoints in seconds.

        :returns: The computed feedforward, in volts.
        """
    @typing.overload
    def calculate(self, velocity: meters_per_second, acceleration: meters_per_second_squared = 0.0) -> volts: ...
    def maxAchievableAcceleration(self, maxVoltage: volts, velocity: meters_per_second) -> meters_per_second_squared: 
        """
        Calculates the maximum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the motor.
        :param velocity:   The velocity of the motor.

        :returns: The maximum possible acceleration at the given velocity.
        """
    def maxAchievableVelocity(self, maxVoltage: volts, acceleration: meters_per_second_squared) -> meters_per_second: 
        """
        Calculates the maximum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the motor.
        :param acceleration: The acceleration of the motor.

        :returns: The maximum possible velocity at the given acceleration.
        """
    def minAchievableAcceleration(self, maxVoltage: volts, velocity: meters_per_second) -> meters_per_second_squared: 
        """
        Calculates the minimum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the motor.
        :param velocity:   The velocity of the motor.

        :returns: The minimum possible acceleration at the given velocity.
        """
    def minAchievableVelocity(self, maxVoltage: volts, acceleration: meters_per_second_squared) -> meters_per_second: 
        """
        Calculates the minimum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the motor.
        :param acceleration: The acceleration of the motor.

        :returns: The minimum possible velocity at the given acceleration.
        """
    @property
    def kA(self) -> volt_seconds_squared_per_meter:
        """
        :type: volt_seconds_squared_per_meter
        """
    @kA.setter
    def kA(self, arg0: volt_seconds_squared_per_meter) -> None:
        pass
    @property
    def kS(self) -> volts:
        """
        :type: volts
        """
    @kS.setter
    def kS(self, arg0: volts) -> None:
        pass
    @property
    def kV(self) -> volt_seconds_per_meter:
        """
        :type: volt_seconds_per_meter
        """
    @kV.setter
    def kV(self, arg0: volt_seconds_per_meter) -> None:
        pass
    pass
