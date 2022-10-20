from __future__ import annotations
import wpiutil._wpiutil
import typing

__all__ = [
    "ControlRecordType",
    "PortForwarder",
    "Sendable",
    "SendableBuilder",
    "SendableRegistry",
    "getStackTrace",
    "getStackTraceDefault",
    "log"
]


class ControlRecordType():
    """
    Members:

      kControlStart

      kControlFinish

      kControlSetMetadata
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
    __members__: dict # value = {'kControlStart': <ControlRecordType.kControlStart: 0>, 'kControlFinish': <ControlRecordType.kControlFinish: 1>, 'kControlSetMetadata': <ControlRecordType.kControlSetMetadata: 2>}
    kControlFinish: wpiutil._wpiutil.ControlRecordType # value = <ControlRecordType.kControlFinish: 1>
    kControlSetMetadata: wpiutil._wpiutil.ControlRecordType # value = <ControlRecordType.kControlSetMetadata: 2>
    kControlStart: wpiutil._wpiutil.ControlRecordType # value = <ControlRecordType.kControlStart: 0>
    pass
class PortForwarder():
    """
    Forward ports to another host.  This is primarily useful for accessing
    Ethernet-connected devices from a computer tethered to the RoboRIO USB port.
    """
    def add(self, port: int, remoteHost: str, remotePort: int) -> None: 
        """
        Forward a local TCP port to a remote host and port.
        Note that local ports less than 1024 won't work as a normal user.

        :param port:       local port number
        :param remoteHost: remote IP address / DNS name
        :param remotePort: remote port number
        """
    @staticmethod
    def getInstance() -> PortForwarder: 
        """
        Get an instance of the PortForwarder class.

        This is a singleton to guarantee that there is only a single instance
        regardless of how many times GetInstance is called.
        """
    def remove(self, port: int) -> None: 
        """
        Stop TCP forwarding on a port.

        :param port: local port number
        """
    pass
class Sendable():
    """
    Interface for Sendable objects.
    """
    def __init__(self) -> None: ...
    def initSendable(self, builder: SendableBuilder) -> None: 
        """
        Initializes this Sendable object.

        :param builder: sendable builder
        """
    pass
class SendableBuilder():
    class BackendKind():
        """
        The backend kinds used for the sendable builder.

        Members:

          kUnknown

          kNetworkTables
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
        __members__: dict # value = {'kUnknown': <BackendKind.kUnknown: 0>, 'kNetworkTables': <BackendKind.kNetworkTables: 1>}
        kNetworkTables: wpiutil._wpiutil.SendableBuilder.BackendKind # value = <BackendKind.kNetworkTables: 1>
        kUnknown: wpiutil._wpiutil.SendableBuilder.BackendKind # value = <BackendKind.kUnknown: 0>
        pass
    def __init__(self) -> None: ...
    def addBooleanArrayProperty(self, key: str, getter: typing.Callable[[], typing.List[int]], setter: typing.Callable[[typing.List[int]], None]) -> None: 
        """
        Add a boolean array property.

        :param key:    property name
        :param getter: getter function (returns current value)
        :param setter: setter function (sets new value)
        """
    def addBooleanProperty(self, key: str, getter: typing.Callable[[], bool], setter: typing.Callable[[bool], None]) -> None: 
        """
        Add a boolean property.

        :param key:    property name
        :param getter: getter function (returns current value)
        :param setter: setter function (sets new value)
        """
    def addDoubleArrayProperty(self, key: str, getter: typing.Callable[[], typing.List[float]], setter: typing.Callable[[typing.List[float]], None]) -> None: 
        """
        Add a double array property.

        :param key:    property name
        :param getter: getter function (returns current value)
        :param setter: setter function (sets new value)
        """
    def addDoubleProperty(self, key: str, getter: typing.Callable[[], float], setter: typing.Callable[[float], None]) -> None: 
        """
        Add a double property.

        :param key:    property name
        :param getter: getter function (returns current value)
        :param setter: setter function (sets new value)
        """
    def addRawProperty(self, key: str, getter: typing.Callable[[], str], setter: typing.Callable[[str], None]) -> None: 
        """
        Add a raw property.

        :param key:    property name
        :param getter: getter function (returns current value)
        :param setter: setter function (sets new value)
        """
    def addSmallBooleanArrayProperty(self, key: str, getter: typing.Callable[[typing.List[int]], typing.List[int]], setter: typing.Callable[[typing.List[int]], None]) -> None: 
        """
        Add a boolean array property (SmallVector form).

        :param key:    property name
        :param getter: getter function (returns current value)
        :param setter: setter function (sets new value)
        """
    def addSmallDoubleArrayProperty(self, key: str, getter: typing.Callable[[typing.List[float]], typing.List[float]], setter: typing.Callable[[typing.List[float]], None]) -> None: 
        """
        Add a double array property (SmallVector form).

        :param key:    property name
        :param getter: getter function (returns current value)
        :param setter: setter function (sets new value)
        """
    def addSmallRawProperty(self, key: str, getter: typing.Callable[[typing.List[str]], str], setter: typing.Callable[[str], None]) -> None: 
        """
        Add a raw property (SmallVector form).

        :param key:    property name
        :param getter: getter function (returns current value)
        :param setter: setter function (sets new value)
        """
    def addSmallStringArrayProperty(self, key: str, getter: typing.Callable[[typing.List[str]], typing.List[str]], setter: typing.Callable[[typing.List[str]], None]) -> None: 
        """
        Add a string array property (SmallVector form).

        :param key:    property name
        :param getter: getter function (returns current value)
        :param setter: setter function (sets new value)
        """
    def addSmallStringProperty(self, key: str, getter: typing.Callable[[typing.List[str]], str], setter: typing.Callable[[str], None]) -> None: 
        """
        Add a string property (SmallString form).

        :param key:    property name
        :param getter: getter function (returns current value)
        :param setter: setter function (sets new value)
        """
    def addStringArrayProperty(self, key: str, getter: typing.Callable[[], typing.List[str]], setter: typing.Callable[[typing.List[str]], None]) -> None: 
        """
        Add a string array property.

        :param key:    property name
        :param getter: getter function (returns current value)
        :param setter: setter function (sets new value)
        """
    def addStringProperty(self, key: str, getter: typing.Callable[[], str], setter: typing.Callable[[str], None]) -> None: 
        """
        Add a string property.

        :param key:    property name
        :param getter: getter function (returns current value)
        :param setter: setter function (sets new value)
        """
    def clearProperties(self) -> None: 
        """
        Clear properties.
        """
    def getBackendKind(self) -> SendableBuilder.BackendKind: 
        """
        Gets the kind of backend being used.

        :returns: Backend kind
        """
    def isPublished(self) -> bool: 
        """
        Return whether this sendable has been published.

        :returns: True if it has been published, false if not.
        """
    def setActuator(self, value: bool) -> None: 
        """
        Set a flag indicating if this sendable should be treated as an actuator.
        By default this flag is false.

        :param value: true if actuator, false if not
        """
    def setSafeState(self, func: typing.Callable[[], None]) -> None: 
        """
        Set the function that should be called to set the Sendable into a safe
        state.  This is called when entering and exiting Live Window mode.

        :param func: function
        """
    def setSmartDashboardType(self, type: str) -> None: 
        """
        Set the string representation of the named data type that will be used
        by the smart dashboard for this sendable.

        :param type: data type
        """
    def update(self) -> None: 
        """
        Update the published values by calling the getters for all properties.
        """
    pass
