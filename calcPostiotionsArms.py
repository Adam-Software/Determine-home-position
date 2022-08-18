class CalcPositionsArms():
  def __init__(self, ArmRangeArray):
    self._ArmShoulderRightMin = ArmRangeArray[1][0][0]
    self._ArmShoulderRightMax = ArmRangeArray[1][1][0]
    self._ArmForearmRightMin  = ArmRangeArray[1][2][0]
    self._ArmForearmRightMax  = ArmRangeArray[1][3][0]
    self._ArmElbowTopRightMin = ArmRangeArray[1][4][0]
    self._ArmElbowTopRightMax = ArmRangeArray[1][5][0]
    self._ArmElbowBottRightMin = ArmRangeArray[1][6][0]
    self._ArmElbowBottRightMax = ArmRangeArray[1][7][0]
    self._ArmShoulderLeftMax = ArmRangeArray[2][0][0] #electronic range exclusion
    self._ArmShoulderLeftMin = ArmRangeArray[2][1][0] #electronic range exclusion
    self._ArmForearmLeftMin  = ArmRangeArray[2][2][0]
    self._ArmForearmLeftMax  = ArmRangeArray[2][3][0]
    self._ArmElbowTopLeftMin = ArmRangeArray[2][4][0]
    self._ArmElbowTopLeftMax = ArmRangeArray[2][5][0]
    self._ArmElbowBottLeftMin = ArmRangeArray[2][6][0]
    self._ArmElbowBottLeftMax = ArmRangeArray[2][7][0]

  def CalcArmsRight(self, ArmShoulderAnglePer, ArmForearmAnglePer, ArmElbowTopAnglePer, ArmElbowBottomAnglePer):
    CalcGolPosShoulder = self._CalcArmsAngle(self._ArmShoulderRightMax, self._ArmShoulderRightMin, ArmShoulderAnglePer)
    CalcGolPosForearm = self._CalcArmsAngle(self._ArmForearmRightMax, self._ArmForearmRightMin, ArmForearmAnglePer)
    CalcGolPosElbowTop =  self._CalcArmsAngle(self._ArmElbowTopRightMax, self._ArmForearmRightMin, ArmElbowTopAnglePer)
    CalcGolPosElbowBott = self._CalcArmsAngle(self._ArmElbowBottRightMax, self._ArmElbowBottRightMin, ArmElbowBottomAnglePer)

    return (CalcGolPosShoulder, CalcGolPosForearm, CalcGolPosElbowTop, CalcGolPosElbowBott)

  def CalcArmsLeft(self, ArmShoulderAnglePer, ArmForearmAnglePer, ArmElbowTopAnglePer, ArmElbowBottomAnglePer):
    CalcGolPosShoulder = ((self._ArmShoulderLeftMax - self._ArmShoulderLeftMin) * ArmShoulderAnglePer) + self._ArmShoulderLeftMin
    CalcGolPosForearm = ((self._ArmForearmLeftMax - self._ArmForearmLeftMin) * ArmForearmAnglePer) + self._ArmForearmLeftMin
    CalcGolPosElbowTop = ((self._ArmElbowTopLeftMax - self._ArmElbowTopLeftMin) * ArmElbowTopAnglePer) + self._ArmElbowTopLeftMin
    CalcGolPosElbowBott = ((self._ArmElbowBottLeftMax - self._ArmElbowBottLeftMin) * ArmElbowBottomAnglePer) + self._ArmElbowBottLeftMin

    return (CalcGolPosShoulder, CalcGolPosForearm, CalcGolPosElbowTop, CalcGolPosElbowBott)

  #elbow
  def CalcArmsRightElbow(self, ArmShoulderAnglePer, ArmForearmAnglePer, ArmElbowAnglePer):
    CalcGolPosShoulder = self._CalcArmsAngle(self._ArmShoulderRightMax, self._ArmShoulderRightMin, ArmShoulderAnglePer)
    CalcGolPosForearm = self._CalcArmsAngle(self._ArmForearmRightMax, self._ArmForearmRightMin, ArmForearmAnglePer)
    CalcGolPosElbowTop =  self._CalcArmsAngle(self._ArmElbowTopRightMax, self._ArmElbowTopRightMin, ArmElbowAnglePer)
    CalcGolPosElbowBott = self._CalcArmsAngle(self._ArmElbowBottRightMax, self._ArmElbowBottRightMin, ArmElbowAnglePer)

    return (CalcGolPosShoulder, CalcGolPosForearm, CalcGolPosElbowTop, CalcGolPosElbowBott)

  #elbow
  def CalcArmsLeftElbow(self, ArmShoulderAnglePer, ArmForearmAnglePer, ArmElbowAnglePer):
    CalcGolPosShoulder = self._CalcArmsAngle(self._ArmShoulderLeftMax, self._ArmShoulderLeftMin, ArmShoulderAnglePer)
    CalcGolPosForearm = self._CalcArmsAngle(self._ArmForearmLeftMax, self._ArmForearmLeftMin, ArmForearmAnglePer)
    CalcGolPosElbowTop =  self._CalcArmsAngle(self._ArmElbowTopLeftMax, self._ArmElbowTopLeftMin, ArmElbowAnglePer)
    CalcGolPosElbowBott = self._CalcArmsAngle(self._ArmElbowBottLeftMax, self._ArmElbowBottLeftMin, ArmElbowAnglePer)

    return (CalcGolPosShoulder, CalcGolPosForearm, CalcGolPosElbowTop, CalcGolPosElbowBott)

  def _CalcArmsAngle(self, angleMax, angleMin, anglePer):
    position = ((angleMax - angleMin) * anglePer) + angleMin
    return position
