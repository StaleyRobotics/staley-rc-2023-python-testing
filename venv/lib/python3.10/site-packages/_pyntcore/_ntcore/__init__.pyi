from __future__ import annotations
import _pyntcore._ntcore
import typing
import _pyntcore._ntcore.NotifyFlags
import networktables
import wpiutil._wpiutil
import wpiutil._wpiutil.log

__all__ = [
    "ConnectionInfo",
    "ConnectionNotification",
    "EntryInfo",
    "EntryNotification",
    "LogMessage",
    "NTSendable",
    "NTSendableBuilder",
    "NetworkTable",
    "NetworkTableEntry",
    "NetworkTableType",
    "NetworkTablesInstance",
    "NotifyFlags",
    "Value",
    "startConnectionDataLog",
    "startEntryDataLog",
    "stopConnectionDataLog",
    "stopEntryDataLog"
]


class ConnectionInfo():
    """
    NetworkTables Connection Information
    """
    def __init__(self) -> None: ...
    @property
    def remote_id(self) -> str:
        """
        The remote identifier (as set on the remote node by
        NetworkTableInstance::SetNetworkIdentity() or nt::SetNetworkIdentity()).

        :type: str
        """
    @remote_id.setter
    def remote_id(self, arg0: str) -> None:
        """
        The remote identifier (as set on the remote node by
        NetworkTableInstance::SetNetworkIdentity() or nt::SetNetworkIdentity()).
        """
    @property
    def remote_ip(self) -> str:
        """
        The IP address of the remote node.

        :type: str
        """
    @remote_ip.setter
    def remote_ip(self, arg0: str) -> None:
        """
        The IP address of the remote node.
        """
    pass
class ConnectionNotification():
    """
    NetworkTables Connection Notification
    """
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, listener_: int, connected_: bool, conn_: ConnectionInfo) -> None: ...
    @property
    def conn(self) -> ConnectionInfo:
        """
        Connection info.

        :type: ConnectionInfo
        """
    @property
    def connected(self) -> bool:
        """
        True if event is due to connection being established.

        :type: bool
        """
    @connected.setter
    def connected(self, arg0: bool) -> None:
        """
        True if event is due to connection being established.
        """
    pass
