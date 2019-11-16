cmake_minimum_required(VERSION 2.8.3)
project(pioneer3dx_explorer)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  std_msgs
  pcl_conversions
  pcl_ros
  openni_launch
  openni2_launch
)

catkin_package(
  INCLUDE_DIRS
  CATKIN_DEPENDS roscpp
		 pcl_conversions
		 pcl_ros
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
