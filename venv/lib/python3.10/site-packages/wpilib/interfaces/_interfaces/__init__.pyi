from __future__ import annotations
import wpilib.interfaces._interfaces
import typing
import wpimath.geometry._geometry

__all__ = [
    "Accelerometer",
    "CounterBase",
    "GenericHID",
    "Gyro",
    "MotorController",
    "SpeedController"
]


class Accelerometer():
    """
    Interface for 3-axis accelerometers.
    """
    class Range():
        """
        Members:

          kRange_2G

          kRange_4G

          kRange_8G

          kRange_16G
        """
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        __members__: dict # value = {'kRange_2G': <Range.kRange_2G: 0>, 'kRange_4G': <Range.kRange_4G: 1>, 'kRange_8G': <Range.kRange_8G: 2>, 'kRange_16G': <Range.kRange_16G: 3>}
        kRange_16G: wpilib.interfaces._interfaces.Accelerometer.Range # value = <Range.kRange_16G: 3>
        kRange_2G: wpilib.interfaces._interfaces.Accelerometer.Range # value = <Range.kRange_2G: 0>
        kRange_4G: wpilib.interfaces._interfaces.Accelerometer.Range # value = <Range.kRange_4G: 1>
        kRange_8G: wpilib.interfaces._interfaces.Accelerometer.Range # value = <Range.kRange_8G: 2>
        pass
    def __init__(self) -> None: ...
    def getX(self) -> float: 
        """
        Common interface for getting the x axis acceleration.

        :returns: The acceleration along the x axis in g-forces
        """
    def getY(self) -> float: 
        """
        Common interface for getting the y axis acceleration.

        :returns: The acceleration along the y axis in g-forces
        """
    def getZ(self) -> float: 
        """
        Common interface for getting the z axis acceleration.

        :returns: The acceleration along the z axis in g-forces
        """
    def setRange(self, range: Accelerometer.Range) -> None: 
        """
        Common interface for setting the measuring range of an accelerometer.

        :param range: The maximum acceleration, positive or negative, that the
                      accelerometer will measure. Not all accelerometers support all
                      ranges.
        """
    pass
class CounterBase():
    """
    Interface for counting the number of ticks on a digital input channel.

    Encoders, Gear tooth sensors, and counters should all subclass this so it can
    be used to build more advanced classes for control and driving.

    All counters will immediately start counting - Reset() them if you need them
    to be zeroed before use.
    """
    class EncodingType():
        """
        Members:

          k1X

          k2X

          k4X
        """
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        __members__: dict # value = {'k1X': <EncodingType.k1X: 0>, 'k2X': <EncodingType.k2X: 1>, 'k4X': <EncodingType.k4X: 2>}
        k1X: wpilib.interfaces._interfaces.CounterBase.EncodingType # value = <EncodingType.k1X: 0>
        k2X: wpilib.interfaces._interfaces.CounterBase.EncodingType # value = <EncodingType.k2X: 1>
        k4X: wpilib.interfaces._interfaces.CounterBase.EncodingType # value = <EncodingType.k4X: 2>
        pass
    def __init__(self) -> None: ...
    def get(self) -> int: ...
    def getDirection(self) -> bool: ...
    def getPeriod(self) -> seconds: ...
    def getStopped(self) -> bool: ...
    def reset(self) -> None: ...
    def setMaxPeriod(self, maxPeriod: seconds) -> None: ...
    pass
