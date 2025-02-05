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
time.sleep_ms(2000)
for idx in range (len(thresholds)):
    blobs,img = camera.get_blobs_bottom()
    blob_idx = camera.find_blob(blobs,idx)
    print("looking for blob "+str(idx))

#    if blob_idx is None:
#        print("no blob detected")
#        if idx ==5:
#            servo.set_differential_drive(0.1,0)
#            time.sleep_ms(800)

#        while blob_idx is None:
#            servo.set_differential_drive(0.1,-1)
#            time.sleep_ms(200)
#            servo.set_differential_drive(0,0)
#            blobs,img = camera.get_blobs_bottom()
#            blob_idx = camera.find_blob(blobs,idx)
#    print("blob detected")

    while blob_idx is None:
        servo.set_differential_drive(0.1,-1)
        time.sleep_ms(200)
        servo.set_differential_drive(0,0)
        blobs,img = camera.get_blobs_bottom()
        blob_idx = camera.find_blob(blobs,idx)

    servo.set_differential_drive(0,0)

    frames_no_blobs = 0

    while (frames_no_blobs<6):
        blobs,img = camera.get_blobs_bottom()
        blob_idx = camera.find_blob(blobs,idx)

        if blob_idx is None:
            frames_no_blobs+=1
        else:
            frames_no_blobs= 0
            blob_bias = round((camera.w_centre-blobs[blob_idx].cx())/camera.w_centre,1)
            servo.set_differential_drive(0.15,blob_bias)
            time.sleep_ms(150)
            servo.set_differential_drive(0,0)
    servo.set_differential_drive(0.2,0)
    time.sleep_ms(400)


    servo.set_differential_drive(0,0)










