# pioneer3dx cartographer

## Introduction

This package enables cartographing using the Google Cartographer for the pioneer3dx robot. The package provides ready-to-use launch files and other important configuration files.

## Main concepts

TODO

## Installation

### Prerequisites

* Pioneer3dx robot
* SICK LMS200-30106 laser scanner

### Dependencies

The following libraries are required.

* p2os (https://github.com/allenh1/p2os)
* cartographer (https://github.com/googlecartographer/cartographer)
* sicktoolbox_wrapper (https://github.com/ros-drivers/sicktoolbox_wrapper)

### Package installation

Install pioneer3dx_cartographer into your catkin workspace and build the package using CMake.

```console
$ cd ~/catkin_ws/src
$ git clone https://github.com/informatik-mannheim/Pioneer
$ cd ..
$ catkin_make
```

## Cartographing

TODO

## Future plans

* Adding an IMU to the package (https://www.conrad.de/de/p/tinkerforge-imu-brick-2-0-1411060.html)
