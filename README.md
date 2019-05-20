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

Install pioneer3dx-explorer into your catkin workspace and build the package using CMake.

```console
$ cd ~/catkin_ws/src
$ git clone https://github.com/informatik-mannheim/pioneer3dx_explorer
$ cd ..
$ catkin_make
```

## Cartographing
