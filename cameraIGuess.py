from picamera import PiCamera
import time

camera = PiCamera()

print("starting video")
camera.resolution = (1920,1080)
camera.start_recording('/home/pi/RHAB/LOG/VID/Flight.h264')
camera.wait_recording(1800.0)
camera.stop_recording()
print("Stopping video")

print("starting pictures")
camera.resolution = (2592,1944)
for filename in camera.capture_continuous('/home/pi/RHAB/LOG/PICS/img{counter:03d}.jpg'):
        print ("took a picture")

        time.sleep(30)