class EntryInfo():
    """
    NetworkTables Entry Information
    """
    def __init__(self) -> None: ...
    @property
    def entry(self) -> int:
        """
        Entry handle

        :type: int
        """
    @entry.setter
    def entry(self, arg0: int) -> None:
        """
        Entry handle
        """
    @property
    def flags(self) -> int:
        """
        Entry flags

        :type: int
        """
    @flags.setter
    def flags(self, arg0: int) -> None:
        """
        Entry flags
        """
    @property
    def last_change(self) -> int:
        """
        Timestamp of last change to entry (type or value).

        :type: int
        """
    @last_change.setter
    def last_change(self, arg0: int) -> None:
        """
        Timestamp of last change to entry (type or value).
        """
    @property
    def name(self) -> str:
        """
        Entry name

        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        """
        Entry name
        """
    @property
    def type(self) -> NT_Type:
        """
        Entry type

        :type: NT_Type
        """
    @type.setter
    def type(self, arg0: NT_Type) -> None:
        """
        Entry type
        """
    pass
class EntryNotification():
    """
    NetworkTables Entry Notification
    """
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, listener_: int, entry_: int, name_: str, value_: Value, flags_: int) -> None: ...
    @property
    def name(self) -> str:
        """
        Entry name.

        :type: str
        """
    @property
    def value(self) -> Value:
        """
        The new value.

        :type: Value
        """
    pass
class LogMessage():
    """
    NetworkTables log message.
    """
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, logger_: int, level_: int, filename_: str, line_: int, message_: str) -> None: ...
    @property
    def filename(self) -> str:
        """
        :type: str
        """
    @filename.setter
    def filename(self, arg0: str) -> None:
        pass
    @property
    def level(self) -> int:
        """
        :type: int
        """
    @level.setter
    def level(self, arg0: int) -> None:
        pass
    @property
    def line(self) -> int:
        """
        :type: int
        """
    @line.setter
    def line(self, arg0: int) -> None:
        pass
    @property
    def message(self) -> str:
        """
        :type: str
        """
    @message.setter
    def message(self, arg0: str) -> None:
        pass
    pass
class NTSendable(wpiutil._wpiutil.Sendable):
    """
    Interface for NetworkTable Sendable objects.
    """
    def __init__(self) -> None: ...
    @typing.overload
    def initSendable(self, builder: NTSendableBuilder) -> None: 
        """
        Initializes this Sendable object.

        :param builder: sendable builder
        """
    @typing.overload
    def initSendable(self, builder: wpiutil._wpiutil.SendableBuilder) -> None: ...
    pass
class NTSendableBuilder(wpiutil._wpiutil.SendableBuilder):
    def __init__(self) -> None: ...
    def addValueProperty(self, key: str, getter: typing.Callable[[], Value], setter: typing.Callable[[Value], None]) -> None: 
        """
        Add a NetworkTableValue property.

        :param key:    property name
        :param getter: getter function (returns current value)
        :param setter: setter function (sets new value)
        """
    def getEntry(self, key: str) -> NetworkTableEntry: 
        """
        Add a property without getters or setters.  This can be used to get
        entry handles for the function called by SetUpdateTable().

        :param key: property name

        :returns: Network table entry
        """
    def getTable(self) -> NetworkTable: 
        """
        Get the network table.

        :returns: The network table
        """
    def setUpdateTable(self, func: typing.Callable[[], None]) -> None: 
        """
        Set the function that should be called to update the network table
        for things other than properties.  Note this function is not passed
        the network table object; instead it should use the entry handles
        returned by GetEntry().

        :param func: function
        """
    pass
class NetworkTable():
    """
    A network table that knows its subtable path.
    @ingroup ntcore_cpp_api
    """
    def __contains__(self, arg0: str) -> bool: ...
    @typing.overload
    def addEntryListener(self, key: str, listener: typing.Callable[[NetworkTable, str, NetworkTableEntry, Value, int], None], flags: int) -> int: 
        """
        Listen to keys only within this table.

        :param listener: listener to add
        :param flags:    EntryListenerFlags bitmask

        :returns: Listener handle

        Listen to a single key.

        :param key:      the key name
        :param listener: listener to add
        :param flags:    EntryListenerFlags bitmask

        :returns: Listener handle
        """
    @typing.overload
    def addEntryListener(self, listener: typing.Callable[[NetworkTable, str, NetworkTableEntry, Value, int], None], flags: int) -> int: ...
    def addSubTableListener(self, listener: typing.Callable[[NetworkTable, str, NetworkTable], None], localNotify: bool = False) -> int: 
        """
        Listen for sub-table creation.
        This calls the listener once for each newly created sub-table.
        It immediately calls the listener for any existing sub-tables.

        :param listener:    listener to add
        :param localNotify: notify local changes as well as remote

        :returns: Listener handle
        """
    @staticmethod
    def basenameKey(key: str) -> str: 
        """
        Gets the "base name" of a key. For example, "/foo/bar" becomes "bar".
        If the key has a trailing slash, returns an empty string.

        :param key: key

        :returns: base name
        """
    def clearFlags(self, key: str, flags: int) -> None: 
        """
        Clears flags on the specified key in this table. The key can
        not be null.

        :param key:   the key name
        :param flags: the flags to clear (bitmask)
        """
    def clearPersistent(self, key: str) -> None: 
        """
        Stop making a key's value persistent through program restarts.
        The key cannot be null.

        :param key: the key name
        """
    def containsKey(self, key: str) -> bool: 
        """
        Determines whether the given key is in this table.

        :param key: the key to search for

        :returns: true if the table as a value assigned to the given key
        """
    def containsSubTable(self, key: str) -> bool: 
        """
        Determines whether there exists a non-empty subtable for this key
        in this table.

        :param key: the key to search for

        :returns: true if there is a subtable with the key which contains at least
                  one key/subtable of its own
        """
    def delete(self, key: str) -> None: 
        """
        Deletes the specified key in this table.

        :param key: the key name
        """
    def getBoolean(self, key: str, defaultValue: object) -> object: 
        """
        Gets the boolean associated with the given name. If the key does not
        exist or is of different type, it will return the default value.

        :param key:          the key to look up
        :param defaultValue: the value to be returned if no value is found

        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
    def getBooleanArray(self, key: str, defaultValue: object) -> object: 
        """
        Returns the boolean array the key maps to. If the key does not exist or is
        of different type, it will return the default value.

        :param key:          the key to look up
        :param defaultValue: the value to be returned if no value is found

        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
                  
                  @note This makes a copy of the array.  If the overhead of this is a
                  concern, use GetValue() instead.
                  
                  @note The returned array is std::vector<int> instead of std::vector<bool>
                  because std::vector<bool> is special-cased in C++.  0 is false, any
                  non-zero value is true.
        """
    def getEntry(self, key: str) -> NetworkTableEntry: 
        """
        Gets the entry for a subkey.

        :param key: the key name

        :returns: Network table entry.
        """
    def getFlags(self, key: str) -> int: 
        """
        Returns the flags for the specified key.

        :param key: the key name

        :returns: the flags, or 0 if the key is not defined
        """
    @staticmethod
    def getHierarchy(key: str) -> typing.List[str]: 
        """
        Gets a list of the names of all the super tables of a given key. For
        example, the key "/foo/bar/baz" has a hierarchy of "/", "/foo",
        "/foo/bar", and "/foo/bar/baz".

        :param key: the key

        :returns: List of super tables
        """
    def getInstance(self) -> NetworkTablesInstance: 
        """
        Gets the instance for the table.

        :returns: Instance
        """
    def getKeys(self, types: int = 0) -> typing.List[str]: 
        """
        Gets all keys in the table (not including sub-tables).

        :param types: bitmask of types; 0 is treated as a "don't care".

        :returns: keys currently in the table
        """
    def getNumber(self, key: str, defaultValue: object) -> object: 
        """
        Gets the number associated with the given name.

        :param key:          the key to look up
        :param defaultValue: the value to be returned if no value is found

        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
    def getNumberArray(self, key: str, defaultValue: object) -> object: 
        """
        Returns the number array the key maps to. If the key does not exist or is
        of different type, it will return the default value.

        :param key:          the key to look up
        :param defaultValue: the value to be returned if no value is found

        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
                  
                  @note This makes a copy of the array.  If the overhead of this is a
                  concern, use GetValue() instead.
        """
    def getPath(self) -> str: 
        """
        Gets the full path of this table.  Does not include the trailing "/".

        :returns: The path (e.g "", "/foo").
        """
    def getRaw(self, key: str, defaultValue: object) -> object: 
        """
        Returns the raw value (byte array) the key maps to. If the key does not
        exist or is of different type, it will return the default value.

        :param key:          the key to look up
        :param defaultValue: the value to be returned if no value is found

        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
                  
                  @note This makes a copy of the raw contents.  If the overhead of this is a
                  concern, use GetValue() instead.
        """
    def getString(self, key: str, defaultValue: object) -> object: 
        """
        Gets the string associated with the given name. If the key does not
        exist or is of different type, it will return the default value.

        :param key:          the key to look up
        :param defaultValue: the value to be returned if no value is found

        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
    def getStringArray(self, key: str, defaultValue: object) -> object: 
        """
        Returns the string array the key maps to. If the key does not exist or is
        of different type, it will return the default value.

        :param key:          the key to look up
        :param defaultValue: the value to be returned if no value is found

        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
                  
                  @note This makes a copy of the array.  If the overhead of this is a
                  concern, use GetValue() instead.
        """
    def getSubTable(self, key: str) -> NetworkTable: 
        """
        Returns the table at the specified key. If there is no table at the
        specified key, it will create a new table

        :param key: the key name

        :returns: the networktable to be returned
        """
    def getSubTables(self) -> typing.List[str]: 
        """
        Gets the names of all subtables in the table.

        :returns: subtables currently in the table
        """
    def getValue(self, key: str, value: object) -> object: ...
    def isPersistent(self, key: str) -> bool: 
        """
        Returns whether the value is persistent through program restarts.
        The key cannot be null.

        :param key: the key name
        """
    def loadEntries(self, filename: str, warn: typing.Callable[[int, str], None]) -> str: 
        """
        Load table values from a file.  The file format used is identical to
        that used for SavePersistent / LoadPersistent.

        :param filename: filename
        :param warn:     callback function for warnings

        :returns: error string, or nullptr if successful
        """
    @staticmethod
    def normalizeKey(key: str, withLeadingSlash: bool = True) -> str: 
        """
        Normalizes an network table key to contain no consecutive slashes and
        optionally start with a leading slash. For example:

        <pre><code>
        normalizeKey("/foo/bar", true)  == "/foo/bar"
        normalizeKey("foo/bar", true)   == "/foo/bar"
        normalizeKey("/foo/bar", false) == "foo/bar"
        normalizeKey("foo//bar", false) == "foo/bar"
        </code></pre>

        :param key:              the key to normalize
        :param withLeadingSlash: whether or not the normalized key should begin
                                 with a leading slash

        :returns: normalized key
        """
    def putBoolean(self, key: str, value: bool) -> bool: 
        """
        Put a boolean in the table

        :param key:   the key to be assigned to
        :param value: the value that will be assigned

        :returns: False if the table key already exists with a different type
        """
    def putBooleanArray(self, key: str, value: typing.List[int]) -> bool: 
        """
        Put a boolean array in the table

        :param key:   the key to be assigned to
        :param value: the value that will be assigned

        :returns: False if the table key already exists with a different type
                  
                  @note The array must be of int's rather than of bool's because
                  std::vector<bool> is special-cased in C++.  0 is false, any
                  non-zero value is true.
        """
    def putNumber(self, key: str, value: float) -> bool: 
        """
        Put a number in the table

        :param key:   the key to be assigned to
        :param value: the value that will be assigned

        :returns: False if the table key already exists with a different type
        """
    def putNumberArray(self, key: str, value: typing.List[float]) -> bool: 
        """
        Put a number array in the table

        :param key:   the key to be assigned to
        :param value: the value that will be assigned

        :returns: False if the table key already exists with a different type
        """
    def putRaw(self, key: str, value: str) -> bool: 
        """
        Put a raw value (byte array) in the table

        :param key:   the key to be assigned to
        :param value: the value that will be assigned

        :returns: False if the table key already exists with a different type
        """
    def putString(self, key: str, value: str) -> bool: 
        """
        Put a string in the table

        :param key:   the key to be assigned to
        :param value: the value that will be assigned

        :returns: False if the table key already exists with a different type
        """
    def putStringArray(self, key: str, value: typing.List[str]) -> bool: 
        """
        Put a string array in the table

        :param key:   the key to be assigned to
        :param value: the value that will be assigned

        :returns: False if the table key already exists with a different type
        """
    @typing.overload
    def putValue(self, key: str, value: Value) -> bool: 
        """
        Put a value in the table

        :param key:   the key to be assigned to
        :param value: the value that will be assigned

        :returns: False if the table key already exists with a different type
        """
    @typing.overload
    def putValue(self, key: str, value: bool) -> bool: ...
    @typing.overload
    def putValue(self, key: str, value: bytes) -> bool: ...
    @typing.overload
    def putValue(self, key: str, value: float) -> bool: ...
    @typing.overload
    def putValue(self, key: str, value: sequence) -> bool: ...
    @typing.overload
    def putValue(self, key: str, value: str) -> bool: ...
    def removeEntryListener(self, listener: int) -> None: 
        """
        Remove an entry listener.

        :param listener: listener handle
        """
    def removeTableListener(self, listener: int) -> None: 
        """
        Remove a sub-table listener.

        :param listener: listener handle
        """
    def saveEntries(self, filename: str) -> str: 
        """
        Save table values to a file.  The file format used is identical to
        that used for SavePersistent.

        :param filename: filename

        :returns: error string, or nullptr if successful
        """
    def setDefaultBoolean(self, key: str, defaultValue: bool) -> bool: 
        """
        Gets the current value in the table, setting it if it does not exist.

        :param key:          the key
        :param defaultValue: the default value to set if key doesn't exist.

        :returns: False if the table key exists with a different type
        """
    def setDefaultBooleanArray(self, key: str, defaultValue: typing.List[int]) -> bool: 
        """
        Gets the current value in the table, setting it if it does not exist.

        :param key:          the key
        :param defaultValue: the default value to set if key doesn't exist.

        :returns: False if the table key exists with a different type
        """
    def setDefaultNumber(self, key: str, defaultValue: float) -> bool: 
        """
        Gets the current value in the table, setting it if it does not exist.

        :param key:          the key
        :param defaultValue: the default value to set if key doesn't exist.

        :returns: False if the table key exists with a different type
        """
    def setDefaultNumberArray(self, key: str, defaultValue: typing.List[float]) -> bool: 
        """
        Gets the current value in the table, setting it if it does not exist.

        :param key:          the key
        :param defaultValue: the default value to set if key doesn't exist.

        :returns: False if the table key exists with a different type
        """
    def setDefaultRaw(self, key: str, defaultValue: str) -> bool: 
        """
        Gets the current value in the table, setting it if it does not exist.

        :param key:          the key
        :param defaultValue: the default value to set if key doesn't exist.

        :returns: False if the table key exists with a different type
        """
    def setDefaultString(self, key: str, defaultValue: str) -> bool: 
        """
        Gets the current value in the table, setting it if it does not exist.

        :param key:          the key
        :param defaultValue: the default value to set if key doesn't exist.

        :returns: False if the table key exists with a different type
        """
    def setDefaultStringArray(self, key: str, defaultValue: typing.List[str]) -> bool: 
        """
        Gets the current value in the table, setting it if it does not exist.

        :param key:          the key
        :param defaultValue: the default value to set if key doesn't exist.

        :returns: False if the table key exists with a different type
        """
    @typing.overload
    def setDefaultValue(self, key: str, defaultValue: Value) -> bool: 
        """
        Gets the current value in the table, setting it if it does not exist.

        :param key:          the key
        :param defaultValue: the default value to set if key doesn't exist.

        :returns: False if the table key exists with a different type
        """
    @typing.overload
    def setDefaultValue(self, key: str, value: bool) -> bool: ...
    @typing.overload
    def setDefaultValue(self, key: str, value: bytes) -> bool: ...
    @typing.overload
    def setDefaultValue(self, key: str, value: float) -> bool: ...
    @typing.overload
    def setDefaultValue(self, key: str, value: sequence) -> bool: ...
    @typing.overload
    def setDefaultValue(self, key: str, value: str) -> bool: ...
    def setFlags(self, key: str, flags: int) -> None: 
        """
        Sets flags on the specified key in this table. The key can
        not be null.

        :param key:   the key name
        :param flags: the flags to set (bitmask)
        """
    def setPersistent(self, key: str) -> None: 
        """
        Makes a key's value persistent through program restarts.

        :param key: the key to make persistent
        """
    PATH_SEPARATOR_CHAR = '/'
    pass
