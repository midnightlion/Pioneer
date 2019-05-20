# pioneer3dx-explorer

## Introduction

This package enables cartographing using the Google Cartographer for the pioneer3dx robot. The package provides ready-to-use launch files and other important configuration files.

## Main concepts

### 

### 

## Installation



### Prerequisites

* Pioneer3dx robot
* SICK LMS200-30106 laser scanner
* IMU Brick 2.0

### Dependencies

The following libraries are required.

* p2os (https://github.com/allenh1/p2os)
* cartographer (https://github.com/googlecartographer/cartographer)
* sicktoolbox_wrapper (https://github.com/ros-drivers/sicktoolbox_wrapper)
* ros-tinkerforge_sensors (https://github.com/gus484/ros-tinkerforge_sensors)

### Package installation

Install pioneer3dx-explorer into your workspace and build the package using catkin.

```console
$ cd ~/catkin_ws/src
$ git clone https://github.com/informatik-mannheim/pioneer3dx_explorer
$ cd ..
$ catkin_make
```

## Cartographing

### Recording your own bag file

Record scan, tf and imu data using a rosbag record. Be sure to start these components at first. You could use the pioneer.launch file for example or start the components by yourself.

```console
$ roslaunch launch/pioneer.launch
$ rosbag record scan tf imu
```

Then validate your recorded file for possible errors or optimisation infos.

```console
$ cartographer_rosbag_validate -bag-filename recorded.bag
```

### Offline cartographing

This runs the offline cartographer using your previously created bag file. This launch file starts the cartographer and rviz for visualisation and then plays your rosbag file.

```console
$ roslaunch launch/offline_cartographer.launch bag_filename:=/home/pioneer/recorded.bag
```

### Online cartographing

This runs the online cartographer. This launch file starts the necessary components like motor, laser scanner and imu, starts the cartographer and rviz for visualisation.

```console
$ roslaunch launch/cartographer.launch
```