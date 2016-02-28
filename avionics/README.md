
# Avionics
### Overview
This file is intended as a guide for setting up the flight controller(avionics) for Goliath. Goliath uses the [Pixhawk](http://www.pixhawk.org) flight controller. The Pixhawk hardware is open source and is capable of running different flight stacks. For Goliath, the PX4 flight stack was chosen.

## Basic Setup
### Install QGroundControl
QGroundControl is a software an open source micro air vehicle ground control station [QGroundControl](http://qgroundcontrol.com). In addition to being able to provide mission control for Goliath, it also provides an easy way to load the latest version of the Firmware.

### Conroller Setup
The Taranis X9D is the controller recommended for the Pixhawk. General information on setting up the Taranis with the Pixhawk can be found on the Pixhawk user guide at:
[Pixhawk Flight Mode Configuration](http://px4.io/docs/flight-mode-configuration/)
Follow the instructions for setting up the controller for Single Channel Flight Mode Configuration in the video.
[Controller Setup](http://https://youtu.be/scqO7vbH2jo)

####Goliath specific configuration
Additional channels are required for Goliath to control the gas engine. Setup the controller with the following channels: 
Channel | Source | Function
---|---|---
CH6 | S2 | choke servo
CH7 | SH | starter relay
CH8 | SD | ignition relay

### Firmware Update
After downloading QGroundControl, launch the software. Follow the instructions for installing the latest version of the Firmware.

### Configuration
QGroundControl will prompt the user for configuration.

## Advanced Firmware
For more advanced users, looking to do software development, you'll want to fork the Firmware and compile it yourself. The following guides the developers on how to get setup

### Firmware Setup
Before getting started with the firmware, the tool chains need to be setup for compiling the firmware. While the firmware can be compiled on most operating systems, it's really recommended to use Linux, particularly Ubuntu, as it has the most support. The instructions for setting up the tools chains for Linux can be found at:
[Linux Tool Chain Setup](http://dev.px4.io/starting-installing-linux.html)

Once the tool chain has been setup, simply follow the instructions for downloading and compiler the firmware:
[Building the Firmware](http://dev.px4.io/starting-building.html)

### Firmware Configuration
The PX4 flight stack is able to be used for different airframes though the use of mixers. The mixer tells the flight stack how to take the input values and translate them to the output values, so that the control software can be universally applied and eliminates the need for custom firmware. The guide for added custom airframes is at:
[Adding a new Airframe Configuration](http://dev.px4.io/airframes-adding-a-new-frame.html)
[Old Guide - Deprecated](https://pixhawk.org/dev/mixing)

The custom mixer file for Goliath will be located in this folder.

### Theory of Operation
After ensuring that the area is clear, the first step is to set the master switch to ON. At this point the Pixhawk controller will power up and start in safe mode. While in safe mode, all of the servos and relays are disabled from being activated by the firmware. Once it's confirmed that the firmware is operating nominally, the operator can take the system out of safe mode. At this point all of the controls can be checked out prior to starting the engine. If all of the controls are working nominally, the engine can then be started. The engine ignition relay is enabled, allowing the engine to run. Next, the starter is used to start the engine.
