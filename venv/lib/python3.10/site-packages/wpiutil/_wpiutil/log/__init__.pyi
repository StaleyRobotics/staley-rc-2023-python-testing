from __future__ import annotations
import wpiutil._wpiutil.log
import typing

__all__ = [
    "BooleanArrayLogEntry",
    "BooleanLogEntry",
    "DataLog",
    "DataLogEntry",
    "DataLogReader",
    "DataLogRecord",
    "DoubleArrayLogEntry",
    "DoubleLogEntry",
    "FloatArrayLogEntry",
    "FloatLogEntry",
    "IntegerArrayLogEntry",
    "IntegerLogEntry",
    "MetadataRecordData",
    "RawLogEntry",
    "StartRecordData",
    "StringArrayLogEntry",
    "StringLogEntry"
]


class DataLogEntry():
    """
    Log entry base class.
    """
    def finish(self, timestamp: int = 0) -> None: 
        """
        Finishes the entry.

        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    def setMetadata(self, metadata: str, timestamp: int = 0) -> None: 
        """
        Updates the metadata for the entry.

        :param metadata:  New metadata for the entry
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    pass
class BooleanLogEntry(DataLogEntry):
    """
    Log boolean values.
    """
    @typing.overload
    def __init__(self, log: DataLog, name: str, metadata: str, timestamp: int = 0) -> None: ...
    @typing.overload
    def __init__(self, log: DataLog, name: str, timestamp: int = 0) -> None: ...
    def append(self, value: bool, timestamp: int = 0) -> None: 
        """
        Appends a record to the log.

        :param value:     Value to record
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    kDataType = 'boolean'
    pass
class DataLog():
    """
    A data log. The log file is created immediately upon construction with a
    temporary filename.  The file may be renamed at any time using the
    SetFilename() function.

    The lifetime of the data log object must be longer than any data log entry
    objects that refer to it.

    The data log is periodically flushed to disk.  It can also be explicitly
    flushed to disk by using the Flush() function.
    """
    @typing.overload
    def __init__(self, dir: str = '', filename: str = '', period: float = 0.25, extraHeader: str = '') -> None: 
        """
        Construct a new Data Log.  The log will be initially created with a
        temporary filename.

        :param dir:         directory to store the log
        :param filename:    filename to use; if none provided, a random filename is
                            generated of the form "wpilog_{}.wpilog"
        :param period:      time between automatic flushes to disk, in seconds;
                            this is a time/storage tradeoff
        :param extraHeader: extra header data

        Construct a new Data Log that passes its output to the provided function
        rather than a file.  The write function will be called on a separate
        background thread and may block.  The write function is called with an
        empty data array when the thread is terminating.

        :param write:       write function
        :param period:      time between automatic calls to write, in seconds;
                            this is a time/storage tradeoff
        :param extraHeader: extra header data
        """
    @typing.overload
    def __init__(self, write: typing.Callable[[buffer], None], period: float = 0.25, extraHeader: str = '') -> None: ...
    def appendBoolean(self, entry: int, value: bool, timestamp: int) -> None: ...
    def appendBooleanArray(self, entry: int, arr: typing.List[bool], timestamp: int) -> None: ...
    def appendDouble(self, entry: int, value: float, timestamp: int) -> None: ...
    def appendDoubleArray(self, entry: int, arr: typing.List[float], timestamp: int) -> None: ...
    def appendFloat(self, entry: int, value: float, timestamp: int) -> None: ...
    def appendFloatArray(self, entry: int, arr: typing.List[float], timestamp: int) -> None: ...
    def appendInteger(self, entry: int, value: int, timestamp: int) -> None: ...
    def appendIntegerArray(self, entry: int, arr: typing.List[int], timestamp: int) -> None: ...
    def appendRaw(self, entry: int, data: buffer, timestamp: int) -> None: 
        """
        Appends a record to the log.

        :param entry:     Entry index, as returned by Start()
        :param data:      Data to record
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    def appendRaw2(self, entry: int, data: typing.List[buffer], timestamp: int) -> None: 
        """
        Appends a record to the log.

        :param entry:     Entry index, as returned by Start()
        :param data:      Data to record
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    def appendString(self, entry: int, value: str, timestamp: int) -> None: ...
    def appendStringArray(self, entry: int, arr: typing.List[str], timestamp: int) -> None: ...
    def finish(self, entry: int, timestamp: int = 0) -> None: 
        """
        Finish an entry.

        :param entry:     Entry index
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    def flush(self) -> None: 
        """
        Explicitly flushes the log data to disk.
        """
    def pause(self) -> None: 
        """
        Pauses appending of data records to the log.  While paused, no data records
        are saved (e.g. AppendX is a no-op).  Has no effect on entry starts /
        finishes / metadata changes.
        """
    def resume(self) -> None: 
        """
        Resumes appending of data records to the log.
        """
    def setFilename(self, filename: str) -> None: 
        """
        Change log filename.

        :param filename: filename
        """
    def setMetadata(self, entry: int, metadata: str, timestamp: int = 0) -> None: 
        """
        Updates the metadata for an entry.

        :param entry:     Entry index
        :param metadata:  New metadata for the entry
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    def start(self, name: str, type: str, metadata: str = '', timestamp: int = 0) -> int: 
        """
        Start an entry.  Duplicate names are allowed (with the same type), and
        result in the same index being returned (Start/Finish are reference
        counted).  A duplicate name with a different type will result in an error
        message being printed to the console and 0 being returned (which will be
        ignored by the Append functions).

        :param name:      Name
        :param type:      Data type
        :param metadata:  Initial metadata (e.g. data properties)
        :param timestamp: Time stamp (may be 0 to indicate now)

        :returns: Entry index
        """
    pass
class BooleanArrayLogEntry(DataLogEntry):
    """
    Log array of boolean values.
    """
    @typing.overload
    def __init__(self, log: DataLog, name: str, metadata: str, timestamp: int = 0) -> None: ...
    @typing.overload
    def __init__(self, log: DataLog, name: str, timestamp: int = 0) -> None: ...
    def append(self, arr: typing.List[bool], timestamp: int = 0) -> None: 
        """
        Appends a record to the log.  For find functions to work, timestamp
        must be monotonically increasing.

        :param arr:       Values to record
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    kDataType = 'boolean[]'
    pass
