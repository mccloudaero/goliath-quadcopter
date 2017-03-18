
# RPM Sensor

## Frequency Measurement
The frequency is measured using a hall effect sensor connected to a [Trinket Pro](https://www.adafruit.com/product/2000).

# Trinket Pro
Pin | Purpose
---|---
BAT+|Power to Trinket Pro
GND|Ground
3|Hall Effect Signal
5V(Header)|Hall Effect Power
GND(Header)|Hall Effect Ground 
A4|SDA for I2C
A5|SCL for I2C

## Pixhawk I2C Port pinout
Pin | Signal | Volt
---|---|---
1(red)|VCC|+5
2(blk)|SCL|+3.3(pullups)
3(blk)|SDA|+3.3(pullups)
4(blk)|GND|GND

## References
[Additional Trinket Pro Info] (https://learn.adafruit.com/introducing-pro-trinket/downloads)
[Trinket Pro Pinout] (https://learn.adafruit.com/introducing-pro-trinket/pinouts)

[Adafruit IDE Setup] (https://learn.adafruit.com/adafruit-arduino-ide-setup/overview)

[Hall Effect Sensor Example] (https://diyhacking.com/arduino-hall-effect-sensor-tutorial/)
