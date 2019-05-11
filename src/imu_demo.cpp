#include "ros/ros.h"
#include "sensor_msgs/Imu.h"

#include <sstream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "imu_demo");

  ros::NodeHandle n;

  ros::Publisher pub = n.advertise<sensor_msgs::Imu>("imu", 1000);

  ros::Rate loop_rate(1000);

  int i = 1;
  while (ros::ok())
  {
    sensor_msgs::Imu msg;

    msg.header.stamp = ros::Time::now();
    msg.header.frame_id = "imu";

    msg.linear_acceleration.x = 0.0001; //This is just a demo value
    msg.linear_acceleration.y = 0.0001; //This is just a demo value

    //Set them to -1 if the sensor doesn't provide data
    msg.orientation_covariance[0] = -1;
    //msg.angular_velocity_covariance[0] = -1;
    //msg.linear_acceleration_covariance[0] = -1;

    ROS_INFO("%s", "Published some data");

    pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
    ++i;
  }


  return 0;
}