class NetworkTableEntry():
    """
    NetworkTables Entry
    @ingroup ntcore_cpp_api
    """
    class Flags():
        """
        Flag values (as returned by GetFlags()).

        Members:

          kPersistent
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
        __members__: dict # value = {'kPersistent': <Flags.kPersistent: 1>}
        kPersistent: _pyntcore._ntcore.NetworkTableEntry.Flags # value = <Flags.kPersistent: 1>
        pass
    def __eq__(self, arg0: NetworkTableEntry) -> bool: 
        """
        Equality operator.  Returns true if both instances refer to the same
        native handle.
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct invalid instance.

        Construct from native handle.

        :param handle: Native handle
        """
    @typing.overload
    def __init__(self, handle: int) -> None: ...
    def __ne__(self, arg0: NetworkTableEntry) -> bool: 
        """
        Inequality operator.
        """
    def addListener(self, callback: typing.Callable[[EntryNotification], None], flags: int) -> int: 
        """
        Add a listener for changes to this entry.

        :param callback: listener to add
        :param flags:    NotifyKind bitmask

        :returns: Listener handle
        """
    def clearFlags(self, flags: int) -> None: 
        """
        Clears flags.

        :param flags: the flags to clear (bitmask)
        """
    def clearPersistent(self) -> None: 
        """
        Stop making value persistent through program restarts.
        """
    def delete(self) -> None: 
        """
        Deletes the entry.
        """
    def exists(self) -> bool: 
        """
        Determines if the entry currently exists.

        :returns: True if the entry exists, false otherwise.
        """
    def forceSetBoolean(self, value: bool) -> None: 
        """
        Sets the entry's value.  If the value is of different type, the type is
        changed to match the new value.

        :param value: the value to set
        """
    def forceSetBooleanArray(self, value: typing.List[bool]) -> None: 
        """
        Sets the entry's value.  If the value is of different type, the type is
        changed to match the new value.

        :param value: the value to set
        """
    def forceSetDouble(self, value: float) -> None: 
        """
        Sets the entry's value.  If the value is of different type, the type is
        changed to match the new value.

        :param value: the value to set
        """
    def forceSetDoubleArray(self, value: typing.List[float]) -> None: 
        """
        Sets the entry's value.  If the value is of different type, the type is
        changed to match the new value.

        :param value: the value to set
        """
    def forceSetRaw(self, value: str) -> None: 
        """
        Sets the entry's value.  If the value is of different type, the type is
        changed to match the new value.

        :param value: the value to set
        """
    def forceSetString(self, value: str) -> None: 
        """
        Sets the entry's value.  If the value is of different type, the type is
        changed to match the new value.

        :param value: the value to set
        """
    def forceSetStringArray(self, value: typing.List[str]) -> None: 
        """
        Sets the entry's value.  If the value is of different type, the type is
        changed to match the new value.

        :param value: the value to set
        """
    @typing.overload
    def forceSetValue(self, value: Value) -> None: 
        """
        Sets the entry's value.  If the value is of different type, the type is
        changed to match the new value.

        :param value: the value to set
        """
    @typing.overload
    def forceSetValue(self, value: bool) -> None: ...
    @typing.overload
    def forceSetValue(self, value: bytes) -> None: ...
    @typing.overload
    def forceSetValue(self, value: float) -> None: ...
    @typing.overload
    def forceSetValue(self, value: sequence) -> None: ...
    @typing.overload
    def forceSetValue(self, value: str) -> None: ...
    def getBoolean(self, defaultValue: object) -> object: 
        """
        Gets the entry's value as a boolean. If the entry does not exist or is of
        different type, it will return the default value.

        :param defaultValue: the value to be returned if no value is found

        :returns: the entry's value or the given default value
        """
    def getBooleanArray(self, defaultValue: object) -> object: 
        """
        Gets the entry's value as a boolean array. If the entry does not exist
        or is of different type, it will return the default value.

        :param defaultValue: the value to be returned if no value is found

        :returns: the entry's value or the given default value
                  
                  @note This makes a copy of the array.  If the overhead of this is a
                  concern, use GetValue() instead.
                  
                  @note The returned array is std::vector<int> instead of std::vector<bool>
                  because std::vector<bool> is special-cased in C++.  0 is false, any
                  non-zero value is true.
        """
    def getDouble(self, defaultValue: object) -> object: 
        """
        Gets the entry's value as a double. If the entry does not exist or is of
        different type, it will return the default value.

        :param defaultValue: the value to be returned if no value is found

        :returns: the entry's value or the given default value
        """
    def getDoubleArray(self, defaultValue: object) -> object: 
        """
        Gets the entry's value as a double array. If the entry does not exist
        or is of different type, it will return the default value.

        :param defaultValue: the value to be returned if no value is found

        :returns: the entry's value or the given default value
                  
                  @note This makes a copy of the array.  If the overhead of this is a
                  concern, use GetValue() instead.
        """
    def getFlags(self) -> int: 
        """
        Returns the flags.

        :returns: the flags (bitmask)
        """
    def getHandle(self) -> int: 
        """
        Gets the native handle for the entry.

        :returns: Native handle
        """
    def getInfo(self) -> EntryInfo: 
        """
        Gets combined information about the entry.

        :returns: Entry information
        """
    def getInstance(self) -> NetworkTablesInstance: 
        """
        Gets the instance for the entry.

        :returns: Instance
        """
    def getLastChange(self) -> int: 
        """
        Gets the last time the entry's value was changed.

        :returns: Entry last change time
        """
    def getName(self) -> str: 
        """
        Gets the name of the entry (the key).

        :returns: the entry's name
        """
    def getRaw(self, defaultValue: object) -> object: 
        """
        Gets the entry's value as a raw. If the entry does not exist or is of
        different type, it will return the default value.

        :param defaultValue: the value to be returned if no value is found

        :returns: the entry's value or the given default value
        """
    def getString(self, defaultValue: object) -> object: 
        """
        Gets the entry's value as a string. If the entry does not exist or is of
        different type, it will return the default value.

        :param defaultValue: the value to be returned if no value is found

        :returns: the entry's value or the given default value
        """
    def getStringArray(self, defaultValue: object) -> object: 
        """
        Gets the entry's value as a string array. If the entry does not exist
        or is of different type, it will return the default value.

        :param defaultValue: the value to be returned if no value is found

        :returns: the entry's value or the given default value
                  
                  @note This makes a copy of the array.  If the overhead of this is a
                  concern, use GetValue() instead.
        """
    def getType(self) -> NetworkTableType: 
        """
        Gets the type of the entry.

        :returns: the entry's type
        """
    def getValue(self) -> Value: 
        """
        Gets the entry's value. If the entry does not exist, returns nullptr.

        :returns: the entry's value or nullptr if it does not exist.
        """
    def isPersistent(self) -> bool: 
        """
        Returns whether the value is persistent through program restarts.

        :returns: True if the value is persistent.
        """
    def removeListener(self, entry_listener: int) -> None: 
        """
        Remove an entry listener.

        :param entry_listener: Listener handle to remove
        """
    def setBoolean(self, value: bool) -> bool: 
        """
        Sets the entry's value.

        :param value: the value to set

        :returns: False if the entry exists with a different type
        """
    def setBooleanArray(self, value: typing.List[bool]) -> bool: 
        """
        Sets the entry's value.

        :param value: the value to set

        :returns: False if the entry exists with a different type
        """
    def setDefaultBoolean(self, defaultValue: bool) -> bool: 
        """
        Sets the entry's value if it does not exist.

        :param defaultValue: the default value to set

        :returns: False if the entry exists with a different type
        """
    def setDefaultBooleanArray(self, defaultValue: typing.List[int]) -> bool: 
        """
        Sets the entry's value if it does not exist.

        :param defaultValue: the default value to set

        :returns: False if the entry exists with a different type
        """
    def setDefaultDouble(self, defaultValue: float) -> bool: 
        """
        Sets the entry's value if it does not exist.

        :param defaultValue: the default value to set

        :returns: False if the entry exists with a different type
        """
    def setDefaultDoubleArray(self, defaultValue: typing.List[float]) -> bool: 
        """
        Sets the entry's value if it does not exist.

        :param defaultValue: the default value to set

        :returns: False if the entry exists with a different type
        """
    def setDefaultRaw(self, defaultValue: str) -> bool: 
        """
        Sets the entry's value if it does not exist.

        :param defaultValue: the default value to set

        :returns: False if the entry exists with a different type
        """
    def setDefaultString(self, defaultValue: str) -> bool: 
        """
        Sets the entry's value if it does not exist.

        :param defaultValue: the default value to set

        :returns: False if the entry exists with a different type
        """
    def setDefaultStringArray(self, defaultValue: typing.List[str]) -> bool: 
        """
        Sets the entry's value if it does not exist.

        :param defaultValue: the default value to set

        :returns: False if the entry exists with a different type
        """
    @typing.overload
    def setDefaultValue(self, value: Value) -> bool: 
        """
        Sets the entry's value if it does not exist.

        :param value: the default value to set

        :returns: False if the entry exists with a different type
        """
    @typing.overload
    def setDefaultValue(self, value: bool) -> bool: ...
    @typing.overload
    def setDefaultValue(self, value: bytes) -> bool: ...
    @typing.overload
    def setDefaultValue(self, value: float) -> bool: ...
    @typing.overload
    def setDefaultValue(self, value: sequence) -> bool: ...
    @typing.overload
    def setDefaultValue(self, value: str) -> bool: ...
    def setDouble(self, value: float) -> bool: 
        """
        Sets the entry's value.

        :param value: the value to set

        :returns: False if the entry exists with a different type
        """
    def setDoubleArray(self, value: typing.List[float]) -> bool: 
        """
        Sets the entry's value.

        :param value: the value to set

        :returns: False if the entry exists with a different type
        """
    def setFlags(self, flags: int) -> None: 
        """
        Sets flags.

        :param flags: the flags to set (bitmask)
        """
    def setPersistent(self) -> None: 
        """
        Make value persistent through program restarts.
        """
    def setRaw(self, value: str) -> bool: 
        """
        Sets the entry's value.

        :param value: the value to set

        :returns: False if the entry exists with a different type
        """
    def setString(self, value: str) -> bool: 
        """
        Sets the entry's value.

        :param value: the value to set

        :returns: False if the entry exists with a different type
        """
    def setStringArray(self, value: typing.List[str]) -> bool: 
        """
        Sets the entry's value.

        :param value: the value to set

        :returns: False if the entry exists with a different type
        """
    @typing.overload
    def setValue(self, value: Value) -> bool: 
        """
        Sets the entry's value.

        :param value: the value to set

        :returns: False if the entry exists with a different type
        """
    @typing.overload
    def setValue(self, value: bool) -> bool: ...
    @typing.overload
    def setValue(self, value: bytes) -> bool: ...
    @typing.overload
    def setValue(self, value: float) -> bool: ...
    @typing.overload
    def setValue(self, value: sequence) -> bool: ...
    @typing.overload
    def setValue(self, value: str) -> bool: ...
    @property
    def value(self) -> object:
        """
        :type: object
        """
    __hash__ = None
    pass
class NetworkTableType():
    """
    NetworkTable entry type.
    @ingroup ntcore_cpp_api

    Members:

      kUnassigned

      kBoolean

      kDouble

      kString

      kRaw

      kBooleanArray

      kDoubleArray

      kStringArray

      kRpc
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
    __members__: dict # value = {'kUnassigned': <NetworkTableType.kUnassigned: 0>, 'kBoolean': <NetworkTableType.kBoolean: 1>, 'kDouble': <NetworkTableType.kDouble: 2>, 'kString': <NetworkTableType.kString: 4>, 'kRaw': <NetworkTableType.kRaw: 8>, 'kBooleanArray': <NetworkTableType.kBooleanArray: 16>, 'kDoubleArray': <NetworkTableType.kDoubleArray: 32>, 'kStringArray': <NetworkTableType.kStringArray: 64>, 'kRpc': <NetworkTableType.kRpc: 128>}
    kBoolean: _pyntcore._ntcore.NetworkTableType # value = <NetworkTableType.kBoolean: 1>
    kBooleanArray: _pyntcore._ntcore.NetworkTableType # value = <NetworkTableType.kBooleanArray: 16>
    kDouble: _pyntcore._ntcore.NetworkTableType # value = <NetworkTableType.kDouble: 2>
    kDoubleArray: _pyntcore._ntcore.NetworkTableType # value = <NetworkTableType.kDoubleArray: 32>
    kRaw: _pyntcore._ntcore.NetworkTableType # value = <NetworkTableType.kRaw: 8>
    kRpc: _pyntcore._ntcore.NetworkTableType # value = <NetworkTableType.kRpc: 128>
    kString: _pyntcore._ntcore.NetworkTableType # value = <NetworkTableType.kString: 4>
    kStringArray: _pyntcore._ntcore.NetworkTableType # value = <NetworkTableType.kStringArray: 64>
    kUnassigned: _pyntcore._ntcore.NetworkTableType # value = <NetworkTableType.kUnassigned: 0>
    pass
