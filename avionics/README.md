
# Avionics
### Overview
This file is intended as a guide for setting up the flight controller(avionics) for Goliath. Goliath uses the [Pixhawk](http://www.px4.io) flight controller. The Pixhawk hardware is open source and is capable of running different flight stacks. For Goliath, the PX4 flight stack was chosen.

[Quadrotor X Layout](https://dev.px4.io/en/airframes/airframe_reference.html#quadrotor-x)

## Basic Setup
### Install QGroundControl
QGroundControl is a software an open source micro air vehicle ground control station [QGroundControl](http://qgroundcontrol.com). In addition to being able to provide mission control for Goliath, it also provides an easy way to load the latest version of the Firmware.

### Controller Setup
The Taranis X9D is the controller recommended for the Pixhawk. General information on setting up the Taranis with the Pixhawk can be found on the Pixhawk user guide at:
[Pixhawk Flight Mode Configuration](http://px4.io/docs/flight-mode-configuration/)
Follow the instructions for setting up the controller for Single Channel Flight Mode Configuration in the video.
[Controller Setup](http://https://youtu.be/scqO7vbH2jo)

####Flight Modes
Switches SE and SF are used together to cycle through the different modes.

Num | Mode | Switch
---|---|---
1|Stabalized/Main|SF back, SE back
2|Acro|SF back, SE mid
3|Altitude Control|SF back, SE front
4|Position Control|SF front, SE front
5|Loiter|SF front, SE mid
6|Return|SF front, SE back

####Goliath specific configuration
Additional channels are required for Goliath to control the gas engine. Setup the controller with the following channels: 

Channel | Source | Function
---|---|---
CH6 | S2 | choke servo
CH7 | SH | starter relay
CH8 | SD | ignition relay

### Firmware Update
After downloading QGroundControl, launch the software. Follow the instructions for installing the latest version of the firmware.

### Customize Configuration
While, the Pixhawk firmware does not require modification, the controller does need custom configuration for Goliath. Customization is done by placing specific files on the flight controller SD card. Details on customization of the Pixhawk can be found at:<br>
[Pixhawk: System Startup](http://dev.px4.io/advanced-system-startup.html)<br>
[Pixhawk: Adding A New Airframe](http://dev.px4.io/airframes-adding-a-new-frame.html)

#### Configuration File
The configuration file on the SD card is at: /etc/config.txt

#### Mixers
Goliath requires a custom mixer file for both main and aux. The mixer files are placed at /etc/mixers/

Details on how to make custom mixer files can be found at http://dev.px4.io/concept-mixing.html

#### AUX Servos
The configuration of the Aux output pins is controlled by the fmu app (https://pixhawk.org/firmware/apps/fmu). The mode needed for Goliath's configuration is:
mode_pwm_gpio
This mode enables SRV1-SRV4 and GPIO_EXT1 and GPIO_EXT2

System start-up commands can be changed using the following guide.
http://dev.px4.io/advanced-system-startup.html


### Theory of Operation
After ensuring that the area is clear, the first step is to set the master switch to ON. At this point the Pixhawk controller will power up and start in safe mode (Main LED will be breathing). While in safe mode, all of the servos and relays are disabled from being activated by the firmware. Once it's confirmed that the firmware is operating nominally, the operator can take the system out of safe mode. At this point all of the controls can be checked out prior to starting the engine. If all of the controls are working nominally, the engine can then be started. The engine ignition relay is enabled, allowing the engine to run. Next, the starter is used to start the engine.

### Arming and Disarming
#### From the Control Stick
##### Arming
1. Ensure the Main LED is breathing.
2. Press and hold the safety swith for 3 seconds. The light on the safety switch will start blinking differently.
3. Place the throttle stick in the bottom right corner and hold for 5 seconds. The main LED will become solid.
##### Disarming
To disarm, place the throttle stick in the bottom left corner.

#### Ground Station
Alternatively arming and disarming can also be performed in QGroundControl.

## System Console
Using an FTDI 3.3V cable, connect it to the serial 4/5 port.

Dev Guide on how to connect to the system console:
http://dev.px4.io/advanced-system-console.html

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


