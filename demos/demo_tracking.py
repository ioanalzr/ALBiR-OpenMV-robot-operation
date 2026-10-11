from robot import *
from machine import LED

led = LED("LED_BLUE")
led.on()

thresholds = [
              (25, 31, -26, -10, 1, 33),   # Broader Red

]

robot = Robot(thresholds)

# robot.stage1(0.3, 0.5)
threshold_idx = 0
robot.scan_for_blob(threshold_idx = threshold_idx,step = 2,limit = 90)
blobs, _ =robot.cam.get_blobs(angle = robot.servo.pan_pos)
blob = robot.cam.get_biggest_blob(blobs)
# while blob is not None:
#     robot.track_blob(blob)
#     blobs, _ =robot.cam.get_blobs(angle = robot.servo.pan_pos)
#     blob = robot.cam.get_biggest_blob(blobs)

if blob is not None:
    robot.track_blob(blob)
time.sleep_ms(100)
if robot.servo.pan_pos >0:
    dir = 1
else:
    dir = -1
robot.servo.set_speed(0.1*dir,-0.1*dir)

while blob is not None and (abs(robot.servo.pan_pos) > 5):
    blobs, _ =robot.cam.get_blobs(angle = robot.servo.pan_pos)
    blob = robot.cam.get_biggest_blob(blobs)

    if blob is not None:
        robot.track_blob(blob)
            # time.sleep_ms(50)
    else:
        robot.drive(0,0) # Stop spinning
        break
robot.drive(0,0)
