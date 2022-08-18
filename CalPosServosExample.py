from interpolationMethod import CalcPosServo

GoalPosHeadPer = 0.2
GoalPosNeckPer = 0.2

ArmShoulderAnglRightPer = 0
ArmForearmAnglRightPer = 0
ArmElbowTopAnglRightPer = 0
ArmElbowBottAnglRightPer = 0
ArmElbowAnglRightPer = 0

ArmShoulderAnglLeftPer = 0
ArmForearmAnglLeftPer = 0
ArmElbowTopAnglLeftPer = 0
ArmElbowBottAnglLeftPer = 0
ArmElbowAnglLeftPer = 0
SwitchBothlbow = False

PressTopAnglPer = 0
PressBottAnglPer = 0

BodyRotPer = 0.5

HightBothLegPer = 0
HightLeftLegPer = 0
HightRightLegPer = 0
SwitchBothLeg = False


ReadPosArray = CalcPosServo()
   
HeadPos = ReadPosArray.CalcHead(GoalPosHeadPer, GoalPosNeckPer)
print('HeadPos')
print(int(HeadPos[0]))
print(int(HeadPos[1]))
 
ArmsPos = ReadPosArray.CalcArms(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False)
ArmsPosElbow = ReadPosArray.CalcArms(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, True)

print('ArmsPos')
print(ArmsPos)
print('ArmsPosElbow')
print(ArmsPosElbow)

