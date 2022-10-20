from __future__ import annotations
import wpimath._controls._controls.plant
import typing
import wpimath._controls._controls.system

__all__ = [
    "DCMotor",
    "LinearSystemId"
]


class DCMotor():
    """
    Holds the constants for a DC motor.
    """
    @staticmethod
    def CIM(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of CIM.
        """
    @staticmethod
    def NEO(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of NEO brushless motor.
        """
    @staticmethod
    def NEO550(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of NEO 550 brushless motor.
        """
    @staticmethod
    def RS775_125(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Andymark RS 775-125.
        """
    def __init__(self, nominalVoltage: volts, stallTorque: newton_meters, stallCurrent: amperes, freeCurrent: amperes, freeSpeed: radians_per_second, numMotors: int = 1) -> None: 
        """
        Constructs a DC motor.

        :param nominalVoltage: Voltage at which the motor constants were measured.
        :param stallTorque:    Torque when stalled.
        :param stallCurrent:   Current draw when stalled.
        :param freeCurrent:    Current draw under no load.
        :param freeSpeed:      Angular velocity under no load.
        :param numMotors:      Number of motors in a gearbox.
        """
    @staticmethod
    def andymark9015(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Andymark 9015.
        """
    @staticmethod
    def bag(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Bag motor.
        """
    @staticmethod
    def banebotsRS550(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Banebots RS 550.
        """
    @staticmethod
    def banebotsRS775(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Banebots RS 775.
        """
    def current(self, speed: radians_per_second, inputVoltage: volts) -> amperes: 
        """
        Returns current drawn by motor with given speed and input voltage.

        :param speed:        The current angular velocity of the motor.
        :param inputVoltage: The voltage being applied to the motor.
        """
    @staticmethod
    def falcon500(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Falcon 500 brushless motor.
        """
    @staticmethod
    def miniCIM(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of MiniCIM.
        """
    @staticmethod
    def romiBuiltIn(numMotors: int = 1) -> DCMotor: 
        """
        Return a gearbox of Romi/TI_RSLK MAX motors.
        """
    @staticmethod
    def vex775Pro(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Vex 775 Pro.
        """
    @property
    def Kt(self) -> volt_seconds:
        """
        :type: volt_seconds
        """
    @property
    def Kv(self) -> radians_per_second_per_volt:
        """
        :type: radians_per_second_per_volt
        """
    @property
    def R(self) -> ohms:
        """
        :type: ohms
        """
    @property
    def freeCurrent(self) -> amperes:
        """
        :type: amperes
        """
    @property
    def freeSpeed(self) -> radians_per_second:
        """
        :type: radians_per_second
        """
    @property
    def nominalVoltage(self) -> volts:
        """
        :type: volts
        """
    @property
    def stallCurrent(self) -> amperes:
        """
        :type: amperes
        """
    @property
    def stallTorque(self) -> newton_meters:
        """
        :type: newton_meters
        """
    pass
class LinearSystemId():
    @staticmethod
    def DCMotorSystem(motor: DCMotor, J: kilogram_square_meters, G: float) -> wpimath._controls._controls.system.LinearSystem_2_1_2: 
        """
        Constructs the state-space model for a DC motor motor.

        States: [[angular position, angular velocity]]
        Inputs: [[voltage]]
        Outputs: [[angular position, angular velocity]]

        :param motor: Instance of DCMotor.
        :param J:     Moment of inertia.
        :param G:     Gear ratio from motor to carriage.
                      @throws std::domain_error if J <= 0 or G <= 0.
        """
    def __init__(self) -> None: ...
    @staticmethod
    def drivetrainVelocitySystem(motor: DCMotor, m: kilograms, r: meters, rb: meters, J: kilogram_square_meters, G: float) -> wpimath._controls._controls.system.LinearSystem_2_2_2: 
        """
        Constructs the state-space model for a drivetrain.

        States: [[left velocity], [right velocity]]
        Inputs: [[left voltage], [right voltage]]
        Outputs: [[left velocity], [right velocity]]

        :param motor: Instance of DCMotor.
        :param m:     Drivetrain mass.
        :param r:     Wheel radius.
        :param rb:    Robot radius.
        :param J:     Moment of inertia.
        :param G:     Gear ratio from motor to wheel.
                      @throws std::domain_error if m <= 0, r <= 0, rb <= 0, J <= 0, or
                      G <= 0.
        """
    @staticmethod
    def elevatorSystem(motor: DCMotor, m: kilograms, r: meters, G: float) -> wpimath._controls._controls.system.LinearSystem_2_1_1: 
        """
        Constructs the state-space model for an elevator.

        States: [[position], [velocity]]
        Inputs: [[voltage]]
        Outputs: [[position]]

        :param motor: Instance of DCMotor.
        :param m:     Carriage mass.
        :param r:     Pulley radius.
        :param G:     Gear ratio from motor to carriage.
                      @throws std::domain_error if m <= 0, r <= 0, or G <= 0.
        """
    @staticmethod
    def flywheelSystem(motor: DCMotor, J: kilogram_square_meters, G: float) -> wpimath._controls._controls.system.LinearSystem_1_1_1: 
        """
        Constructs the state-space model for a flywheel.

        States: [[angular velocity]]
        Inputs: [[voltage]]
        Outputs: [[angular velocity]]

        :param motor: Instance of DCMotor.
        :param J:     Moment of inertia.
        :param G:     Gear ratio from motor to carriage.
                      @throws std::domain_error if J <= 0 or G <= 0.
        """
    @staticmethod
    @typing.overload
    def identifyDrivetrainSystem(kVlinear: volt_seconds_per_meter, kAlinear: volt_seconds_squared_per_meter, kVangular: volt_seconds_per_meter, kAangular: volt_seconds_squared_per_meter) -> wpimath._controls._controls.system.LinearSystem_2_2_2: 
        """
        Constructs the state-space model for a 2 DOF drivetrain velocity system
        from system identification data.

        States: [[left velocity], [right velocity]]
        Inputs: [[left voltage], [right voltage]]
        Outputs: [[left velocity], [right velocity]]

        :param kVlinear:  The linear velocity gain in volts per (meter per second).
        :param kAlinear:  The linear acceleration gain in volts per (meter per
                          second squared).
        :param kVangular: The angular velocity gain in volts per (meter per second).
        :param kAangular: The angular acceleration gain in volts per (meter per
                          second squared).
                          @throws domain_error if kVlinear <= 0, kAlinear <= 0, kVangular <= 0,
                          or kAangular <= 0.

        Constructs the state-space model for a 2 DOF drivetrain velocity system
        from system identification data.

        States: [[left velocity], [right velocity]]
        Inputs: [[left voltage], [right voltage]]
        Outputs: [[left velocity], [right velocity]]

        :param kVlinear:   The linear velocity gain in volts per (meter per second).
        :param kAlinear:   The linear acceleration gain in volts per (meter per
                           second squared).
        :param kVangular:  The angular velocity gain in volts per (radian per
                           second).
        :param kAangular:  The angular acceleration gain in volts per (radian per
                           second squared).
        :param trackwidth: The width of the drivetrain.
                           @throws domain_error if kVlinear <= 0, kAlinear <= 0, kVangular <= 0,
                           kAangular <= 0, or trackwidth <= 0.
        """
    @staticmethod
    @typing.overload
    def identifyDrivetrainSystem(kVlinear: volt_seconds_per_meter, kAlinear: volt_seconds_squared_per_meter, kVangular: volt_seconds_per_radian, kAangular: volt_seconds_squared_per_radian, trackwidth: meters) -> wpimath._controls._controls.system.LinearSystem_2_2_2: ...
    @staticmethod
    def identifyPositionSystemMeters(kV: volt_seconds_per_meter, kA: volt_seconds_squared_per_meter) -> wpimath._controls._controls.system.LinearSystem_2_1_1: 
        """
        Constructs the state-space model for a 1 DOF position system from system
        identification data.

        You MUST use an SI unit (i.e. meters or radians) for the Distance template
        argument. You may still use non-SI units (such as feet or inches) for the
        actual method arguments; they will automatically be converted to SI
        internally.

        States: [[position], [velocity]]
        Inputs: [[voltage]]
        Outputs: [[position]]

        The parameters provided by the user are from this feedforward model:

        u = K_v v + K_a a

        :param kV: The velocity gain, in volt seconds per distance.
        :param kA: The acceleration gain, in volt seconds^2 per distance.
                   @throws std::domain_error if kV <= 0 or kA <= 0.
        """
    @staticmethod
    def identifyPositionSystemRadians(kV: volt_seconds_per_radian, kA: volt_seconds_squared_per_radian) -> wpimath._controls._controls.system.LinearSystem_2_1_1: ...
    @staticmethod
    def identifyVelocitySystemMeters(kV: volt_seconds_per_meter, kA: volt_seconds_squared_per_meter) -> wpimath._controls._controls.system.LinearSystem_1_1_1: 
        """
        Constructs the state-space model for a 1 DOF velocity-only system from
        system identification data.

        You MUST use an SI unit (i.e. meters or radians) for the Distance template
        argument. You may still use non-SI units (such as feet or inches) for the
        actual method arguments; they will automatically be converted to SI
        internally.

        States: [[velocity]]
        Inputs: [[voltage]]
        Outputs: [[velocity]]

        The parameters provided by the user are from this feedforward model:

        u = K_v v + K_a a

        :param kV: The velocity gain, in volt seconds per distance.
        :param kA: The acceleration gain, in volt seconds^2 per distance.
                   @throws std::domain_error if kV <= 0 or kA <= 0.
        """
    @staticmethod
    def identifyVelocitySystemRadians(kV: volt_seconds_per_radian, kA: volt_seconds_squared_per_radian) -> wpimath._controls._controls.system.LinearSystem_1_1_1: ...
    @staticmethod
    def singleJointedArmSystem(motor: DCMotor, J: kilogram_square_meters, G: float) -> wpimath._controls._controls.system.LinearSystem_2_1_1: 
        """
        Constructs the state-space model for a single-jointed arm.

        States: [[angle], [angular velocity]]
        Inputs: [[voltage]]
        Outputs: [[angle]]

        :param motor: Instance of DCMotor.
        :param J:     Moment of inertia.
        :param G:     Gear ratio from motor to carriage.
                      @throws std::domain_error if J <= 0 or G <= 0.
        """
    pass
