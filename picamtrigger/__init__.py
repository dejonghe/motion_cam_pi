import argparse

from picamtrigger.logger import console_logger, logging
from picamtrigger.camtrigger import CamTrigger

__version__ = "0.0.0"



def main():
    parser = argparse.ArgumentParser(description="RPi Camera Trigger")
    parser.add_argument(
        '-i',
        '--input_pin',
        type=int,
        default=4,
        help='The GPIO pin the sensor input is attached to')
    parser.add_argument(
        '-b',
        '--bucket',
        type=str,
        default=None,
        help='AWS S3 Bucket to upload files to.')
    parser.add_argument(
        '-p',
        '--profile',
        type=str,
        default='default',
        help='AWS profile to use.')
    parser.add_argument(
        '-s',
        '--sensitivity',
        type=int,
        default=1,
        help='Sensitivity setting of the camera trigger, this is how many times in a row the pin triggers on a .2 second loop.')
    args = parser.parse_args()
 
    mt = CamTrigger(
        args.input_pin,
        args.bucket,
        args.profile,
        args.sensitivity)

    mt.run()

if __name__ == '__main__':
    main()