class NetworkTablesInstance():
    """
    NetworkTables Instance.

    Instances are completely independent from each other.  Table operations on
    one instance will not be visible to other instances unless the instances are
    connected via the network.  The main limitation on instances is that you
    cannot have two servers on the same network port.  The main utility of
    instances is for unit testing, but they can also enable one program to
    connect to two different NetworkTables networks.

    The global "default" instance (as returned by GetDefault()) is
    always available, and is intended for the common case when there is only
    a single NetworkTables instance being used in the program.  The
    default instance cannot be destroyed.

    Additional instances can be created with the Create() function.
    Instances are not reference counted or RAII.  Instead, they must be
    explicitly destroyed (with Destroy()).

    @ingroup ntcore_cpp_api
    """
    class LogLevel():
        """
        Logging levels (as used by SetLogger()).

        Members:

          kLogCritical

          kLogError

          kLogWarning

          kLogInfo

          kLogDebug

          kLogDebug1

          kLogDebug2

          kLogDebug3

          kLogDebug4
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
        __members__: dict # value = {'kLogCritical': <LogLevel.kLogCritical: 50>, 'kLogError': <LogLevel.kLogError: 40>, 'kLogWarning': <LogLevel.kLogWarning: 30>, 'kLogInfo': <LogLevel.kLogInfo: 20>, 'kLogDebug': <LogLevel.kLogDebug: 10>, 'kLogDebug1': <LogLevel.kLogDebug1: 9>, 'kLogDebug2': <LogLevel.kLogDebug2: 8>, 'kLogDebug3': <LogLevel.kLogDebug3: 7>, 'kLogDebug4': <LogLevel.kLogDebug4: 6>}
        kLogCritical: _pyntcore._ntcore.NetworkTablesInstance.LogLevel # value = <LogLevel.kLogCritical: 50>
        kLogDebug: _pyntcore._ntcore.NetworkTablesInstance.LogLevel # value = <LogLevel.kLogDebug: 10>
        kLogDebug1: _pyntcore._ntcore.NetworkTablesInstance.LogLevel # value = <LogLevel.kLogDebug1: 9>
        kLogDebug2: _pyntcore._ntcore.NetworkTablesInstance.LogLevel # value = <LogLevel.kLogDebug2: 8>
        kLogDebug3: _pyntcore._ntcore.NetworkTablesInstance.LogLevel # value = <LogLevel.kLogDebug3: 7>
        kLogDebug4: _pyntcore._ntcore.NetworkTablesInstance.LogLevel # value = <LogLevel.kLogDebug4: 6>
        kLogError: _pyntcore._ntcore.NetworkTablesInstance.LogLevel # value = <LogLevel.kLogError: 40>
        kLogInfo: _pyntcore._ntcore.NetworkTablesInstance.LogLevel # value = <LogLevel.kLogInfo: 20>
        kLogWarning: _pyntcore._ntcore.NetworkTablesInstance.LogLevel # value = <LogLevel.kLogWarning: 30>
        pass
    class NetworkMode():
        """
        Client/server mode flag values (as returned by GetNetworkMode()).
        This is a bitmask.

        Members:

          kNetModeNone

          kNetModeServer

          kNetModeClient

          kNetModeStarting

          kNetModeFailure

          kNetModeLocal
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
        __members__: dict # value = {'kNetModeNone': <NetworkMode.kNetModeNone: 0>, 'kNetModeServer': <NetworkMode.kNetModeServer: 1>, 'kNetModeClient': <NetworkMode.kNetModeClient: 2>, 'kNetModeStarting': <NetworkMode.kNetModeStarting: 4>, 'kNetModeFailure': <NetworkMode.kNetModeFailure: 8>, 'kNetModeLocal': <NetworkMode.kNetModeLocal: 16>}
        kNetModeClient: _pyntcore._ntcore.NetworkTablesInstance.NetworkMode # value = <NetworkMode.kNetModeClient: 2>
        kNetModeFailure: _pyntcore._ntcore.NetworkTablesInstance.NetworkMode # value = <NetworkMode.kNetModeFailure: 8>
        kNetModeLocal: _pyntcore._ntcore.NetworkTablesInstance.NetworkMode # value = <NetworkMode.kNetModeLocal: 16>
        kNetModeNone: _pyntcore._ntcore.NetworkTablesInstance.NetworkMode # value = <NetworkMode.kNetModeNone: 0>
        kNetModeServer: _pyntcore._ntcore.NetworkTablesInstance.NetworkMode # value = <NetworkMode.kNetModeServer: 1>
        kNetModeStarting: _pyntcore._ntcore.NetworkTablesInstance.NetworkMode # value = <NetworkMode.kNetModeStarting: 4>
        pass
    def __eq__(self, arg0: NetworkTablesInstance) -> bool: 
        """
        Equality operator.  Returns true if both instances refer to the same
        native handle.
        """
    def __ne__(self, arg0: NetworkTablesInstance) -> bool: 
        """
        Inequality operator.
        """
    def addConnectionListener(self, callback: typing.Callable[[bool, ConnectionInfo], None], immediateNotify: bool) -> None: 
        """
        Add a connection listener.

        :param callback:         listener to add
        :param immediate_notify: notify listener of all existing connections

        :returns: Listener handle
        """
    @typing.overload
    def addEntryListener(self, listener: typing.Callable[[str, object, int], None], immediateNotify: bool = True, localNotify: bool = True, paramIsNew: bool = True) -> int: 
        """
        Add a listener for all entries starting with a certain prefix.

        :param prefix:   UTF-8 string prefix
        :param callback: listener to add
        :param flags:    EntryListenerFlags bitmask

        :returns: Listener handle
        """
    @typing.overload
    def addEntryListener(self, prefix: str, callback: typing.Callable[[EntryNotification], None], flags: int) -> int: ...
    def addLogger(self, func: typing.Callable[[LogMessage], None], minLevel: int, maxLevel: int) -> int: 
        """
        Add logger callback function.  By default, log messages are sent to stderr;
        this function sends log messages with the specified levels to the provided
        callback function instead.  The callback function will only be called for
        log messages with level greater than or equal to minLevel and less than or
        equal to maxLevel; messages outside this range will be silently ignored.

        :param func:     log callback function
        :param minLevel: minimum log level
        :param maxLevel: maximum log level

        :returns: Logger handle
        """
    @staticmethod
    def create() -> NetworkTablesInstance: 
        """
        Create an instance.

        :returns: Newly created instance
        """
    def deleteAllEntries(self) -> None: 
        """
        Deletes ALL keys in ALL subtables (except persistent values).
        Use with caution!
        """
    @staticmethod
    def destroy(inst: NetworkTablesInstance) -> None: 
        """
        Destroys an instance (note: this has global effect).

        :param inst: Instance
        """
    def flush(self) -> None: 
        """
        Flushes all updated values immediately to the network.
        @note This is rate-limited to protect the network from flooding.
        This is primarily useful for synchronizing network updates with
        user code.
        """
    def getConnections(self) -> typing.List[ConnectionInfo]: 
        """
        Get information on the currently established network connections.
        If operating as a client, this will return either zero or one values.

        :returns: array of connection information
        """
    @staticmethod
    def getDefault() -> NetworkTablesInstance: 
        """
        Get global default instance.

        :returns: Global default instance
        """
    def getEntries(self, prefix: str, types: int) -> typing.List[NetworkTableEntry]: 
        """
        Get entries starting with the given prefix.

        The results are optionally filtered by string prefix and entry type to
        only return a subset of all entries.

        :param prefix: entry name required prefix; only entries whose name
                       starts with this string are returned
        :param types:  bitmask of types; 0 is treated as a "don't care"

        :returns: Array of entries.
        """
    def getEntry(self, name: str) -> NetworkTableEntry: 
        """
        Gets the entry for a key.

        :param name: Key

        :returns: Network table entry.
        """
    def getEntryInfo(self, prefix: str, types: int) -> typing.List[EntryInfo]: 
        """
        Get information about entries starting with the given prefix.

        The results are optionally filtered by string prefix and entry type to
        only return a subset of all entries.

        :param prefix: entry name required prefix; only entries whose name
                       starts with this string are returned
        :param types:  bitmask of types; 0 is treated as a "don't care"

        :returns: Array of entry information.
        """
    def getGlobalAutoUpdateValue(self, arg0: str, arg1: handle, arg2: bool) -> NetworkTableEntry: ...
    def getGlobalTable(self) -> NetworkTable: ...
    def getHandle(self) -> int: 
        """
        Gets the native handle for the entry.

        :returns: Native handle
        """
    def getNetworkMode(self) -> int: 
        """
        Get the current network mode.

        :returns: Bitmask of NetworkMode.
        """
    def getRemoteAddress(self) -> typing.Optional[str]: ...
    def getTable(self, key: str) -> NetworkTable: 
        """
        Gets the table with the specified key.

        :param key: the key name

        :returns: The network table
        """
    def initialize(self, server: str = '') -> None: ...
    def isConnected(self) -> bool: 
        """
        Return whether or not the instance is connected to another node.

        :returns: True if connected.
        """
    def isServer(self) -> bool: ...
    def loadEntries(self, filename: str, prefix: str, warn: typing.Callable[[int, str], None]) -> str: 
        """
        Load table values from a file.  The file format used is identical to
        that used for SavePersistent / LoadPersistent.

        :param filename: filename
        :param prefix:   load only keys starting with this prefix
        :param warn:     callback function for warnings

        :returns: error string, or nullptr if successful
        """
    def loadPersistent(self, filename: str, warn: typing.Callable[[int, str], None]) -> str: 
        """
        Load persistent values from a file.  The server automatically does this
        at startup, but this function provides a way to restore persistent values
        in the same format from a file at any time on either a client or a server.

        :param filename: filename
        :param warn:     callback function for warnings

        :returns: error string, or nullptr if successful
        """
    @staticmethod
    def removeConnectionListener(conn_listener: int) -> None: 
        """
        Remove a connection listener.

        :param conn_listener: Listener handle to remove
        """
    @staticmethod
    def removeEntryListener(entry_listener: int) -> None: 
        """
        Remove an entry listener.

        :param entry_listener: Listener handle to remove
        """
    @staticmethod
    def removeLogger(logger: int) -> None: 
        """
        Remove a logger.

        :param logger: Logger handle to remove
        """
    def saveEntries(self, filename: str, prefix: str) -> str: 
        """
        Save table values to a file.  The file format used is identical to
        that used for SavePersistent.

        :param filename: filename
        :param prefix:   save only keys starting with this prefix

        :returns: error string, or nullptr if successful
        """
    def savePersistent(self, filename: str) -> str: 
        """
        Save persistent values to a file.  The server automatically does this,
        but this function provides a way to save persistent values in the same
        format to a file on either a client or a server.

        :param filename: filename

        :returns: error string, or nullptr if successful
        """
    def setNetworkIdentity(self, name: str) -> None: 
        """
        Set the network identity of this node.

        This is the name used during the initial connection handshake, and is
        visible through ConnectionInfo on the remote node.

        :param name: identity to advertise
        """
    @typing.overload
    def setServer(self, server_name: str, port: int = 1735) -> None: 
        """
        Sets server address and port for client (without restarting client).

        :param server_name: server name (UTF-8 string, null terminated)
        :param port:        port to communicate over

        Sets server addresses and ports for client (without restarting client).
        The client will attempt to connect to each server in round robin fashion.

        :param servers: array of server name and port pairs

        Sets server addresses and port for client (without restarting client).
        The client will attempt to connect to each server in round robin fashion.

        :param servers: array of server names
        :param port:    port to communicate over
        """
    @typing.overload
    def setServer(self, servers: typing.List[str], port: int = 1735) -> None: ...
    @typing.overload
    def setServer(self, servers: typing.List[typing.Tuple[str, int]]) -> None: ...
    def setServerTeam(self, team: int, port: int = 1735) -> None: 
        """
        Sets server addresses and port for client (without restarting client).
        Connects using commonly known robot addresses for the specified team.

        :param team: team number
        :param port: port to communicate over
        """
    def setUpdateRate(self, interval: float) -> None: 
        """
        Set the periodic update rate.
        Sets how frequently updates are sent to other nodes over the network.

        :param interval: update interval in seconds (range 0.01 to 1.0)
        """
    @typing.overload
    def startClient(self) -> None: 
        """
        Starts a client.  Use SetServer to set the server name and port.

        Starts a client using the specified server and port

        :param server_name: server name (UTF-8 string, null terminated)
        :param port:        port to communicate over

        Starts a client using the specified (server, port) combinations.  The
        client will attempt to connect to each server in round robin fashion.

        :param servers: array of server name and port pairs

        Starts a client using the specified servers and port.  The
        client will attempt to connect to each server in round robin fashion.

        :param servers: array of server names
        :param port:    port to communicate over
        """
    @typing.overload
    def startClient(self, server_name: str, port: int = 1735) -> None: ...
    @typing.overload
    def startClient(self, servers: typing.List[str], port: int = 1735) -> None: ...
    @typing.overload
    def startClient(self, servers: typing.List[typing.Tuple[str, int]]) -> None: ...
    def startClientTeam(self, team: int, port: int = 1735) -> None: 
        """
        Starts a client using commonly known robot addresses for the specified
        team.

        :param team: team number
        :param port: port to communicate over
        """
    def startConnectionDataLog(self, log: wpiutil._wpiutil.log.DataLog, name: str) -> int: 
        """
        Starts logging connection changes to a DataLog.

        :param log:  data log object; lifetime must extend until
                     StopConnectionDataLog is called or the instance is destroyed
        :param name: data log entry name

        :returns: Data logger handle
        """
    def startDSClient(self, port: int = 1735) -> None: 
        """
        Starts requesting server address from Driver Station.
        This connects to the Driver Station running on localhost to obtain the
        server IP address.

        :param port: server port to use in combination with IP from DS
        """
    def startEntryDataLog(self, log: wpiutil._wpiutil.log.DataLog, prefix: str, logPrefix: str) -> int: 
        """
        Starts logging entry changes to a DataLog.

        :param log:       data log object; lifetime must extend until StopEntryDataLog is
                          called or the instance is destroyed
        :param prefix:    only store entries with names that start with this prefix;
                          the prefix is not included in the data log entry name
        :param logPrefix: prefix to add to data log entry names

        :returns: Data logger handle
        """
    def startLocal(self) -> None: 
        """
        Starts local-only operation.  Prevents calls to StartServer or StartClient
        from taking effect.  Has no effect if StartServer or StartClient
        has already been called.
        """
    def startServer(self, persistFilename: str = 'networktables.ini', listenAddress: str = '', port: int = 1735) -> None: 
        """
        Starts a server using the specified filename, listening address, and port.

        :param persist_filename: the name of the persist file to use (UTF-8 string,
                                 null terminated)
        :param listen_address:   the address to listen on, or null to listen on any
                                 address (UTF-8 string, null terminated)
        :param port:             port to communicate over
        """
    def stopClient(self) -> None: 
        """
        Stops the client if it is running.
        """
    @staticmethod
    def stopConnectionDataLog(logger: int) -> None: 
        """
        Stops logging connection changes to a DataLog.

        :param logger: data logger handle
        """
    def stopDSClient(self) -> None: 
        """
        Stops requesting server address from Driver Station.
        """
    @staticmethod
    def stopEntryDataLog(logger: int) -> None: 
        """
        Stops logging entry changes to a DataLog.

        :param logger: data logger handle
        """
    def stopLocal(self) -> None: 
        """
        Stops local-only operation.  StartServer or StartClient can be called after
        this call to start a server or client.
        """
    def stopServer(self) -> None: 
        """
        Stops the server if it is running.
        """
    def waitForConnectionListenerQueue(self, timeout: float) -> bool: 
        """
        Wait for the connection listener queue to be empty.  This is primarily
        useful for deterministic testing.  This blocks until either the connection
        listener queue is empty (e.g. there are no more events that need to be
        passed along to callbacks or poll queues) or the timeout expires.

        :param timeout: timeout, in seconds.  Set to 0 for non-blocking behavior,
                        or a negative value to block indefinitely

        :returns: False if timed out, otherwise true.
        """
    def waitForEntryListenerQueue(self, timeout: float) -> bool: 
        """
        Wait for the entry listener queue to be empty.  This is primarily useful
        for deterministic testing.  This blocks until either the entry listener
        queue is empty (e.g. there are no more events that need to be passed along
        to callbacks or poll queues) or the timeout expires.

        :param timeout: timeout, in seconds.  Set to 0 for non-blocking behavior,
                        or a negative value to block indefinitely

        :returns: False if timed out, otherwise true.
        """
    def waitForLoggerQueue(self, timeout: float) -> bool: 
        """
        Wait for the incoming log event queue to be empty.  This is primarily
        useful for deterministic testing.  This blocks until either the log event
        queue is empty (e.g. there are no more events that need to be passed along
        to callbacks or poll queues) or the timeout expires.

        :param timeout: timeout, in seconds.  Set to 0 for non-blocking behavior,
                        or a negative value to block indefinitely

        :returns: False if timed out, otherwise true.
        """
    def waitForRpcCallQueue(self, timeout: float) -> bool: 
        """
        Wait for the incoming RPC call queue to be empty.  This is primarily useful
        for deterministic testing.  This blocks until either the RPC call
        queue is empty (e.g. there are no more events that need to be passed along
        to callbacks or poll queues) or the timeout expires.

        :param timeout: timeout, in seconds.  Set to 0 for non-blocking behavior,
                        or a negative value to block indefinitely

        :returns: False if timed out, otherwise true.
        """
    NotifyFlags = _pyntcore._ntcore.NotifyFlags
    __hash__ = None
    kDefaultPort = 1735
    pass
