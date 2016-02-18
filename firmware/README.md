
# Firmware
### Overview
This file is intended as a guide for setting up the firmware for Goliath. Goliath uses the [Pixhawk](http://www.pixhawk.org) flight controller. The Pixhawk hardware is open source and is capable of running different flight stacks. For Goliath, the PX4 flight stack was chosen.

### Firmware Setup
Before getting started with the firmware, the tool chains need to be setup for compiling the firmware. While the firmware can be compiled on most operating systems, it's really recommended to use Linux, particularly Ubuntu, as it has the most support. The instructions for setting up the tools chains for Linux can be found at:
[Linux Tool Chain Setup](http://dev.px4.io/starting-installing-linux.html)

Once the tool chain has been setup, simply follow the instructions for downloading and compiler the firmware:
[Building the Firmware](http://dev.px4.io/starting-building.html)

