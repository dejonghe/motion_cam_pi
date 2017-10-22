# PiCamTrigger
## Overview
This project was initally built to trigger the RaspberryPi Camera from a Adafruit Motion Sensor. There's an option to send images captured to S3. 

## Usage
```
usage: pi-camera-trigger [-h] [-i INPUT_PIN] [-b BUCKET] [-p PROFILE]

RPi Camera Trigger

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_PIN, --input_pin INPUT_PIN
                        The GPIO pin the sensor input is attached to. Default 4
  -b BUCKET, --bucket BUCKET
                        AWS S3 Bucket to upload files to.
  -p PROFILE, --profile PROFILE
                        AWS profile to use.
```