class DataLogReader():
    """
    Data log reader (reads logs written by the DataLog class).
    """
    @typing.overload
    def __init__(self, buffer: buffer, name: str = '') -> None: ...
    @typing.overload
    def __init__(self, filename: str) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def getBufferIdentifier(self) -> str: 
        """
        Gets the buffer identifier, typically the filename.

        :returns: Identifier string
        """
    def getExtraHeader(self) -> str: 
        """
        Gets the extra header data.

        :returns: Extra header data
        """
    def getVersion(self) -> int: 
        """
        Gets the data log version. Returns 0 if data log is invalid.

        :returns: Version number; most significant byte is major, least significant
                  is minor (so version 1.0 will be 0x0100)
        """
    def isValid(self) -> bool: 
        """
        Returns true if the data log is valid (e.g. has a valid header).
        """
    pass
class DataLogRecord():
    """
    A record in the data log. May represent either a control record (entry == 0)
    or a data record. Used only for reading (e.g. with DataLogReader).
    """
    def getBoolean(self) -> bool: 
        """
        Decodes a data record as a boolean. Note if the data type (as indicated in
        the corresponding start control record for this entry) is not "boolean",
        invalid results may be returned or TypeError will be raised.
        """
    def getBooleanArray(self) -> list: 
        """
        Decodes a data record as a boolean array. Note if the data type (as
        indicated in the corresponding start control record for this entry) is not
        "boolean[]", invalid results may be returned or a TypeError may be raised.
        """
    def getDouble(self) -> float: 
        """
        Decodes a data record as a double. Note if the data type (as indicated in
        the corresponding start control record for this entry) is not "double",
        invalid results may be returned or TypeError will be raised.
        """
    def getDoubleArray(self) -> typing.List[float]: 
        """
        Decodes a data record as a double array. Note if the data type (as
        indicated in the corresponding start control record for this entry) is not
        "double[]", invalid results may be returned or a TypeError may be raised.
        """
    def getEntry(self) -> int: 
        """
        Gets the entry ID.

        :returns: entry ID
        """
    def getFinishEntry(self) -> int: 
        """
        Decodes a finish control record. Raises TypeError on error.
        """
    def getFloat(self) -> float: 
        """
        Decodes a data record as a float. Note if the data type (as indicated in
        the corresponding start control record for this entry) is not "float",
        invalid results may be returned or TypeError will be raised.
        """
    def getFloatArray(self) -> typing.List[float]: 
        """
        Decodes a data record as a float array. Note if the data type (as
        indicated in the corresponding start control record for this entry) is not
        "float[]", invalid results may be returned or a TypeError may be raised.
        """
    def getInteger(self) -> int: 
        """
        Decodes a data record as an integer. Note if the data type (as indicated in
        the corresponding start control record for this entry) is not "int64",
        invalid results may be returned or TypeError will be raised.
        """
    def getIntegerArray(self) -> typing.List[int]: 
        """
        Decodes a data record as an integer array. Note if the data type (as
        indicated in the corresponding start control record for this entry) is not
        "int64[]", invalid results may be returned or a TypeError may be raised.
        """
    def getRaw(self) -> bytes: 
        """
        Gets the raw data. Use the GetX functions to decode based on the data type
        in the entry's start record.
        """
    def getSetMetadataData(self) -> MetadataRecordData: 
        """
        Decodes a set metadata control record. Raises TypeError on error.
        """
    def getSize(self) -> int: 
        """
        Gets the size of the raw data.

        :returns: size
        """
    def getStartData(self) -> StartRecordData: 
        """
        Decodes a start control record. Raises TypeError on error.
        """
    def getString(self) -> str: 
        """
        Decodes a data record as a string. Note if the data type (as indicated in
        the corresponding start control record for this entry) is not "string",
        invalid results may be returned or TypeError will be raised.
        """
    def getStringArray(self) -> typing.List[str]: 
        """
        Decodes a data record as a string array. Note if the data type (as
        indicated in the corresponding start control record for this entry) is not
        "string[]", invalid results may be returned or a TypeError may be raised.
        """
    def getTimestamp(self) -> int: 
        """
        Gets the record timestamp.

        :returns: Timestamp, in integer microseconds
        """
    def isControl(self) -> bool: 
        """
        Returns true if the record is a control record.

        :returns: True if control record, false if normal data record.
        """
    def isFinish(self) -> bool: 
        """
        Returns true if the record is a finish control record. Use GetFinishEntry()
        to decode the contents.

        :returns: True if finish control record, false otherwise.
        """
    def isSetMetadata(self) -> bool: 
        """
        Returns true if the record is a set metadata control record. Use
        GetSetMetadataData() to decode the contents.

        :returns: True if set metadata control record, false otherwise.
        """
    def isStart(self) -> bool: 
        """
        Returns true if the record is a start control record. Use GetStartData()
        to decode the contents.

        :returns: True if start control record, false otherwise.
        """
    pass