class Value():
    """
    A network table entry value.
    @ingroup ntcore_cpp_api
    """
    def __eq__(self, arg0: Value) -> bool: ...
    def __init__(self) -> None: ...
    def getBoolean(self) -> bool: 
        """
        Get the entry's boolean value.

        :returns: The boolean value.
        """
    def getBooleanArray(self) -> object: 
        """
        Get the entry's boolean array value.

        :returns: The boolean array value.
        """
    def getDouble(self) -> float: 
        """
        Get the entry's double value.

        :returns: The double value.
        """
    def getDoubleArray(self) -> typing.List[float]: 
        """
        Get the entry's double array value.

        :returns: The double array value.
        """
    @staticmethod
    def getFactoryByType(arg0: NetworkTableType) -> cpp_function: ...
    def getRaw(self) -> str: 
        """
        Get the entry's raw value.

        :returns: The raw value.
        """
    def getRpc(self) -> str: 
        """
        Get the entry's rpc definition value.

        :returns: The rpc definition value.
        """
    def getString(self) -> str: 
        """
        Get the entry's string value.

        :returns: The string value.
        """
    def getStringArray(self) -> typing.List[str]: 
        """
        Get the entry's string array value.

        :returns: The string array value.
        """
    def isBoolean(self) -> bool: 
        """
        Determine if entry value contains a boolean.

        :returns: True if the entry value is of boolean type.
        """
    def isBooleanArray(self) -> bool: 
        """
        Determine if entry value contains a boolean array.

        :returns: True if the entry value is of boolean array type.
        """
    def isDouble(self) -> bool: 
        """
        Determine if entry value contains a double.

        :returns: True if the entry value is of double type.
        """
    def isDoubleArray(self) -> bool: 
        """
        Determine if entry value contains a double array.

        :returns: True if the entry value is of double array type.
        """
    def isRaw(self) -> bool: 
        """
        Determine if entry value contains a raw.

        :returns: True if the entry value is of raw type.
        """
    def isRpc(self) -> bool: 
        """
        Determine if entry value contains a rpc definition.

        :returns: True if the entry value is of rpc definition type.
        """
    def isString(self) -> bool: 
        """
        Determine if entry value contains a string.

        :returns: True if the entry value is of string type.
        """
    def isStringArray(self) -> bool: 
        """
        Determine if entry value contains a string array.

        :returns: True if the entry value is of string array type.
        """
    def isValid(self) -> bool: 
        """
        Determine if entry value contains a value or is unassigned.

        :returns: True if the entry value contains a value.
        """
    def last_change(self) -> int: 
        """
        Get the creation time of the value.

        :returns: The time, in the units returned by nt::Now().
        """
    @staticmethod
    def makeBoolean(value: bool, time: int = 0) -> Value: 
        """
        Creates a boolean entry value.

        :param value: the value
        :param time:  if nonzero, the creation time to use (instead of the current
                      time)

        :returns: The entry value
        """
    @staticmethod
    def makeBooleanArray(value: typing.List[bool], time: int = 0) -> Value: 
        """
        Creates a boolean array entry value.

        :param value: the value
        :param time:  if nonzero, the creation time to use (instead of the current
                      time)

        :returns: The entry value
        """
    @staticmethod
    def makeDouble(value: float, time: int = 0) -> Value: 
        """
        Creates a double entry value.

        :param value: the value
        :param time:  if nonzero, the creation time to use (instead of the current
                      time)

        :returns: The entry value
        """
    @staticmethod
    def makeDoubleArray(value: typing.List[float], time: int = 0) -> Value: 
        """
        Creates a double array entry value.

        :param value: the value
        :param time:  if nonzero, the creation time to use (instead of the current
                      time)

        :returns: The entry value
        """
    @staticmethod
    def makeRaw(value: str, time: int = 0) -> Value: 
        """
        Creates a raw entry value.

        :param value: the value
        :param time:  if nonzero, the creation time to use (instead of the current
                      time)

        :returns: The entry value
        """
    @staticmethod
    def makeRpc(value: str, time: int = 0) -> Value: 
        """
        Creates a rpc entry value.

        :param value: the value
        :param time:  if nonzero, the creation time to use (instead of the current
                      time)

        :returns: The entry value
        """
    @staticmethod
    def makeString(value: str, time: int = 0) -> Value: 
        """
        Creates a string entry value.

        :param value: the value
        :param time:  if nonzero, the creation time to use (instead of the current
                      time)

        :returns: The entry value
        """
    @staticmethod
    def makeStringArray(value: typing.List[str], time: int = 0) -> Value: 
        """
        Creates a string array entry value.

        :param value: the value
        :param time:  if nonzero, the creation time to use (instead of the current
                      time)

        :returns: The entry value
                  
                  @note This function moves the values out of the vector.
        """
    @staticmethod
    def makeValue(value: handle) -> Value: ...
    def time(self) -> int: 
        """
        Get the creation time of the value.

        :returns: The time, in the units returned by nt::Now().
        """
    def type(self) -> NetworkTableType: 
        """
        Get the data type.

        :returns: The type.
        """
    def value(self) -> object: 
        """
        Get the data value stored.

        :returns: The type.
        """
    __hash__ = None
    pass
