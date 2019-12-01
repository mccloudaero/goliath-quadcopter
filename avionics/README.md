
# Avionics
### Overview
This file is intended as a guide for setting up the avionics for Goliath. Goliath uses the [Pixhawk2](https://docs.px4.io/en/flight_controller/pixhawk-2.html) flight controller running the [PX4](https://px4.io) flight stack.
=======
This file is intended as a guide for setting up the flight controller(avionics) for Goliath. Goliath uses the [Pixhawk](http://www.px4.io) flight controller. The Pixhawk hardware is open source and is capable of running different flight stacks. For Goliath, the PX4 flight stack was chosen.

[Quadrotor X Layout](https://dev.px4.io/en/airframes/airframe_reference.html#quadrotor-x)

## Basic Setup
### Install QGroundControl on your computer
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
Goliath requires special drivers for PX4, and therefore a custom Firmware update. Following the instructions found in /goliath_px4_firmware_patch/README.md

### Customize Configuration
While, the Pixhawk firmware does not require modification, the controller does need custom configuration for Goliath.

Copy /etc in the avionics directory to the SD card.

* /etc/config.txt 
  Sets up the custom configuration for Goliath, specifies which mixers to use 

* /etc/extras.txt 
  Starts the driver for the EVPR master node 

* /etc/mixers
  Custom mixers for goliath

Details on how to make custom mixer files can be found at http://dev.px4.io/concept-mixing.html

#### AUX Servos
The configuration of the Aux output pins is controlled by the fmu app (https://pixhawk.org/firmware/apps/fmu). The mode needed for Goliath's configuration is:
mode_pwm_gpio
This mode enables SRV1-SRV4 and GPIO_EXT1 and GPIO_EXT2

System start-up commands can be changed using the following guide.
http://dev.px4.io/advanced-system-startup.html

More informatition on customization of the PX4 flight stack can be found at:<br>
[Pixhawk: System Startup](http://dev.px4.io/advanced-system-startup.html)<br>
[Pixhawk: Adding A New Airframe](http://dev.px4.io/airframes-adding-a-new-frame.html)

#### Debugging 
Dev Guide on how to connect to the system console:
http://dev.px4.io/advanced-system-console.html

### Theory of Operation
After ensuring that the area is clear, the first step is to set the master switch to ON. At this point the flight controller will power up and start in safe mode (Main LED will be breathing). While in safe mode, all of the servos and relays are disabled from being activated by the firmware. Once it's confirmed that the firmware is operating nominally, the operator can take the system out of safe mode. At this point all of the controls can be checked out prior to starting the engine. If all of the controls are working nominally, the engine can then be started. The engine ignition relay is enabled, allowing the engine to run. Next, the starter is used to start the engine.

### Arming and Disarming
#### From the Control Stick
##### Arming
1. Ensure the Main LED is breathing.
2. Press and hold the safety switch for 3 seconds. The light on the safety switch will start blinking differently.
3. Place the throttle stick in the bottom right corner and hold for 5 seconds. The main LED will become solid.
##### Disarming
To disarm, place the throttle stick in the bottom left corner.

#### Ground Station
Alternatively arming and disarming can also be performed in QGroundControl.