class DoubleArrayLogEntry(DataLogEntry):
    """
    Log array of double values.
    """
    @typing.overload
    def __init__(self, log: DataLog, name: str, metadata: str, timestamp: int = 0) -> None: ...
    @typing.overload
    def __init__(self, log: DataLog, name: str, timestamp: int = 0) -> None: ...
    def append(self, arr: typing.List[float], timestamp: int = 0) -> None: 
        """
        Appends a record to the log.

        :param arr:       Values to record
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    kDataType = 'double[]'
    pass
class DoubleLogEntry(DataLogEntry):
    """
    Log double values.
    """
    @typing.overload
    def __init__(self, log: DataLog, name: str, metadata: str, timestamp: int = 0) -> None: ...
    @typing.overload
    def __init__(self, log: DataLog, name: str, timestamp: int = 0) -> None: ...
    def append(self, value: float, timestamp: int = 0) -> None: 
        """
        Appends a record to the log.

        :param value:     Value to record
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    kDataType = 'double'
    pass
class FloatArrayLogEntry(DataLogEntry):
    """
    Log array of float values.
    """
    @typing.overload
    def __init__(self, log: DataLog, name: str, metadata: str, timestamp: int = 0) -> None: ...
    @typing.overload
    def __init__(self, log: DataLog, name: str, timestamp: int = 0) -> None: ...
    def append(self, arr: typing.List[float], timestamp: int = 0) -> None: 
        """
        Appends a record to the log.

        :param arr:       Values to record
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    kDataType = 'float[]'
    pass
class FloatLogEntry(DataLogEntry):
    """
    Log float values.
    """
    @typing.overload
    def __init__(self, log: DataLog, name: str, metadata: str, timestamp: int = 0) -> None: ...
    @typing.overload
    def __init__(self, log: DataLog, name: str, timestamp: int = 0) -> None: ...
    def append(self, value: float, timestamp: int = 0) -> None: 
        """
        Appends a record to the log.

        :param value:     Value to record
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    kDataType = 'float'
    pass