def _addPolledLogger(poller: int, min_level: int, max_level: int) -> int:
    """
    Set the log level for a log poller.  Events will only be generated for
    log messages with level greater than or equal to min_level and less than or
    equal to max_level; messages outside this range will be silently ignored.

    :param poller:    poller handle
    :param min_level: minimum log level
    :param max_level: maximum log level

    :returns: Logger handle
    """
def _cancelPollLogger(poller: int) -> None:
    """
    Cancel a PollLogger call.  This wakes up a call to PollLogger for this
    poller and causes it to immediately return an empty array.

    :param poller: poller handle
    """
def _createLoggerPoller(inst: int) -> int:
    """
    Create a log poller.  A poller provides a single queue of poll events.
    The returned handle must be destroyed with DestroyLoggerPoller().

    :param inst: instance handle

    :returns: poller handle
    """
def _destroyLoggerPoller(poller: int) -> None:
    """
    Destroy a log poller.  This will abort any blocked polling call and prevent
    additional events from being generated for this poller.

    :param poller: poller handle
    """
def _pollLogger(poller: int) -> typing.List[LogMessage]:
    """
    Get the next log event.  This blocks until the next log occurs.

    :param poller: poller handle

    :returns: Information on the log events.  Only returns empty if an error
              occurred (e.g. the instance was invalid or is shutting down).
    """