class GenericHID():
    """
    Handle input from standard HID devices connected to the Driver Station.

    This class handles standard input that comes from the Driver Station. Each
    time a value is requested the most recent value is returned. There is a
    single class instance for each device and the mapping of ports to hardware
    buttons depends on the code in the Driver Station.
    """
    class HIDType():
        """
        Members:

          kUnknown

          kXInputUnknown

          kXInputGamepad

          kXInputWheel

          kXInputArcadeStick

          kXInputFlightStick

          kXInputDancePad

          kXInputGuitar

          kXInputGuitar2

          kXInputDrumKit

          kXInputGuitar3

          kXInputArcadePad

          kHIDJoystick

          kHIDGamepad

          kHIDDriving

          kHIDFlight

          kHID1stPerson
        """
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        __members__: dict # value = {'kUnknown': <HIDType.kUnknown: -1>, 'kXInputUnknown': <HIDType.kXInputUnknown: 0>, 'kXInputGamepad': <HIDType.kXInputGamepad: 1>, 'kXInputWheel': <HIDType.kXInputWheel: 2>, 'kXInputArcadeStick': <HIDType.kXInputArcadeStick: 3>, 'kXInputFlightStick': <HIDType.kXInputFlightStick: 4>, 'kXInputDancePad': <HIDType.kXInputDancePad: 5>, 'kXInputGuitar': <HIDType.kXInputGuitar: 6>, 'kXInputGuitar2': <HIDType.kXInputGuitar2: 7>, 'kXInputDrumKit': <HIDType.kXInputDrumKit: 8>, 'kXInputGuitar3': <HIDType.kXInputGuitar3: 11>, 'kXInputArcadePad': <HIDType.kXInputArcadePad: 19>, 'kHIDJoystick': <HIDType.kHIDJoystick: 20>, 'kHIDGamepad': <HIDType.kHIDGamepad: 21>, 'kHIDDriving': <HIDType.kHIDDriving: 22>, 'kHIDFlight': <HIDType.kHIDFlight: 23>, 'kHID1stPerson': <HIDType.kHID1stPerson: 24>}
        kHID1stPerson: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kHID1stPerson: 24>
        kHIDDriving: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kHIDDriving: 22>
        kHIDFlight: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kHIDFlight: 23>
        kHIDGamepad: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kHIDGamepad: 21>
        kHIDJoystick: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kHIDJoystick: 20>
        kUnknown: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kUnknown: -1>
        kXInputArcadePad: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kXInputArcadePad: 19>
        kXInputArcadeStick: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kXInputArcadeStick: 3>
        kXInputDancePad: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kXInputDancePad: 5>
        kXInputDrumKit: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kXInputDrumKit: 8>
        kXInputFlightStick: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kXInputFlightStick: 4>
        kXInputGamepad: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kXInputGamepad: 1>
        kXInputGuitar: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kXInputGuitar: 6>
        kXInputGuitar2: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kXInputGuitar2: 7>
        kXInputGuitar3: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kXInputGuitar3: 11>
        kXInputUnknown: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kXInputUnknown: 0>
        kXInputWheel: wpilib.interfaces._interfaces.GenericHID.HIDType # value = <HIDType.kXInputWheel: 2>
        pass
    class RumbleType():
        """
        Members:

          kLeftRumble

          kRightRumble
        """
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        __members__: dict # value = {'kLeftRumble': <RumbleType.kLeftRumble: 0>, 'kRightRumble': <RumbleType.kRightRumble: 1>}
        kLeftRumble: wpilib.interfaces._interfaces.GenericHID.RumbleType # value = <RumbleType.kLeftRumble: 0>
        kRightRumble: wpilib.interfaces._interfaces.GenericHID.RumbleType # value = <RumbleType.kRightRumble: 1>
        pass
    def __init__(self, port: int) -> None: ...
    def __repr__(self) -> str: ...
    def getAxisCount(self) -> int: 
        """
        Get the number of axes for the HID.

        :returns: the number of axis for the current HID
        """
    def getAxisType(self, axis: int) -> int: 
        """
        Get the axis type of a joystick axis.

        :returns: the axis type of a joystick axis.
        """
    def getButtonCount(self) -> int: 
        """
        Get the number of buttons for the HID.

        :returns: the number of buttons on the current HID
        """
    def getName(self) -> str: 
        """
        Get the name of the HID.

        :returns: the name of the HID.
        """
    def getPOV(self, pov: int = 0) -> int: 
        """
        Get the angle in degrees of a POV on the HID.

        The POV angles start at 0 in the up direction, and increase clockwise
        (e.g. right is 90, upper-left is 315).

        :param pov: The index of the POV to read (starting at 0)

        :returns: the angle of the POV in degrees, or -1 if the POV is not pressed.
        """
    def getPOVCount(self) -> int: 
        """
        Get the number of POVs for the HID.

        :returns: the number of POVs for the current HID
        """
    def getPort(self) -> int: 
        """
        Get the port number of the HID.

        :returns: The port number of the HID.
        """
    def getRawAxis(self, axis: int) -> float: 
        """
        Get the value of the axis.

        :param axis: The axis to read, starting at 0.

        :returns: The value of the axis.
        """
    def getRawButton(self, button: int) -> bool: 
        """
        Get the button value (starting at button 1).

        The buttons are returned in a single 16 bit value with one bit representing
        the state of each button. The appropriate button is returned as a boolean
        value.

        This method returns true if the button is being held down at the time
        that this method is being called.

        :param button: The button number to be read (starting at 1)

        :returns: The state of the button.
        """
    def getRawButtonPressed(self, button: int) -> bool: 
        """
        Whether the button was pressed since the last check. %Button indexes begin
        at 1.

        This method returns true if the button went from not pressed to held down
        since the last time this method was called. This is useful if you only
        want to call a function once when you press the button.

        :param button: The button index, beginning at 1.

        :returns: Whether the button was pressed since the last check.
        """
    def getRawButtonReleased(self, button: int) -> bool: 
        """
        Whether the button was released since the last check. %Button indexes begin
        at 1.

        This method returns true if the button went from held down to not pressed
        since the last time this method was called. This is useful if you only
        want to call a function once when you release the button.

        :param button: The button index, beginning at 1.

        :returns: Whether the button was released since the last check.
        """
    def getType(self) -> GenericHID.HIDType: 
        """
        Get the type of the HID.

        :returns: the type of the HID.
        """
    def isConnected(self) -> bool: 
        """
        Get if the HID is connected.

        :returns: true if the HID is connected
        """
    def setOutput(self, outputNumber: int, value: bool) -> None: 
        """
        Set a single HID output value for the HID.

        :param outputNumber: The index of the output to set (1-32)
        :param value:        The value to set the output to
        """
    def setOutputs(self, value: int) -> None: 
        """
        Set all output values for the HID.

        :param value: The 32 bit output value (1 bit for each output)
        """
    def setRumble(self, type: GenericHID.RumbleType, value: float) -> None: 
        """
        Set the rumble output for the HID.

        The DS currently supports 2 rumble values, left rumble and right rumble.

        :param type:  Which rumble value to set
        :param value: The normalized value (0 to 1) to set the rumble to
        """
    pass
