# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from hector_elevation_msgs/ElevationMapMetaData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import genpy

class ElevationMapMetaData(genpy.Message):
  _md5sum = "6c887873faf3a1d55d884bdcc92b9241"
  _type = "hector_elevation_msgs/ElevationMapMetaData"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# This hold basic information about the characterists of the EvaluationGrid

# The time at which the map was loaded
time map_load_time
# Map resolution in xy plane [m/cell]
float64 resolution_xy
# Map resolution in height [m/cell]
float64 resolution_z
# min observed height [m]
float64 min_elevation
# max observed height [m]
float64 max_elevation
# Height zero value. For example 16384.
int16 zero_elevation
# Map width [cells]
uint32 width
# Map height [cells]
uint32 height
# The origin of the map [m, m, rad].  This is the real-world pose of the
# cell (0,0) in the map.
geometry_msgs/Pose origin



================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['map_load_time','resolution_xy','resolution_z','min_elevation','max_elevation','zero_elevation','width','height','origin']
  _slot_types = ['time','float64','float64','float64','float64','int16','uint32','uint32','geometry_msgs/Pose']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       map_load_time,resolution_xy,resolution_z,min_elevation,max_elevation,zero_elevation,width,height,origin

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ElevationMapMetaData, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.map_load_time is None:
        self.map_load_time = genpy.Time()
      if self.resolution_xy is None:
        self.resolution_xy = 0.
      if self.resolution_z is None:
        self.resolution_z = 0.
      if self.min_elevation is None:
        self.min_elevation = 0.
      if self.max_elevation is None:
        self.max_elevation = 0.
      if self.zero_elevation is None:
        self.zero_elevation = 0
      if self.width is None:
        self.width = 0
      if self.height is None:
        self.height = 0
      if self.origin is None:
        self.origin = geometry_msgs.msg.Pose()
    else:
      self.map_load_time = genpy.Time()
      self.resolution_xy = 0.
      self.resolution_z = 0.
      self.min_elevation = 0.
      self.max_elevation = 0.
      self.zero_elevation = 0
      self.width = 0
      self.height = 0
      self.origin = geometry_msgs.msg.Pose()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2I4dh2I7d().pack(_x.map_load_time.secs, _x.map_load_time.nsecs, _x.resolution_xy, _x.resolution_z, _x.min_elevation, _x.max_elevation, _x.zero_elevation, _x.width, _x.height, _x.origin.position.x, _x.origin.position.y, _x.origin.position.z, _x.origin.orientation.x, _x.origin.orientation.y, _x.origin.orientation.z, _x.origin.orientation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.map_load_time is None:
        self.map_load_time = genpy.Time()
      if self.origin is None:
        self.origin = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 106
      (_x.map_load_time.secs, _x.map_load_time.nsecs, _x.resolution_xy, _x.resolution_z, _x.min_elevation, _x.max_elevation, _x.zero_elevation, _x.width, _x.height, _x.origin.position.x, _x.origin.position.y, _x.origin.position.z, _x.origin.orientation.x, _x.origin.orientation.y, _x.origin.orientation.z, _x.origin.orientation.w,) = _get_struct_2I4dh2I7d().unpack(str[start:end])
      self.map_load_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2I4dh2I7d().pack(_x.map_load_time.secs, _x.map_load_time.nsecs, _x.resolution_xy, _x.resolution_z, _x.min_elevation, _x.max_elevation, _x.zero_elevation, _x.width, _x.height, _x.origin.position.x, _x.origin.position.y, _x.origin.position.z, _x.origin.orientation.x, _x.origin.orientation.y, _x.origin.orientation.z, _x.origin.orientation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.map_load_time is None:
        self.map_load_time = genpy.Time()
      if self.origin is None:
        self.origin = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 106
      (_x.map_load_time.secs, _x.map_load_time.nsecs, _x.resolution_xy, _x.resolution_z, _x.min_elevation, _x.max_elevation, _x.zero_elevation, _x.width, _x.height, _x.origin.position.x, _x.origin.position.y, _x.origin.position.z, _x.origin.orientation.x, _x.origin.orientation.y, _x.origin.orientation.z, _x.origin.orientation.w,) = _get_struct_2I4dh2I7d().unpack(str[start:end])
      self.map_load_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I4dh2I7d = None
def _get_struct_2I4dh2I7d():
    global _struct_2I4dh2I7d
    if _struct_2I4dh2I7d is None:
        _struct_2I4dh2I7d = struct.Struct("<2I4dh2I7d")
    return _struct_2I4dh2I7d
