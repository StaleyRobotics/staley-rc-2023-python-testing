from __future__ import annotations
import hal.simulation._simulation
import typing
import hal._wpiHal

__all__ = [
    "AnalogTriggerMode",
    "NotifierInfo",
    "cancelAccelerometerActiveCallback",
    "cancelAccelerometerRangeCallback",
    "cancelAccelerometerXCallback",
    "cancelAccelerometerYCallback",
    "cancelAccelerometerZCallback",
    "cancelAddressableLEDDataCallback",
    "cancelAddressableLEDInitializedCallback",
    "cancelAddressableLEDLengthCallback",
    "cancelAddressableLEDOutputPortCallback",
    "cancelAddressableLEDRunningCallback",
    "cancelAllSimPeriodicCallbacks",
    "cancelAnalogGyroAngleCallback",
    "cancelAnalogGyroInitializedCallback",
    "cancelAnalogGyroRateCallback",
    "cancelAnalogInAccumulatorCenterCallback",
    "cancelAnalogInAccumulatorCountCallback",
    "cancelAnalogInAccumulatorDeadbandCallback",
    "cancelAnalogInAccumulatorInitializedCallback",
    "cancelAnalogInAccumulatorValueCallback",
    "cancelAnalogInAverageBitsCallback",
    "cancelAnalogInInitializedCallback",
    "cancelAnalogInOversampleBitsCallback",
    "cancelAnalogInVoltageCallback",
    "cancelAnalogOutInitializedCallback",
    "cancelAnalogOutVoltageCallback",
    "cancelAnalogTriggerInitializedCallback",
    "cancelAnalogTriggerTriggerLowerBoundCallback",
    "cancelAnalogTriggerTriggerModeCallback",
    "cancelAnalogTriggerTriggerUpperBoundCallback",
    "cancelCTREPCMClosedLoopEnabledCallback",
    "cancelCTREPCMCompressorCurrentCallback",
    "cancelCTREPCMCompressorOnCallback",
    "cancelCTREPCMInitializedCallback",
    "cancelCTREPCMPressureSwitchCallback",
    "cancelCTREPCMSolenoidOutputCallback",
    "cancelDIOFilterIndexCallback",
    "cancelDIOInitializedCallback",
    "cancelDIOIsInputCallback",
    "cancelDIOPulseLengthCallback",
    "cancelDIOValueCallback",
    "cancelDigitalPWMDutyCycleCallback",
    "cancelDigitalPWMInitializedCallback",
    "cancelDigitalPWMPinCallback",
    "cancelDriverStationAllianceStationIdCallback",
    "cancelDriverStationAutonomousCallback",
    "cancelDriverStationDsAttachedCallback",
    "cancelDriverStationEStopCallback",
    "cancelDriverStationEnabledCallback",
    "cancelDriverStationFmsAttachedCallback",
    "cancelDriverStationMatchTimeCallback",
    "cancelDriverStationNewDataCallback",
    "cancelDriverStationTestCallback",
    "cancelDutyCycleFrequencyCallback",
    "cancelDutyCycleInitializedCallback",
    "cancelDutyCycleOutputCallback",
    "cancelEncoderCountCallback",
    "cancelEncoderDirectionCallback",
    "cancelEncoderDistancePerPulseCallback",
    "cancelEncoderInitializedCallback",
    "cancelEncoderMaxPeriodCallback",
    "cancelEncoderPeriodCallback",
    "cancelEncoderResetCallback",
    "cancelEncoderReverseDirectionCallback",
    "cancelEncoderSamplesToAverageCallback",
    "cancelJoystickAxesCallback",
    "cancelJoystickButtonsCallback",
    "cancelJoystickDescriptorCallback",
    "cancelJoystickOutputsCallback",
    "cancelJoystickPOVsCallback",
    "cancelMatchInfoCallback",
    "cancelPWMInitializedCallback",
    "cancelPWMPeriodScaleCallback",
    "cancelPWMPositionCallback",
    "cancelPWMRawValueCallback",
    "cancelPWMSpeedCallback",
    "cancelPWMZeroLatchCallback",
    "cancelPowerDistributionCurrentCallback",
    "cancelPowerDistributionInitializedCallback",
    "cancelPowerDistributionTemperatureCallback",
    "cancelPowerDistributionVoltageCallback",
    "cancelREVPHCompressorConfigTypeCallback",
    "cancelREVPHCompressorCurrentCallback",
    "cancelREVPHCompressorOnCallback",
    "cancelREVPHInitializedCallback",
    "cancelREVPHPressureSwitchCallback",
    "cancelREVPHSolenoidOutputCallback",
    "cancelRelayForwardCallback",
    "cancelRelayInitializedForwardCallback",
    "cancelRelayInitializedReverseCallback",
    "cancelRelayReverseCallback",
    "cancelRoboRioBrownoutVoltageCallback",
    "cancelRoboRioFPGAButtonCallback",
    "cancelRoboRioUserActive3V3Callback",
    "cancelRoboRioUserActive5VCallback",
    "cancelRoboRioUserActive6VCallback",
    "cancelRoboRioUserCurrent3V3Callback",
    "cancelRoboRioUserCurrent5VCallback",
    "cancelRoboRioUserCurrent6VCallback",
    "cancelRoboRioUserFaults3V3Callback",
    "cancelRoboRioUserFaults5VCallback",
    "cancelRoboRioUserFaults6VCallback",
    "cancelRoboRioUserVoltage3V3Callback",
    "cancelRoboRioUserVoltage5VCallback",
    "cancelRoboRioUserVoltage6VCallback",
    "cancelRoboRioVInCurrentCallback",
    "cancelRoboRioVInVoltageCallback",
    "cancelSPIAccelerometerActiveCallback",
    "cancelSPIAccelerometerRangeCallback",
    "cancelSPIAccelerometerXCallback",
    "cancelSPIAccelerometerYCallback",
    "cancelSPIAccelerometerZCallback",
    "cancelSimDeviceCreatedCallback",
    "cancelSimDeviceFreedCallback",
    "cancelSimPeriodicAfterCallback",
    "cancelSimPeriodicBeforeCallback",
    "cancelSimValueChangedCallback",
    "cancelSimValueCreatedCallback",
    "cancelSimValueResetCallback",
    "findAddressableLEDForChannel",
    "findAnalogTriggerForChannel",
    "findDigitalPWMForChannel",
    "findDutyCycleForChannel",
    "findEncoderForChannel",
    "getAccelerometerActive",
    "getAccelerometerRange",
    "getAccelerometerX",
    "getAccelerometerY",
    "getAccelerometerZ",
    "getAddressableLEDData",
    "getAddressableLEDInitialized",
    "getAddressableLEDLength",
    "getAddressableLEDOutputPort",
    "getAddressableLEDRunning",
    "getAnalogGyroAngle",
    "getAnalogGyroInitialized",
    "getAnalogGyroRate",
    "getAnalogInAccumulatorCenter",
    "getAnalogInAccumulatorCount",
    "getAnalogInAccumulatorDeadband",
    "getAnalogInAccumulatorInitialized",
    "getAnalogInAccumulatorValue",
    "getAnalogInAverageBits",
    "getAnalogInInitialized",
    "getAnalogInOversampleBits",
    "getAnalogInSimDevice",
    "getAnalogInVoltage",
    "getAnalogOutInitialized",
    "getAnalogOutVoltage",
    "getAnalogTriggerInitialized",
    "getAnalogTriggerTriggerLowerBound",
    "getAnalogTriggerTriggerMode",
    "getAnalogTriggerTriggerUpperBound",
    "getCTREPCMAllSolenoids",
    "getCTREPCMClosedLoopEnabled",
    "getCTREPCMCompressorCurrent",
    "getCTREPCMCompressorOn",
    "getCTREPCMInitialized",
    "getCTREPCMPressureSwitch",
    "getCTREPCMSolenoidOutput",
    "getDIOFilterIndex",
    "getDIOInitialized",
    "getDIOIsInput",
    "getDIOPulseLength",
    "getDIOSimDevice",
    "getDIOValue",
    "getDigitalPWMDutyCycle",
    "getDigitalPWMInitialized",
    "getDigitalPWMPin",
    "getDriverStationAllianceStationId",
    "getDriverStationAutonomous",
    "getDriverStationDsAttached",
    "getDriverStationEStop",
    "getDriverStationEnabled",
    "getDriverStationFmsAttached",
    "getDriverStationMatchTime",
    "getDriverStationTest",
    "getDutyCycleDigitalChannel",
    "getDutyCycleFrequency",
    "getDutyCycleInitialized",
    "getDutyCycleOutput",
    "getDutyCycleSimDevice",
    "getEncoderCount",
    "getEncoderDigitalChannelA",
    "getEncoderDigitalChannelB",
    "getEncoderDirection",
    "getEncoderDistance",
    "getEncoderDistancePerPulse",
    "getEncoderInitialized",
    "getEncoderMaxPeriod",
    "getEncoderPeriod",
    "getEncoderRate",
    "getEncoderReset",
    "getEncoderReverseDirection",
    "getEncoderSamplesToAverage",
    "getEncoderSimDevice",
    "getJoystickAxes",
    "getJoystickButtons",
    "getJoystickCounts",
    "getJoystickDescriptor",
    "getJoystickOutputs",
    "getJoystickPOVs",
    "getMatchInfo",
    "getNextNotifierTimeout",
    "getNotifierInfo",
    "getNumNotifiers",
    "getPWMInitialized",
    "getPWMPeriodScale",
    "getPWMPosition",
    "getPWMRawValue",
    "getPWMSpeed",
    "getPWMZeroLatch",
    "getPowerDistributionAllCurrents",
    "getPowerDistributionCurrent",
    "getPowerDistributionInitialized",
    "getPowerDistributionTemperature",
    "getPowerDistributionVoltage",
    "getProgramStarted",
    "getREVPHAllSolenoids",
    "getREVPHCompressorConfigType",
    "getREVPHCompressorCurrent",
    "getREVPHCompressorOn",
    "getREVPHInitialized",
    "getREVPHPressureSwitch",
    "getREVPHSolenoidOutput",
    "getRelayForward",
    "getRelayInitializedForward",
    "getRelayInitializedReverse",
    "getRelayReverse",
    "getRoboRioBrownoutVoltage",
    "getRoboRioFPGAButton",
    "getRoboRioUserActive3V3",
    "getRoboRioUserActive5V",
    "getRoboRioUserActive6V",
    "getRoboRioUserCurrent3V3",
    "getRoboRioUserCurrent5V",
    "getRoboRioUserCurrent6V",
    "getRoboRioUserFaults3V3",
    "getRoboRioUserFaults5V",
    "getRoboRioUserFaults6V",
    "getRoboRioUserVoltage3V3",
    "getRoboRioUserVoltage5V",
    "getRoboRioUserVoltage6V",
    "getRoboRioVInCurrent",
    "getRoboRioVInVoltage",
    "getSPIAccelerometerActive",
    "getSPIAccelerometerRange",
    "getSPIAccelerometerX",
    "getSPIAccelerometerY",
    "getSPIAccelerometerZ",
    "getSimDeviceHandle",
    "getSimDeviceName",
    "getSimValueDeviceHandle",
    "getSimValueHandle",
    "isSimDeviceEnabled",
    "isTimingPaused",
    "notifyDriverStationNewData",
    "pauseTiming",
    "resetAccelerometerData",
    "resetAddressableLEDData",
    "resetAllData",
    "resetAnalogGyroData",
    "resetAnalogInData",
    "resetAnalogOutData",
    "resetAnalogTriggerData",
    "resetCTREPCMData",
    "resetDIOData",
    "resetDigitalPWMData",
    "resetDriverStationData",
    "resetDutyCycleData",
    "resetEncoderData",
    "resetGlobalHandles",
    "resetPWMData",
    "resetPowerDistributionData",
    "resetREVPHData",
    "resetRelayData",
    "resetRoboRioData",
    "resetSPIAccelerometerData",
    "resetSimDeviceData",
    "restartTiming",
    "resumeTiming",
    "setAccelerometerActive",
    "setAccelerometerRange",
    "setAccelerometerX",
    "setAccelerometerY",
    "setAccelerometerZ",
    "setAddressableLEDData",
    "setAddressableLEDInitialized",
    "setAddressableLEDLength",
    "setAddressableLEDOutputPort",
    "setAddressableLEDRunning",
    "setAnalogGyroAngle",
    "setAnalogGyroInitialized",
    "setAnalogGyroRate",
    "setAnalogInAccumulatorCenter",
    "setAnalogInAccumulatorCount",
    "setAnalogInAccumulatorDeadband",
    "setAnalogInAccumulatorInitialized",
    "setAnalogInAccumulatorValue",
    "setAnalogInAverageBits",
    "setAnalogInInitialized",
    "setAnalogInOversampleBits",
    "setAnalogInVoltage",
    "setAnalogOutInitialized",
    "setAnalogOutVoltage",
    "setAnalogTriggerInitialized",
    "setAnalogTriggerTriggerLowerBound",
    "setAnalogTriggerTriggerMode",
    "setAnalogTriggerTriggerUpperBound",
    "setCTREPCMAllSolenoids",
    "setCTREPCMClosedLoopEnabled",
    "setCTREPCMCompressorCurrent",
    "setCTREPCMCompressorOn",
    "setCTREPCMInitialized",
    "setCTREPCMPressureSwitch",
    "setCTREPCMSolenoidOutput",
    "setDIOFilterIndex",
    "setDIOInitialized",
    "setDIOIsInput",
    "setDIOPulseLength",
    "setDIOValue",
    "setDigitalPWMDutyCycle",
    "setDigitalPWMInitialized",
    "setDigitalPWMPin",
    "setDriverStationAllianceStationId",
    "setDriverStationAutonomous",
    "setDriverStationDsAttached",
    "setDriverStationEStop",
    "setDriverStationEnabled",
    "setDriverStationFmsAttached",
    "setDriverStationMatchTime",
    "setDriverStationTest",
    "setDutyCycleFrequency",
    "setDutyCycleInitialized",
    "setDutyCycleOutput",
    "setEncoderCount",
    "setEncoderDirection",
    "setEncoderDistance",
    "setEncoderDistancePerPulse",
    "setEncoderInitialized",
    "setEncoderMaxPeriod",
    "setEncoderPeriod",
    "setEncoderRate",
    "setEncoderReset",
    "setEncoderReverseDirection",
    "setEncoderSamplesToAverage",
    "setEventName",
    "setGameSpecificMessage",
    "setJoystickAxes",
    "setJoystickAxis",
    "setJoystickAxisCount",
    "setJoystickAxisType",
    "setJoystickButton",
    "setJoystickButtonCount",
    "setJoystickButtons",
    "setJoystickButtonsValue",
    "setJoystickDescriptor",
    "setJoystickIsXbox",
    "setJoystickName",
    "setJoystickOutputs",
    "setJoystickPOV",
    "setJoystickPOVCount",
    "setJoystickPOVs",
    "setJoystickType",
    "setMatchInfo",
    "setMatchNumber",
    "setMatchType",
    "setPWMInitialized",
    "setPWMPeriodScale",
    "setPWMPosition",
    "setPWMRawValue",
    "setPWMSpeed",
    "setPWMZeroLatch",
    "setPowerDistributionAllCurrents",
    "setPowerDistributionCurrent",
    "setPowerDistributionInitialized",
    "setPowerDistributionTemperature",
    "setPowerDistributionVoltage",
    "setProgramStarted",
    "setREVPHAllSolenoids",
    "setREVPHCompressorConfigType",
    "setREVPHCompressorCurrent",
    "setREVPHCompressorOn",
    "setREVPHInitialized",
    "setREVPHPressureSwitch",
    "setREVPHSolenoidOutput",
    "setRelayForward",
    "setRelayInitializedForward",
    "setRelayInitializedReverse",
    "setRelayReverse",
    "setReplayNumber",
    "setRoboRioBrownoutVoltage",
    "setRoboRioFPGAButton",
    "setRoboRioUserActive3V3",
    "setRoboRioUserActive5V",
    "setRoboRioUserActive6V",
    "setRoboRioUserCurrent3V3",
    "setRoboRioUserCurrent5V",
    "setRoboRioUserCurrent6V",
    "setRoboRioUserFaults3V3",
    "setRoboRioUserFaults5V",
    "setRoboRioUserFaults6V",
    "setRoboRioUserVoltage3V3",
    "setRoboRioUserVoltage5V",
    "setRoboRioUserVoltage6V",
    "setRoboRioVInCurrent",
    "setRoboRioVInVoltage",
    "setRuntimeType",
    "setSPIAccelerometerActive",
    "setSPIAccelerometerRange",
    "setSPIAccelerometerX",
    "setSPIAccelerometerY",
    "setSPIAccelerometerZ",
    "setSimDeviceEnabled",
    "stepTiming",
    "stepTimingAsync",
    "waitForProgramStart"
]


