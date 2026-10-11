from servos import *
from camera import *
from machine import LED

led = LED("LED_BLUE")
led.on()


servo = Servo()
servo.soft_reset()

thresholds = [
              (38, 46, -20, -9, -2, 12),
              (49, 58, -8, 8, -50, -28),
              (86, 89, -9, 3, 31, 46),
               (43, 56, 37, 54, 6, 24),
              (28, 38, 14, 29, -17, 0),
              (62, 68, 23, 36, 23, 45),
              (63, 71, -30, -1, 1, 41),
              ]
camera = Cam(thresholds, 10)

servo.set_differential_drive(0,0)
time.sleep_ms(2000) # wait for camera gain
for idx in range (len(thresholds)):
    blobs,img = camera.get_blobs()
    blob_idx = camera.find_blob(blobs,idx)
    print("looking for blob "+str(idx))

    while blob_idx is None:
        servo.set_speed(0.1,-0.1)
        blobs,img = camera.get_blobs()
        blob_idx = camera.find_blob(blobs,idx)


    servo.set_differential_drive(0,0)

    frames_no_blobs = 0

    while (frames_no_blobs<6):
        blobs,img = camera.get_blobs()
        blob_idx = camera.find_blob(blobs,idx)

        if blob_idx is None:
            frames_no_blobs+=1
        else:
            frames_no_blobs= 0
            blob_bias = -1*round((camera.w_centre-blobs[blob_idx].cx())/camera.w_centre,3)
            servo.set_differential_drive(0.1,blob_bias)
    servo.set_differential_drive(0,0)
    print("found blob "+str(idx))









