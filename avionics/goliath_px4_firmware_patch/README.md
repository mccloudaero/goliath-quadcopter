# PX4 Firmware patch
Adds drivers for:
* EVPR Master Node
* GPIO Relays

# Firmware Setup
## Checkout Firmware from
https://github.com/PX4/Firmware.git

## Apply Patch
git apply <path to patch>

## Compile
make px4fmu-v3_default

## Flash
make px4fmu-v3_default upload