class AnalogTriggerMode():
    """
    Members:

      HALSIM_AnalogTriggerUnassigned

      HALSIM_AnalogTriggerFiltered

      HALSIM_AnalogTriggerDutyCycle

      HALSIM_AnalogTriggerAveraged
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
    HALSIM_AnalogTriggerAveraged: hal.simulation._simulation.AnalogTriggerMode # value = <AnalogTriggerMode.HALSIM_AnalogTriggerAveraged: 3>
    HALSIM_AnalogTriggerDutyCycle: hal.simulation._simulation.AnalogTriggerMode # value = <AnalogTriggerMode.HALSIM_AnalogTriggerDutyCycle: 2>
    HALSIM_AnalogTriggerFiltered: hal.simulation._simulation.AnalogTriggerMode # value = <AnalogTriggerMode.HALSIM_AnalogTriggerFiltered: 1>
    HALSIM_AnalogTriggerUnassigned: hal.simulation._simulation.AnalogTriggerMode # value = <AnalogTriggerMode.HALSIM_AnalogTriggerUnassigned: 0>
    __members__: dict # value = {'HALSIM_AnalogTriggerUnassigned': <AnalogTriggerMode.HALSIM_AnalogTriggerUnassigned: 0>, 'HALSIM_AnalogTriggerFiltered': <AnalogTriggerMode.HALSIM_AnalogTriggerFiltered: 1>, 'HALSIM_AnalogTriggerDutyCycle': <AnalogTriggerMode.HALSIM_AnalogTriggerDutyCycle: 2>, 'HALSIM_AnalogTriggerAveraged': <AnalogTriggerMode.HALSIM_AnalogTriggerAveraged: 3>}
    pass
class NotifierInfo():
    def __init__(self) -> None: ...
    @property
    def handle(self) -> int:
        """
        :type: int
        """
    @handle.setter
    def handle(self, arg0: int) -> None:
        pass
    @property
    def name(self) -> memoryview:
        """
        :type: memoryview
        """
    @property
    def timeout(self) -> int:
        """
        :type: int
        """
    @timeout.setter
    def timeout(self, arg0: int) -> None:
        pass
    @property
    def waitTimeValid(self) -> int:
        """
        :type: int
        """
    @waitTimeValid.setter
    def waitTimeValid(self, arg0: int) -> None:
        pass
    pass
def cancelAccelerometerActiveCallback(index: int, uid: int) -> None:
    pass
def cancelAccelerometerRangeCallback(index: int, uid: int) -> None:
    pass
def cancelAccelerometerXCallback(index: int, uid: int) -> None:
    pass
def cancelAccelerometerYCallback(index: int, uid: int) -> None:
    pass
def cancelAccelerometerZCallback(index: int, uid: int) -> None:
    pass
def cancelAddressableLEDDataCallback(index: int, uid: int) -> None:
    pass
def cancelAddressableLEDInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelAddressableLEDLengthCallback(index: int, uid: int) -> None:
    pass
def cancelAddressableLEDOutputPortCallback(index: int, uid: int) -> None:
    pass
def cancelAddressableLEDRunningCallback(index: int, uid: int) -> None:
    pass
def cancelAllSimPeriodicCallbacks() -> None:
    pass
def cancelAnalogGyroAngleCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogGyroInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogGyroRateCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogInAccumulatorCenterCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogInAccumulatorCountCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogInAccumulatorDeadbandCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogInAccumulatorInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogInAccumulatorValueCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogInAverageBitsCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogInInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogInOversampleBitsCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogInVoltageCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogOutInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogOutVoltageCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogTriggerInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogTriggerTriggerLowerBoundCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogTriggerTriggerModeCallback(index: int, uid: int) -> None:
    pass
def cancelAnalogTriggerTriggerUpperBoundCallback(index: int, uid: int) -> None:
    pass
def cancelCTREPCMClosedLoopEnabledCallback(index: int, uid: int) -> None:
    pass
def cancelCTREPCMCompressorCurrentCallback(index: int, uid: int) -> None:
    pass
def cancelCTREPCMCompressorOnCallback(index: int, uid: int) -> None:
    pass
def cancelCTREPCMInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelCTREPCMPressureSwitchCallback(index: int, uid: int) -> None:
    pass
def cancelCTREPCMSolenoidOutputCallback(index: int, channel: int, uid: int) -> None:
    pass
def cancelDIOFilterIndexCallback(index: int, uid: int) -> None:
    pass
def cancelDIOInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelDIOIsInputCallback(index: int, uid: int) -> None:
    pass
def cancelDIOPulseLengthCallback(index: int, uid: int) -> None:
    pass
def cancelDIOValueCallback(index: int, uid: int) -> None:
    pass
def cancelDigitalPWMDutyCycleCallback(index: int, uid: int) -> None:
    pass
def cancelDigitalPWMInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelDigitalPWMPinCallback(index: int, uid: int) -> None:
    pass
def cancelDriverStationAllianceStationIdCallback(uid: int) -> None:
    pass
def cancelDriverStationAutonomousCallback(uid: int) -> None:
    pass
def cancelDriverStationDsAttachedCallback(uid: int) -> None:
    pass
def cancelDriverStationEStopCallback(uid: int) -> None:
    pass
def cancelDriverStationEnabledCallback(uid: int) -> None:
    pass
def cancelDriverStationFmsAttachedCallback(uid: int) -> None:
    pass
def cancelDriverStationMatchTimeCallback(uid: int) -> None:
    pass
def cancelDriverStationNewDataCallback(uid: int) -> None:
    pass
def cancelDriverStationTestCallback(uid: int) -> None:
    pass
def cancelDutyCycleFrequencyCallback(index: int, uid: int) -> None:
    pass
def cancelDutyCycleInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelDutyCycleOutputCallback(index: int, uid: int) -> None:
    pass
def cancelEncoderCountCallback(index: int, uid: int) -> None:
    pass
def cancelEncoderDirectionCallback(index: int, uid: int) -> None:
    pass
def cancelEncoderDistancePerPulseCallback(index: int, uid: int) -> None:
    pass
def cancelEncoderInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelEncoderMaxPeriodCallback(index: int, uid: int) -> None:
    pass
def cancelEncoderPeriodCallback(index: int, uid: int) -> None:
    pass
def cancelEncoderResetCallback(index: int, uid: int) -> None:
    pass
def cancelEncoderReverseDirectionCallback(index: int, uid: int) -> None:
    pass
def cancelEncoderSamplesToAverageCallback(index: int, uid: int) -> None:
    pass
def cancelJoystickAxesCallback(uid: int) -> None:
    pass
def cancelJoystickButtonsCallback(uid: int) -> None:
    pass
def cancelJoystickDescriptorCallback(uid: int) -> None:
    pass
def cancelJoystickOutputsCallback(uid: int) -> None:
    pass
def cancelJoystickPOVsCallback(uid: int) -> None:
    pass
def cancelMatchInfoCallback(uid: int) -> None:
    pass
def cancelPWMInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelPWMPeriodScaleCallback(index: int, uid: int) -> None:
    pass
def cancelPWMPositionCallback(index: int, uid: int) -> None:
    pass
def cancelPWMRawValueCallback(index: int, uid: int) -> None:
    pass
def cancelPWMSpeedCallback(index: int, uid: int) -> None:
    pass
def cancelPWMZeroLatchCallback(index: int, uid: int) -> None:
    pass
def cancelPowerDistributionCurrentCallback(index: int, channel: int, uid: int) -> None:
    pass
def cancelPowerDistributionInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelPowerDistributionTemperatureCallback(index: int, uid: int) -> None:
    pass
def cancelPowerDistributionVoltageCallback(index: int, uid: int) -> None:
    pass
def cancelREVPHCompressorConfigTypeCallback(index: int, uid: int) -> None:
    pass
def cancelREVPHCompressorCurrentCallback(index: int, uid: int) -> None:
    pass
def cancelREVPHCompressorOnCallback(index: int, uid: int) -> None:
    pass
def cancelREVPHInitializedCallback(index: int, uid: int) -> None:
    pass
def cancelREVPHPressureSwitchCallback(index: int, uid: int) -> None:
    pass
def cancelREVPHSolenoidOutputCallback(index: int, channel: int, uid: int) -> None:
    pass
def cancelRelayForwardCallback(index: int, uid: int) -> None:
    pass
def cancelRelayInitializedForwardCallback(index: int, uid: int) -> None:
    pass
def cancelRelayInitializedReverseCallback(index: int, uid: int) -> None:
    pass
def cancelRelayReverseCallback(index: int, uid: int) -> None:
    pass
def cancelRoboRioBrownoutVoltageCallback(uid: int) -> None:
    pass
def cancelRoboRioFPGAButtonCallback(uid: int) -> None:
    pass
def cancelRoboRioUserActive3V3Callback(uid: int) -> None:
    pass
def cancelRoboRioUserActive5VCallback(uid: int) -> None:
    pass
def cancelRoboRioUserActive6VCallback(uid: int) -> None:
    pass
def cancelRoboRioUserCurrent3V3Callback(uid: int) -> None:
    pass
def cancelRoboRioUserCurrent5VCallback(uid: int) -> None:
    pass
def cancelRoboRioUserCurrent6VCallback(uid: int) -> None:
    pass
def cancelRoboRioUserFaults3V3Callback(uid: int) -> None:
    pass
def cancelRoboRioUserFaults5VCallback(uid: int) -> None:
    pass
def cancelRoboRioUserFaults6VCallback(uid: int) -> None:
    pass
def cancelRoboRioUserVoltage3V3Callback(uid: int) -> None:
    pass
def cancelRoboRioUserVoltage5VCallback(uid: int) -> None:
    pass
def cancelRoboRioUserVoltage6VCallback(uid: int) -> None:
    pass
def cancelRoboRioVInCurrentCallback(uid: int) -> None:
    pass
def cancelRoboRioVInVoltageCallback(uid: int) -> None:
    pass
def cancelSPIAccelerometerActiveCallback(index: int, uid: int) -> None:
    pass
def cancelSPIAccelerometerRangeCallback(index: int, uid: int) -> None:
    pass
def cancelSPIAccelerometerXCallback(index: int, uid: int) -> None:
    pass
def cancelSPIAccelerometerYCallback(index: int, uid: int) -> None:
    pass
def cancelSPIAccelerometerZCallback(index: int, uid: int) -> None:
    pass
def cancelSimDeviceCreatedCallback(uid: int) -> None:
    pass
def cancelSimDeviceFreedCallback(uid: int) -> None:
    pass
def cancelSimPeriodicAfterCallback(uid: int) -> None:
    pass
def cancelSimPeriodicBeforeCallback(uid: int) -> None:
    pass
def cancelSimValueChangedCallback(uid: int) -> None:
    pass
def cancelSimValueCreatedCallback(uid: int) -> None:
    pass
def cancelSimValueResetCallback(uid: int) -> None:
    pass
def findAddressableLEDForChannel(channel: int) -> int:
    pass
def findAnalogTriggerForChannel(channel: int) -> int:
    pass
def findDigitalPWMForChannel(channel: int) -> int:
    pass
def findDutyCycleForChannel(channel: int) -> int:
    pass
def findEncoderForChannel(channel: int) -> int:
    pass
def getAccelerometerActive(index: int) -> int:
    pass
def getAccelerometerRange(index: int) -> hal._wpiHal.AccelerometerRange:
    pass
def getAccelerometerX(index: int) -> float:
    pass
def getAccelerometerY(index: int) -> float:
    pass
def getAccelerometerZ(index: int) -> float:
    pass
def getAddressableLEDData(index: int, data: hal._wpiHal.AddressableLEDData) -> int:
    pass
def getAddressableLEDInitialized(index: int) -> int:
    pass
def getAddressableLEDLength(index: int) -> int:
    pass
def getAddressableLEDOutputPort(index: int) -> int:
    pass
def getAddressableLEDRunning(index: int) -> int:
    pass
def getAnalogGyroAngle(index: int) -> float:
    pass
def getAnalogGyroInitialized(index: int) -> int:
    pass
def getAnalogGyroRate(index: int) -> float:
    pass
def getAnalogInAccumulatorCenter(index: int) -> int:
    pass
def getAnalogInAccumulatorCount(index: int) -> int:
    pass
def getAnalogInAccumulatorDeadband(index: int) -> int:
    pass
def getAnalogInAccumulatorInitialized(index: int) -> int:
    pass
def getAnalogInAccumulatorValue(index: int) -> int:
    pass
def getAnalogInAverageBits(index: int) -> int:
    pass
def getAnalogInInitialized(index: int) -> int:
    pass
def getAnalogInOversampleBits(index: int) -> int:
    pass
def getAnalogInSimDevice(index: int) -> int:
    pass
def getAnalogInVoltage(index: int) -> float:
    pass
def getAnalogOutInitialized(index: int) -> int:
    pass
def getAnalogOutVoltage(index: int) -> float:
    pass
def getAnalogTriggerInitialized(index: int) -> int:
    pass
def getAnalogTriggerTriggerLowerBound(index: int) -> float:
    pass
def getAnalogTriggerTriggerMode(index: int) -> AnalogTriggerMode:
    pass
def getAnalogTriggerTriggerUpperBound(index: int) -> float:
    pass
def getCTREPCMAllSolenoids(index: int) -> int:
    pass
def getCTREPCMClosedLoopEnabled(index: int) -> int:
    pass
def getCTREPCMCompressorCurrent(index: int) -> float:
    pass
def getCTREPCMCompressorOn(index: int) -> int:
    pass
def getCTREPCMInitialized(index: int) -> int:
    pass
def getCTREPCMPressureSwitch(index: int) -> int:
    pass
def getCTREPCMSolenoidOutput(index: int, channel: int) -> int:
    pass
def getDIOFilterIndex(index: int) -> int:
    pass
def getDIOInitialized(index: int) -> int:
    pass
def getDIOIsInput(index: int) -> int:
    pass
def getDIOPulseLength(index: int) -> float:
    pass
def getDIOSimDevice(index: int) -> int:
    pass
def getDIOValue(index: int) -> int:
    pass
def getDigitalPWMDutyCycle(index: int) -> float:
    pass
def getDigitalPWMInitialized(index: int) -> int:
    pass
def getDigitalPWMPin(index: int) -> int:
    pass
def getDriverStationAllianceStationId() -> hal._wpiHal.AllianceStationID:
    pass
def getDriverStationAutonomous() -> int:
    pass
def getDriverStationDsAttached() -> int:
    pass
def getDriverStationEStop() -> int:
    pass
def getDriverStationEnabled() -> int:
    pass
def getDriverStationFmsAttached() -> int:
    pass
def getDriverStationMatchTime() -> float:
    pass
def getDriverStationTest() -> int:
    pass
def getDutyCycleDigitalChannel(index: int) -> int:
    pass
def getDutyCycleFrequency(index: int) -> int:
    pass
def getDutyCycleInitialized(index: int) -> int:
    pass
def getDutyCycleOutput(index: int) -> float:
    pass
def getDutyCycleSimDevice(index: int) -> int:
    pass
def getEncoderCount(index: int) -> int:
    pass
def getEncoderDigitalChannelA(index: int) -> int:
    pass
def getEncoderDigitalChannelB(index: int) -> int:
    pass
def getEncoderDirection(index: int) -> int:
    pass
def getEncoderDistance(index: int) -> float:
    pass
def getEncoderDistancePerPulse(index: int) -> float:
    pass
def getEncoderInitialized(index: int) -> int:
    pass
def getEncoderMaxPeriod(index: int) -> float:
    pass
def getEncoderPeriod(index: int) -> float:
    pass
def getEncoderRate(index: int) -> float:
    pass
def getEncoderReset(index: int) -> int:
    pass
def getEncoderReverseDirection(index: int) -> int:
    pass
def getEncoderSamplesToAverage(index: int) -> int:
    pass
def getEncoderSimDevice(index: int) -> int:
    pass
def getJoystickAxes(joystickNum: int, axes: hal._wpiHal.JoystickAxes) -> None:
    pass
def getJoystickButtons(joystickNum: int, buttons: hal._wpiHal.JoystickButtons) -> None:
    pass
def getJoystickCounts(stick: int) -> typing.Tuple[int, int, int]:
    pass
def getJoystickDescriptor(joystickNum: int, descriptor: hal._wpiHal.JoystickDescriptor) -> None:
    pass
def getJoystickOutputs(joystickNum: int) -> typing.Tuple[int, int, int]:
    pass
def getJoystickPOVs(joystickNum: int, povs: hal._wpiHal.JoystickPOVs) -> None:
    pass
def getMatchInfo(info: hal._wpiHal.MatchInfo) -> None:
    pass
def getNextNotifierTimeout() -> int:
    pass
def getNotifierInfo(arr: NotifierInfo, size: int) -> int:
    """
    Gets detailed information about each notifier.

    :param arr:  array of information to be filled
    :param size: size of arr

    :returns: Number of notifiers; note: may be larger than passed-in size
    """
def getNumNotifiers() -> int:
    pass
def getPWMInitialized(index: int) -> int:
    pass
def getPWMPeriodScale(index: int) -> int:
    pass
def getPWMPosition(index: int) -> float:
    pass
def getPWMRawValue(index: int) -> int:
    pass
def getPWMSpeed(index: int) -> float:
    pass
def getPWMZeroLatch(index: int) -> int:
    pass
def getPowerDistributionAllCurrents(index: int, length: int) -> float:
    pass
def getPowerDistributionCurrent(index: int, channel: int) -> float:
    pass
def getPowerDistributionInitialized(index: int) -> int:
    pass
def getPowerDistributionTemperature(index: int) -> float:
    pass
def getPowerDistributionVoltage(index: int) -> float:
    pass
def getProgramStarted() -> int:
    pass
def getREVPHAllSolenoids(index: int) -> int:
    pass
def getREVPHCompressorConfigType(index: int) -> hal._wpiHal.REVPHCompressorConfigType:
    pass
def getREVPHCompressorCurrent(index: int) -> float:
    pass
def getREVPHCompressorOn(index: int) -> int:
    pass
def getREVPHInitialized(index: int) -> int:
    pass
def getREVPHPressureSwitch(index: int) -> int:
    pass
def getREVPHSolenoidOutput(index: int, channel: int) -> int:
    pass
def getRelayForward(index: int) -> int:
    pass
def getRelayInitializedForward(index: int) -> int:
    pass
def getRelayInitializedReverse(index: int) -> int:
    pass
def getRelayReverse(index: int) -> int:
    pass
def getRoboRioBrownoutVoltage() -> float:
    pass
def getRoboRioFPGAButton() -> int:
    pass
def getRoboRioUserActive3V3() -> int:
    pass
def getRoboRioUserActive5V() -> int:
    pass
def getRoboRioUserActive6V() -> int:
    pass
def getRoboRioUserCurrent3V3() -> float:
    pass
def getRoboRioUserCurrent5V() -> float:
    pass
def getRoboRioUserCurrent6V() -> float:
    pass
def getRoboRioUserFaults3V3() -> int:
    pass
def getRoboRioUserFaults5V() -> int:
    pass
def getRoboRioUserFaults6V() -> int:
    pass
def getRoboRioUserVoltage3V3() -> float:
    pass
def getRoboRioUserVoltage5V() -> float:
    pass
def getRoboRioUserVoltage6V() -> float:
    pass
def getRoboRioVInCurrent() -> float:
    pass
def getRoboRioVInVoltage() -> float:
    pass
def getSPIAccelerometerActive(index: int) -> int:
    pass
def getSPIAccelerometerRange(index: int) -> int:
    pass
def getSPIAccelerometerX(index: int) -> float:
    pass
def getSPIAccelerometerY(index: int) -> float:
    pass
def getSPIAccelerometerZ(index: int) -> float:
    pass
def getSimDeviceHandle(name: str) -> int:
    pass
def getSimDeviceName(handle: int) -> str:
    pass
def getSimValueDeviceHandle(handle: int) -> int:
    pass
def getSimValueHandle(device: int, name: str) -> int:
    pass
def isSimDeviceEnabled(name: str) -> int:
    pass
def isTimingPaused() -> int:
    pass
def notifyDriverStationNewData() -> None:
    pass
def pauseTiming() -> None:
    pass
def resetAccelerometerData(index: int) -> None:
    pass
def resetAddressableLEDData(index: int) -> None:
    pass
def resetAllData() -> None:
    pass
def resetAnalogGyroData(index: int) -> None:
    pass
def resetAnalogInData(index: int) -> None:
    pass
def resetAnalogOutData(index: int) -> None:
    pass
def resetAnalogTriggerData(index: int) -> None:
    pass
def resetCTREPCMData(index: int) -> None:
    pass
def resetDIOData(index: int) -> None:
    pass
def resetDigitalPWMData(index: int) -> None:
    pass
def resetDriverStationData() -> None:
    pass
def resetDutyCycleData(index: int) -> None:
    pass
def resetEncoderData(index: int) -> None:
    pass
def resetGlobalHandles() -> None:
    pass
def resetPWMData(index: int) -> None:
    pass
def resetPowerDistributionData(index: int) -> None:
    pass
def resetREVPHData(index: int) -> None:
    pass
def resetRelayData(index: int) -> None:
    pass
def resetRoboRioData() -> None:
    pass
def resetSPIAccelerometerData(index: int) -> None:
    pass
def resetSimDeviceData() -> None:
    pass
def restartTiming() -> None:
    pass
def resumeTiming() -> None:
    pass
def setAccelerometerActive(index: int, active: int) -> None:
    pass
def setAccelerometerRange(index: int, range: hal._wpiHal.AccelerometerRange) -> None:
    pass
def setAccelerometerX(index: int, x: float) -> None:
    pass
def setAccelerometerY(index: int, y: float) -> None:
    pass
def setAccelerometerZ(index: int, z: float) -> None:
    pass
def setAddressableLEDData(index: int, data: hal._wpiHal.AddressableLEDData, length: int) -> None:
    pass
def setAddressableLEDInitialized(index: int, initialized: int) -> None:
    pass
def setAddressableLEDLength(index: int, length: int) -> None:
    pass
def setAddressableLEDOutputPort(index: int, outputPort: int) -> None:
    pass
def setAddressableLEDRunning(index: int, running: int) -> None:
    pass
def setAnalogGyroAngle(index: int, angle: float) -> None:
    pass
def setAnalogGyroInitialized(index: int, initialized: int) -> None:
    pass
def setAnalogGyroRate(index: int, rate: float) -> None:
    pass
def setAnalogInAccumulatorCenter(index: int, accumulatorCenter: int) -> None:
    pass
def setAnalogInAccumulatorCount(index: int, accumulatorCount: int) -> None:
    pass
def setAnalogInAccumulatorDeadband(index: int, accumulatorDeadband: int) -> None:
    pass
def setAnalogInAccumulatorInitialized(index: int, accumulatorInitialized: int) -> None:
    pass
def setAnalogInAccumulatorValue(index: int, accumulatorValue: int) -> None:
    pass
def setAnalogInAverageBits(index: int, averageBits: int) -> None:
    pass
def setAnalogInInitialized(index: int, initialized: int) -> None:
    pass
def setAnalogInOversampleBits(index: int, oversampleBits: int) -> None:
    pass
def setAnalogInVoltage(index: int, voltage: float) -> None:
    pass
def setAnalogOutInitialized(index: int, initialized: int) -> None:
    pass
def setAnalogOutVoltage(index: int, voltage: float) -> None:
    pass
def setAnalogTriggerInitialized(index: int, initialized: int) -> None:
    pass
def setAnalogTriggerTriggerLowerBound(index: int, triggerLowerBound: float) -> None:
    pass
def setAnalogTriggerTriggerMode(index: int, triggerMode: AnalogTriggerMode) -> None:
    pass
def setAnalogTriggerTriggerUpperBound(index: int, triggerUpperBound: float) -> None:
    pass
def setCTREPCMAllSolenoids(index: int, values: int) -> None:
    pass
def setCTREPCMClosedLoopEnabled(index: int, closedLoopEnabled: int) -> None:
    pass
def setCTREPCMCompressorCurrent(index: int, compressorCurrent: float) -> None:
    pass
def setCTREPCMCompressorOn(index: int, compressorOn: int) -> None:
    pass
def setCTREPCMInitialized(index: int, solenoidInitialized: int) -> None:
    pass
def setCTREPCMPressureSwitch(index: int, pressureSwitch: int) -> None:
    pass
def setCTREPCMSolenoidOutput(index: int, channel: int, solenoidOutput: int) -> None:
    pass
def setDIOFilterIndex(index: int, filterIndex: int) -> None:
    pass
def setDIOInitialized(index: int, initialized: int) -> None:
    pass
def setDIOIsInput(index: int, isInput: int) -> None:
    pass
def setDIOPulseLength(index: int, pulseLength: float) -> None:
    pass
def setDIOValue(index: int, value: int) -> None:
    pass
def setDigitalPWMDutyCycle(index: int, dutyCycle: float) -> None:
    pass
def setDigitalPWMInitialized(index: int, initialized: int) -> None:
    pass
def setDigitalPWMPin(index: int, pin: int) -> None:
    pass
def setDriverStationAllianceStationId(allianceStationId: hal._wpiHal.AllianceStationID) -> None:
    pass
def setDriverStationAutonomous(autonomous: int) -> None:
    pass
def setDriverStationDsAttached(dsAttached: int) -> None:
    pass
def setDriverStationEStop(eStop: int) -> None:
    pass
def setDriverStationEnabled(enabled: int) -> None:
    pass
def setDriverStationFmsAttached(fmsAttached: int) -> None:
    pass
def setDriverStationMatchTime(matchTime: float) -> None:
    pass
def setDriverStationTest(test: int) -> None:
    pass
def setDutyCycleFrequency(index: int, frequency: int) -> None:
    pass
def setDutyCycleInitialized(index: int, initialized: int) -> None:
    pass
def setDutyCycleOutput(index: int, output: float) -> None:
    pass
def setEncoderCount(index: int, count: int) -> None:
    pass
def setEncoderDirection(index: int, direction: int) -> None:
    pass
def setEncoderDistance(index: int, distance: float) -> None:
    pass
def setEncoderDistancePerPulse(index: int, distancePerPulse: float) -> None:
    pass
def setEncoderInitialized(index: int, initialized: int) -> None:
    pass
def setEncoderMaxPeriod(index: int, maxPeriod: float) -> None:
    pass
def setEncoderPeriod(index: int, period: float) -> None:
    pass
def setEncoderRate(index: int, rate: float) -> None:
    pass
def setEncoderReset(index: int, reset: int) -> None:
    pass
def setEncoderReverseDirection(index: int, reverseDirection: int) -> None:
    pass
def setEncoderSamplesToAverage(index: int, samplesToAverage: int) -> None:
    pass
def setEventName(name: str) -> None:
    pass
def setGameSpecificMessage(message: str) -> None:
    pass
def setJoystickAxes(joystickNum: int, axes: hal._wpiHal.JoystickAxes) -> None:
    pass
def setJoystickAxis(stick: int, axis: int, value: float) -> None:
    pass
def setJoystickAxisCount(stick: int, count: int) -> None:
    pass
def setJoystickAxisType(stick: int, axis: int, type: int) -> None:
    pass
def setJoystickButton(stick: int, button: int, state: int) -> None:
    pass
def setJoystickButtonCount(stick: int, count: int) -> None:
    pass
def setJoystickButtons(joystickNum: int, buttons: hal._wpiHal.JoystickButtons) -> None:
    pass
def setJoystickButtonsValue(stick: int, buttons: int) -> None:
    pass
def setJoystickDescriptor(joystickNum: int, descriptor: hal._wpiHal.JoystickDescriptor) -> None:
    pass
def setJoystickIsXbox(stick: int, isXbox: int) -> None:
    pass
def setJoystickName(stick: int, name: str) -> None:
    pass
def setJoystickOutputs(joystickNum: int, outputs: int, leftRumble: int, rightRumble: int) -> None:
    pass
def setJoystickPOV(stick: int, pov: int, value: int) -> None:
    pass
def setJoystickPOVCount(stick: int, count: int) -> None:
    pass
def setJoystickPOVs(joystickNum: int, povs: hal._wpiHal.JoystickPOVs) -> None:
    pass
def setJoystickType(stick: int, type: int) -> None:
    pass
def setMatchInfo(info: hal._wpiHal.MatchInfo) -> None:
    pass
def setMatchNumber(matchNumber: int) -> None:
    pass
def setMatchType(type: hal._wpiHal.MatchType) -> None:
    pass
def setPWMInitialized(index: int, initialized: int) -> None:
    pass
def setPWMPeriodScale(index: int, periodScale: int) -> None:
    pass
def setPWMPosition(index: int, position: float) -> None:
    pass
def setPWMRawValue(index: int, rawValue: int) -> None:
    pass
def setPWMSpeed(index: int, speed: float) -> None:
    pass
def setPWMZeroLatch(index: int, zeroLatch: int) -> None:
    pass
def setPowerDistributionAllCurrents(index: int, currents: float, length: int) -> None:
    pass
def setPowerDistributionCurrent(index: int, channel: int, current: float) -> None:
    pass
def setPowerDistributionInitialized(index: int, initialized: int) -> None:
    pass
def setPowerDistributionTemperature(index: int, temperature: float) -> None:
    pass
def setPowerDistributionVoltage(index: int, voltage: float) -> None:
    pass
def setProgramStarted() -> None:
    pass
def setREVPHAllSolenoids(index: int, values: int) -> None:
    pass
def setREVPHCompressorConfigType(index: int, configType: hal._wpiHal.REVPHCompressorConfigType) -> None:
    pass
def setREVPHCompressorCurrent(index: int, compressorCurrent: float) -> None:
    pass
def setREVPHCompressorOn(index: int, compressorOn: int) -> None:
    pass
def setREVPHInitialized(index: int, solenoidInitialized: int) -> None:
    pass
def setREVPHPressureSwitch(index: int, pressureSwitch: int) -> None:
    pass
def setREVPHSolenoidOutput(index: int, channel: int, solenoidOutput: int) -> None:
    pass
def setRelayForward(index: int, forward: int) -> None:
    pass
def setRelayInitializedForward(index: int, initializedForward: int) -> None:
    pass
def setRelayInitializedReverse(index: int, initializedReverse: int) -> None:
    pass
def setRelayReverse(index: int, reverse: int) -> None:
    pass
def setReplayNumber(replayNumber: int) -> None:
    pass
def setRoboRioBrownoutVoltage(brownoutVoltage: float) -> None:
    pass
def setRoboRioFPGAButton(fPGAButton: int) -> None:
    pass
def setRoboRioUserActive3V3(userActive3V3: int) -> None:
    pass
def setRoboRioUserActive5V(userActive5V: int) -> None:
    pass
def setRoboRioUserActive6V(userActive6V: int) -> None:
    pass
def setRoboRioUserCurrent3V3(userCurrent3V3: float) -> None:
    pass
def setRoboRioUserCurrent5V(userCurrent5V: float) -> None:
    pass
def setRoboRioUserCurrent6V(userCurrent6V: float) -> None:
    pass
def setRoboRioUserFaults3V3(userFaults3V3: int) -> None:
    pass
def setRoboRioUserFaults5V(userFaults5V: int) -> None:
    pass
def setRoboRioUserFaults6V(userFaults6V: int) -> None:
    pass
def setRoboRioUserVoltage3V3(userVoltage3V3: float) -> None:
    pass
def setRoboRioUserVoltage5V(userVoltage5V: float) -> None:
    pass
def setRoboRioUserVoltage6V(userVoltage6V: float) -> None:
    pass
def setRoboRioVInCurrent(vInCurrent: float) -> None:
    pass
def setRoboRioVInVoltage(vInVoltage: float) -> None:
    pass
def setRuntimeType(type: hal._wpiHal.RuntimeType) -> None:
    pass
def setSPIAccelerometerActive(index: int, active: int) -> None:
    pass
def setSPIAccelerometerRange(index: int, range: int) -> None:
    pass
def setSPIAccelerometerX(index: int, x: float) -> None:
    pass
def setSPIAccelerometerY(index: int, y: float) -> None:
    pass
def setSPIAccelerometerZ(index: int, z: float) -> None:
    pass
def setSimDeviceEnabled(prefix: str, enabled: int) -> None:
    pass
def stepTiming(delta: int) -> None:
    pass
def stepTimingAsync(delta: int) -> None:
    pass
def waitForProgramStart() -> None:
    pass
