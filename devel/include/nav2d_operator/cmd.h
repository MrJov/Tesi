// Generated by gencpp from file nav2d_operator/cmd.msg
// DO NOT EDIT!


#ifndef NAV2D_OPERATOR_MESSAGE_CMD_H
#define NAV2D_OPERATOR_MESSAGE_CMD_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace nav2d_operator
{
template <class ContainerAllocator>
struct cmd_
{
  typedef cmd_<ContainerAllocator> Type;

  cmd_()
    : Velocity(0.0)
    , Turn(0.0)
    , Mode(0)  {
    }
  cmd_(const ContainerAllocator& _alloc)
    : Velocity(0.0)
    , Turn(0.0)
    , Mode(0)  {
  (void)_alloc;
    }



   typedef double _Velocity_type;
  _Velocity_type Velocity;

   typedef double _Turn_type;
  _Turn_type Turn;

   typedef int8_t _Mode_type;
  _Mode_type Mode;




  typedef boost::shared_ptr< ::nav2d_operator::cmd_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::nav2d_operator::cmd_<ContainerAllocator> const> ConstPtr;

}; // struct cmd_

typedef ::nav2d_operator::cmd_<std::allocator<void> > cmd;

typedef boost::shared_ptr< ::nav2d_operator::cmd > cmdPtr;
typedef boost::shared_ptr< ::nav2d_operator::cmd const> cmdConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::nav2d_operator::cmd_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::nav2d_operator::cmd_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace nav2d_operator

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'nav2d_operator': ['/home/jov/tesi_ws/src/navigation_2d/nav2d_operator/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::nav2d_operator::cmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::nav2d_operator::cmd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::nav2d_operator::cmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::nav2d_operator::cmd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::nav2d_operator::cmd_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::nav2d_operator::cmd_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::nav2d_operator::cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "90c9a043660646e2102f124332ecb8b7";
  }

  static const char* value(const ::nav2d_operator::cmd_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x90c9a043660646e2ULL;
  static const uint64_t static_value2 = 0x102f124332ecb8b7ULL;
};

template<class ContainerAllocator>
struct DataType< ::nav2d_operator::cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "nav2d_operator/cmd";
  }

  static const char* value(const ::nav2d_operator::cmd_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::nav2d_operator::cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 Velocity\n\
float64 Turn\n\
int8    Mode\n\
";
  }

  static const char* value(const ::nav2d_operator::cmd_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::nav2d_operator::cmd_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Velocity);
      stream.next(m.Turn);
      stream.next(m.Mode);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct cmd_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::nav2d_operator::cmd_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::nav2d_operator::cmd_<ContainerAllocator>& v)
  {
    s << indent << "Velocity: ";
    Printer<double>::stream(s, indent + "  ", v.Velocity);
    s << indent << "Turn: ";
    Printer<double>::stream(s, indent + "  ", v.Turn);
    s << indent << "Mode: ";
    Printer<int8_t>::stream(s, indent + "  ", v.Mode);
  }
};

} // namespace message_operations
} // namespace ros

#endif // NAV2D_OPERATOR_MESSAGE_CMD_H