class IntegerArrayLogEntry(DataLogEntry):
    """
    Log array of integer values.
    """
    @typing.overload
    def __init__(self, log: DataLog, name: str, metadata: str, timestamp: int = 0) -> None: ...
    @typing.overload
    def __init__(self, log: DataLog, name: str, timestamp: int = 0) -> None: ...
    def append(self, arr: typing.List[int], timestamp: int = 0) -> None: 
        """
        Appends a record to the log.

        :param arr:       Values to record
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    kDataType = 'int64[]'
    pass
class IntegerLogEntry(DataLogEntry):
    """
    Log integer values.
    """
    @typing.overload
    def __init__(self, log: DataLog, name: str, metadata: str, timestamp: int = 0) -> None: ...
    @typing.overload
    def __init__(self, log: DataLog, name: str, timestamp: int = 0) -> None: ...
    def append(self, value: int, timestamp: int = 0) -> None: 
        """
        Appends a record to the log.

        :param value:     Value to record
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    kDataType = 'int64'
    pass
class MetadataRecordData():
    """
    Data contained in a set metadata control record as created by
    DataLog::SetMetadata(). This can be read by calling
    DataLogRecord::GetSetMetadataData().
    """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def entry(self) -> int:
        """
        Entry ID.

        :type: int
        """
    @property
    def metadata(self) -> str:
        """
        New metadata for the entry.

        :type: str
        """
    pass
class RawLogEntry(DataLogEntry):
    """
    Log arbitrary byte data.
    """
    @typing.overload
    def __init__(self, log: DataLog, name: str, metadata: str, timestamp: int = 0) -> None: ...
    @typing.overload
    def __init__(self, log: DataLog, name: str, metadata: str, type: str, timestamp: int = 0) -> None: ...
    @typing.overload
    def __init__(self, log: DataLog, name: str, timestamp: int = 0) -> None: ...
    def append(self, data: buffer, timestamp: int = 0) -> None: 
        """
        Appends a record to the log.

        :param data:      Data to record
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    kDataType = 'raw'
    pass
class StartRecordData():
    """
    Data contained in a start control record as created by DataLog::Start() when
    writing the log. This can be read by calling DataLogRecord::GetStartData().
    """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def entry(self) -> int:
        """
        Entry ID; this will be used for this entry in future records.

        :type: int
        """
    @property
    def metadata(self) -> str:
        """
        Initial metadata.

        :type: str
        """
    @property
    def name(self) -> str:
        """
        Entry name.

        :type: str
        """
    @property
    def type(self) -> str:
        """
        Type of the stored data for this entry, as a string, e.g. "double".

        :type: str
        """
    pass
class StringArrayLogEntry(DataLogEntry):
    """
    Log array of string values.
    """
    @typing.overload
    def __init__(self, log: DataLog, name: str, metadata: str, timestamp: int = 0) -> None: ...
    @typing.overload
    def __init__(self, log: DataLog, name: str, timestamp: int = 0) -> None: ...
    def append(self, arr: typing.List[str], timestamp: int = 0) -> None: 
        """
        Appends a record to the log.

        :param arr:       Values to record
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    kDataType = 'string[]'
    pass
class StringLogEntry(DataLogEntry):
    """
    Log string values.
    """
    @typing.overload
    def __init__(self, log: DataLog, name: str, metadata: str, timestamp: int = 0) -> None: ...
    @typing.overload
    def __init__(self, log: DataLog, name: str, metadata: str, type: str, timestamp: int = 0) -> None: ...
    @typing.overload
    def __init__(self, log: DataLog, name: str, timestamp: int = 0) -> None: ...
    def append(self, value: str, timestamp: int = 0) -> None: 
        """
        Appends a record to the log.

        :param value:     Value to record
        :param timestamp: Time stamp (may be 0 to indicate now)
        """
    kDataType = 'string'
    pass