class Gyro():
    """
    Interface for yaw rate gyros.
    """
    def __init__(self) -> None: ...
    def calibrate(self) -> None: 
        """
        Calibrate the gyro. It's important to make sure that the robot is not
        moving while the calibration is in progress, this is typically
        done when the robot is first turned on while it's sitting at rest before
        the match starts.
        """
    def getAngle(self) -> float: 
        """
        Return the heading of the robot in degrees.

        The angle is continuous, that is it will continue from 360 to 361 degrees.
        This allows algorithms that wouldn't want to see a discontinuity in the
        gyro output as it sweeps past from 360 to 0 on the second time around.

        The angle is expected to increase as the gyro turns clockwise when looked
        at from the top. It needs to follow the NED axis convention.

        :returns: the current heading of the robot in degrees. This heading is based
                  on integration of the returned rate from the gyro.
        """
    def getRate(self) -> float: 
        """
        Return the rate of rotation of the gyro.

        The rate is based on the most recent reading of the gyro analog value.

        The rate is expected to be positive as the gyro turns clockwise when looked
        at from the top. It needs to follow the NED axis convention.

        :returns: the current rate in degrees per second
        """
    def getRotation2d(self) -> wpimath.geometry._geometry.Rotation2d: 
        """
        Return the heading of the robot as a Rotation2d.

        The angle is continuous, that is it will continue from 360 to 361 degrees.
        This allows algorithms that wouldn't want to see a discontinuity in the
        gyro output as it sweeps past from 360 to 0 on the second time around.

        The angle is expected to increase as the gyro turns counterclockwise when
        looked at from the top. It needs to follow the NWU axis convention.

        :returns: the current heading of the robot as a Rotation2d. This heading is
                  based on integration of the returned rate from the gyro.
        """
    def reset(self) -> None: 
        """
        Reset the gyro. Resets the gyro to a heading of zero. This can be used if
        there is significant drift in the gyro and it needs to be recalibrated
        after it has been running.
        """
    pass
class SpeedController():
    """
    Interface for speed controlling devices.

    :deprecated: Use MotorController.
    """
    def __init__(self) -> None: ...
    def disable(self) -> None: 
        """
        Common interface for disabling a motor.
        """
    def get(self) -> float: 
        """
        Common interface for getting the current set speed of a speed controller.

        :returns: The current set speed.  Value is between -1.0 and 1.0.
        """
    def getInverted(self) -> bool: 
        """
        Common interface for returning the inversion state of a speed controller.

        :returns: isInverted The state of inversion, true is inverted.
        """
    def set(self, speed: float) -> None: 
        """
        Common interface for setting the speed of a speed controller.

        :param speed: The speed to set.  Value should be between -1.0 and 1.0.
        """
    def setInverted(self, isInverted: bool) -> None: 
        """
        Common interface for inverting direction of a speed controller.

        :param isInverted: The state of inversion, true is inverted.
        """
    def setVoltage(self, output: volts) -> None: 
        """
        Sets the voltage output of the SpeedController.  Compensates for
        the current bus voltage to ensure that the desired voltage is output even
        if the battery voltage is below 12V - highly useful when the voltage
        outputs are "meaningful" (e.g. they come from a feedforward calculation).

        NOTE: This function *must* be called regularly in order for voltage
        compensation to work properly - unlike the ordinary set function, it is not
        "set it and forget it."

        :param output: The voltage to output.
        """
    def stopMotor(self) -> None: 
        """
        Common interface to stop the motor until Set is called again.
        """
    pass
class MotorController(SpeedController):
    """
    Interface for motor controlling devices.
    """
    def __init__(self) -> None: ...
    pass
