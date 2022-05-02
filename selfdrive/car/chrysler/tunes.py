#!/usr/bin/env python3
from enum import Enum

class LatTunes(Enum):
  INDI = 0
  TORQUE = 1
  PID_A = 2
  PID_B = 3

  ###### LAT ######
def set_lat_tune(tune, name, MAX_LAT_ACCEL=3.5, FRICTION=.001):
    if name == LatTunes.TORQUE:
      tune.init('torque')
      tune.torque.useSteeringAngle = True
      tune.torque.kp = 2.0 / MAX_LAT_ACCEL
      tune.torque.kf = 1.0 / MAX_LAT_ACCEL
      tune.torque.ki = 0.5 / MAX_LAT_ACCEL
      tune.torque.friction = FRICTION
    elif name == LatTunes.INDI:
      tune.init('indi')
      tune.indi.innerLoopGainBP = [0.]
      tune.indi.innerLoopGainV = [4.0]
      tune.indi.outerLoopGainBP = [0.]
      tune.indi.outerLoopGainV = [3.0]
      tune.indi.timeConstantBP = [0.]
      tune.indi.timeConstantV = [1.0]
      tune.indi.actuatorEffectivenessBP = [0.]
      tune.indi.actuatorEffectivenessV = [1.0]
    elif 'PID' in str(name):
      tune.init('pid')
      tune.pid.kiBP = [0.0]
      tune.pid.kpBP = [0.0]
      if name == LatTunes.PID_A:
        tune.pid.kpV = [0.2]
        tune.pid.kiV = [0.05]
        tune.pid.kf = 0.00003
      elif name == LatTunes.PID_B:
        tune.pid.kpV = [0.6]
        tune.pid.kiV = [0.1]
        tune.pid.kf = 0.00006
      else:
          raise NotImplementedError('This PID tune does not exist')
    else:
        raise NotImplementedError('This lateral tune does not exist')
