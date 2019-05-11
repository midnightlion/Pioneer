cmake_minimum_required(VERSION 2.8.3)
project(pioneer3dx_cartographer)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  std_msgs
)

catkin_package()

${catkin_INCLUDE_DIRS}