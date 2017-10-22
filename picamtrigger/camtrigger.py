import boto3
import logging
import os
import picamera
import time

import RPi.GPIO as io
from datetime import datetime

logger = logging.getLogger('camtrigger')

class CamTrigger(object):
    def __init__(self,pin,bucket,profile='default'):
        self.bucket = bucket
        self.pin = pin
        io.setmode(io.BCM)
        self.s3 = self._aws_setup(bucket,profile)
        io.setup(self.pin, io.IN)
       
        
    def _aws_setup(self,bucket,profile):
        if bucket:
            session = boto3.session.Session(profile_name=profile)
            s3 = session.client('s3')
        return s3 if bucket else None

        
    def capture(self, fname='image.jpg'):
        try:
            with picamera.PiCamera() as camera:
                camera.resolution = (2592, 1944)
                camera.framerate = 15
                camera.exposure_mode = 'auto'
                camera.awb_mode = 'auto'
                camera.capture(fname)
            logger.info("Image Captured: {}".format(fname))
        except Exception as e:
            logger.warn("Camera Failed to capture: {}".format(e))

    def upload(self, fname):
        try:
            with open(fname, 'rb') as f:
                self.s3.put_object(
                    Bucket=self.bucket,
                    Body=f,
                    Key="motioncam/{}".format(fname)
                )
            logger.info("Image Uploaded {}".format(fname))
        except Exception as e:
            logger.warn("Failed to upload to S3: {}".format(e))

    def delete(self, fname):
        os.remove(fname)
        logger.info("Image deleted {}".format(fname))

    def cud(self,fname):
        self.capture(fname)
        self.upload(fname)
        self.delete(fname)
 
    def _get_now_fname(self):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
        return "{}.jpg".format(timestamp)

    def run(self):
        logger.info('RaspberryPi Camera Trigger Started.')
        logger.info('Running Test Image.')
        fname = self._get_now_fname()
        self.cud(fname)
        while True:
          try:
              if io.input(self.pin):
                  self.cud(fname)
                  time.sleep(5)
          except Exception as e:
              logger.error("Hit a error, going to continue on. Here's the thing: {}".format(e))
          time.sleep(0.5)
  