def _removeLogger(logger: int) -> None:
    """
    Remove a logger.

    :param logger: Logger handle to remove
    """
def startConnectionDataLog(inst: int, log: wpiutil._wpiutil.log.DataLog, name: str) -> int:
    """
    Starts logging connection changes to a DataLog.

    :param inst: instance handle
    :param log:  data log object; lifetime must extend until StopConnectionDataLog
                 is called or the instance is destroyed
    :param name: data log entry name

    :returns: Data logger handle
    """
def startEntryDataLog(inst: int, log: wpiutil._wpiutil.log.DataLog, prefix: str, logPrefix: str) -> int:
    """
    Starts logging entry changes to a DataLog.

    :param inst:      instance handle
    :param log:       data log object; lifetime must extend until StopEntryDataLog is
                      called or the instance is destroyed
    :param prefix:    only store entries with names that start with this prefix;
                      the prefix is not included in the data log entry name
    :param logPrefix: prefix to add to data log entry names

    :returns: Data logger handle
    """
def stopConnectionDataLog(logger: int) -> None:
    """
    Stops logging connection changes to a DataLog.

    :param logger: data logger handle
    """
def stopEntryDataLog(logger: int) -> None:
    """
    Stops logging entry changes to a DataLog.

    :param logger: data logger handle
    """
