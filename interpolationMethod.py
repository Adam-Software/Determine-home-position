from ReadHomPos import ReadHomPos
from calcPostiotionsArms import CalcPositionsArms

class CalcPosServo():
    def __init__(self):
        self._ReadPosArray = ReadHomPos()
        self._HomePositionArray = self._ReadPosArray.ReadServRange()
        self._PositionArms = CalcPositionsArms(self._HomePositionArray)

    def CalcHead(self, GoalPosHeadPer, GoalPosNeckPer):

        HeadRangeMin = self._HomePositionArray[0][0][0]
        HeadRangeMax = self._HomePositionArray[0][1][0]
        NeckRangeMin = self._HomePositionArray[0][2][0]
        NeckRangeMax = self._HomePositionArray[0][3][0]

        CalcGoalPosHead = ((HeadRangeMax - HeadRangeMin) * GoalPosHeadPer) + HeadRangeMin
        CalcGoalPosNeck = ((NeckRangeMax - NeckRangeMin) * GoalPosNeckPer) + NeckRangeMin

        return CalcGoalPosHead, CalcGoalPosNeck

    def CalcArms(self, ArmShoulderAnglRightPer, ArmForearmAnglRightPer, ArmElbowTopAnglRightPer, ArmElbowBottAnglRightPer, ArmElbowAnglRightPer, 
       ArmShoulderAnglLeftPer, ArmForearmAnglLeftPer, ArmElbowTopAnglLeftPer, ArmElbowBottAnglLeftPer, ArmElbowAnglLeftPer, SwitchBothElbow):

        if SwitchBothElbow == False:
            ArmRight = self._PositionArms.CalcArmsRight(ArmShoulderAnglRightPer, ArmForearmAnglRightPer, ArmElbowTopAnglRightPer, ArmElbowBottAnglRightPer)
            ArmLeft = self._PositionArms.CalcArmsLeft(ArmShoulderAnglLeftPer, ArmForearmAnglLeftPer, ArmElbowTopAnglLeftPer, ArmElbowBottAnglLeftPer)
        else:
            ArmRight = self._PositionArms.CalcArmsRightElbow(ArmShoulderAnglLeftPer, ArmForearmAnglLeftPer,ArmElbowAnglLeftPer)
            ArmLeft = self._PositionArms.CalcArmsLeftElbow(ArmShoulderAnglLeftPer, ArmForearmAnglLeftPer, ArmElbowAnglLeftPer)

        return ('RightArm', ArmRight[0], ArmRight[1], ArmRight[2], ArmRight[3], 'LeftArm', ArmLeft[0], ArmLeft[1], ArmLeft[2], ArmLeft[3])

    def CalcPress(self, PressTopAnglPer, PressBottAnglPer):
        PressTopAnglMin  =  self._HomePositionArray[3][0][0]
        PressTopAnglMax  =  self._HomePositionArray[3][1][0]
        PressBottAnglMin =  self._HomePositionArray[3][2][0]
        PressBottAnglMax =  self._HomePositionArray[3][3][0]

        CalcGoalPosPressTop = ((PressTopAnglMax - PressTopAnglMin) * PressTopAnglPer) + PressTopAnglMin
        CalcGoalPosPressBott = ((PressBottAnglMax - PressBottAnglMin) * PressBottAnglPer) + PressBottAnglMin

        return CalcGoalPosPressTop, CalcGoalPosPressBott

    def CalcBody(self, BodyRotPer):
        BodyRotMin  =  self._HomePositionArray[4][0][0]
        BodyRotMax  =  self._HomePositionArray[4][1][0]

        CalcGoalPosBody = ((BodyRotMax - BodyRotMin) * BodyRotPer) + BodyRotMin

        return CalcGoalPosBody

    def CalcLeg(self, HightBothLegPer, HightLeftLegPer, HightRightLegPer, SwitchBothLeg):
        LegHipAngRightMin = self._HomePositionArray[5][4][0]
        LegHipAngRightMax = self._HomePositionArray[5][5][0]
        LegFootAngRightMin = self._HomePositionArray[5][2][0]
        LegFootAngRightMax = self._HomePositionArray[5][3][0]
        LegKneeAngRightMin = self._HomePositionArray[5][0][0]
        LegKneeAngRightMax = self._HomePositionArray[5][1][0]

        LegHipAngLeftMin = self._HomePositionArray[6][4][0]
        LegHipAngLeftMax = self._HomePositionArray[6][5][0]
        LegFootAngLeftMin = self._HomePositionArray[6][2][0]
        LegFootAngLeftMax = self._HomePositionArray[6][3][0]
        LegKneeAngLeftMin = self._HomePositionArray[6][0][0]
        LegKneeAngLeftMax = self._HomePositionArray[6][1][0]

        if SwitchBothLeg == False:
            CalcGoalPosHipRight = ((LegHipAngRightMax - LegHipAngRightMin) * HightRightLegPer) + LegHipAngRightMin
            CalcGoalPosFootRight = ((LegFootAngRightMax - LegFootAngRightMin) * HightRightLegPer) + LegFootAngRightMin
            CalcGoalPosKneeRight = ((LegKneeAngRightMax - LegKneeAngRightMin) * HightRightLegPer) + LegKneeAngRightMin

            CalcGoalPosHipLeft = ((LegHipAngLeftMax - LegHipAngLeftMin) * HightLeftLegPer) + LegHipAngLeftMin
            CalcGoalPosFootLeft = ((LegFootAngLeftMax - LegFootAngLeftMin) * HightLeftLegPer) + LegFootAngLeftMin
            CalcGoalPosKneeLeft = ((LegKneeAngLeftMax - LegKneeAngLeftMin) * HightLeftLegPer) + LegKneeAngLeftMin
        else:
            CalcGoalPosHipRight = ((LegHipAngRightMax - LegHipAngRightMin) * HightBothLegPer) + LegHipAngRightMin
            CalcGoalPosFootRight = ((LegFootAngRightMax - LegFootAngRightMin) * HightBothLegPer) + LegFootAngRightMin
            CalcGoalPosKneeRight = ((LegKneeAngRightMax - LegKneeAngRightMin) * HightBothLegPer) + LegKneeAngRightMin

            CalcGoalPosHipLeft = ((LegHipAngLeftMax - LegHipAngLeftMin) * HightBothLegPer) + LegHipAngLeftMin
            CalcGoalPosFootLeft = ((LegFootAngLeftMax - LegFootAngLeftMin) * HightBothLegPer) + LegFootAngLeftMin
            CalcGoalPosKneeLeft = ((LegKneeAngLeftMax - LegKneeAngLeftMin) * HightBothLegPer) + LegKneeAngLeftMin

        return 'RightLeg', CalcGoalPosHipRight, CalcGoalPosFootRight, CalcGoalPosKneeRight, 'LeftLeg', CalcGoalPosHipLeft, CalcGoalPosFootLeft, CalcGoalPosKneeLeft