class SendableRegistry():
    """
    The SendableRegistry class is the public interface for registering sensors
    and actuators for use on dashboards and LiveWindow.
    """
    @staticmethod
    @typing.overload
    def add(sendable: Sendable, moduleType: str, channel: int) -> None: 
        """
        Adds an object to the registry.

        :param sendable: object to add
        :param name:     component name

        Adds an object to the registry.

        :param sendable:   object to add
        :param moduleType: A string that defines the module name in the label for
                           the value
        :param channel:    The channel number the device is plugged into

        Adds an object to the registry.

        :param sendable:     object to add
        :param moduleType:   A string that defines the module name in the label for
                             the value
        :param moduleNumber: The number of the particular module type
        :param channel:      The channel number the device is plugged into

        Adds an object to the registry.

        :param sendable:  object to add
        :param subsystem: subsystem name
        :param name:      component name
        """
    @staticmethod
    @typing.overload
    def add(sendable: Sendable, moduleType: str, moduleNumber: int, channel: int) -> None: ...
    @staticmethod
    @typing.overload
    def add(sendable: Sendable, name: str) -> None: ...
    @staticmethod
    @typing.overload
    def add(sendable: Sendable, subsystem: str, name: str) -> None: ...
    @staticmethod
    def addChild(parent: Sendable, child: Sendable) -> None: 
        """
        Adds a child object to an object.  Adds the child object to the registry
        if it's not already present.

        :param parent: parent object
        :param child:  child object
        """
    @staticmethod
    @typing.overload
    def addLW(sendable: Sendable, moduleType: str, channel: int) -> None: 
        """
        Adds an object to the registry and LiveWindow.

        :param sendable: object to add
        :param name:     component name

        Adds an object to the registry and LiveWindow.

        :param sendable:   object to add
        :param moduleType: A string that defines the module name in the label for
                           the value
        :param channel:    The channel number the device is plugged into

        Adds an object to the registry and LiveWindow.

        :param sendable:     object to add
        :param moduleType:   A string that defines the module name in the label for
                             the value
        :param moduleNumber: The number of the particular module type
        :param channel:      The channel number the device is plugged into

        Adds an object to the registry and LiveWindow.

        :param sendable:  object to add
        :param subsystem: subsystem name
        :param name:      component name
        """
    @staticmethod
    @typing.overload
    def addLW(sendable: Sendable, moduleType: str, moduleNumber: int, channel: int) -> None: ...
    @staticmethod
    @typing.overload
    def addLW(sendable: Sendable, name: str) -> None: ...
    @staticmethod
    @typing.overload
    def addLW(sendable: Sendable, subsystem: str, name: str) -> None: ...
    @staticmethod
    def contains(sendable: Sendable) -> bool: 
        """
        Determines if an object is in the registry.

        :param sendable: object to check

        :returns: True if in registry, false if not.
        """
    @staticmethod
    def disableLiveWindow(sendable: Sendable) -> None: 
        """
        Disables LiveWindow for an object.

        :param sendable: object
        """
    @staticmethod
    def enableLiveWindow(sendable: Sendable) -> None: 
        """
        Enables LiveWindow for an object.

        :param sendable: object
        """
    @staticmethod
    def getName(sendable: Sendable) -> str: 
        """
        Gets the name of an object.

        :param sendable: object

        :returns: Name (empty if object is not in registry)
        """
    @staticmethod
    def getSendable(uid: int) -> Sendable: 
        """
        Get sendable object for a given unique id.

        :param uid: unique id

        :returns: sendable object (may be null)
        """
    @staticmethod
    def getSubsystem(sendable: Sendable) -> str: 
        """
        Gets the subsystem name of an object.

        :param sendable: object

        :returns: Subsystem name (empty if object is not in registry)
        """
    @staticmethod
    def getUniqueId(sendable: Sendable) -> int: 
        """
        Get unique id for an object.  Since objects can move, use this instead
        of storing Sendable* directly if ownership is in question.

        :param sendable: object

        :returns: unique id
        """
    @staticmethod
    def publish(sendableUid: int, builder: SendableBuilder) -> None: 
        """
        Publishes an object in the registry.

        :param sendableUid: sendable unique id
        :param builder:     publisher backend
        """
    @staticmethod
    def remove(sendable: Sendable) -> bool: 
        """
        Removes an object from the registry.

        :param sendable: object to remove

        :returns: true if the object was removed; false if it was not present
        """
    @staticmethod
    def setLiveWindowBuilderFactory(factory: typing.Callable[[], SendableBuilder]) -> None: 
        """
        Sets the factory for LiveWindow builders.

        :param factory: factory function
        """
    @staticmethod
    @typing.overload
    def setName(sendable: Sendable, moduleType: str, channel: int) -> None: 
        """
        Sets the name of an object.

        :param sendable: object
        :param name:     name

        Sets the name of an object with a channel number.

        :param sendable:   object
        :param moduleType: A string that defines the module name in the label for
                           the value
        :param channel:    The channel number the device is plugged into

        Sets the name of an object with a module and channel number.

        :param sendable:     object
        :param moduleType:   A string that defines the module name in the label for
                             the value
        :param moduleNumber: The number of the particular module type
        :param channel:      The channel number the device is plugged into

        Sets both the subsystem name and device name of an object.

        :param sendable:  object
        :param subsystem: subsystem name
        :param name:      device name
        """
    @staticmethod
    @typing.overload
    def setName(sendable: Sendable, moduleType: str, moduleNumber: int, channel: int) -> None: ...
    @staticmethod
    @typing.overload
    def setName(sendable: Sendable, name: str) -> None: ...
    @staticmethod
    @typing.overload
    def setName(sendable: Sendable, subsystem: str, name: str) -> None: ...
    @staticmethod
    def setSubsystem(sendable: Sendable, subsystem: str) -> None: 
        """
        Sets the subsystem name of an object.

        :param sendable:  object
        :param subsystem: subsystem name
        """
    @staticmethod
    def update(sendableUid: int) -> None: 
        """
        Updates published information from an object.

        :param sendableUid: sendable unique id
        """
    pass
def _setup_stack_trace_hook(arg0: object) -> None:
    pass
def getStackTrace(offset: int) -> str:
    """
    Get a stack trace, ignoring the first "offset" symbols.

    :param offset: The number of symbols at the top of the stack to ignore
    """
def getStackTraceDefault(offset: int) -> str:
    """
    The default implementation used for GetStackTrace().

    :param offset: The number of symbols at the top of the stack to ignore
    """
_st_cleanup: PyCapsule # value = <capsule object NULL>
