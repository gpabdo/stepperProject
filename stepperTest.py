from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

import time


kit = MotorKit()
for i in range(200):
  kit.stepper1.onestep()
  time.sleep(0.01)
