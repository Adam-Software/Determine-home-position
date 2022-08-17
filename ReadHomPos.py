
class ReadHomPos():

    def ReadServRange(self):
        
        line = []
        with open('/home/pi/adam/positionrange.txt', 'r') as f:
            line = f.read() 
        line = line.split('\n')
        data = []

        for l in line:
            get = l.split(',')
            for i in range(len(get)):
                if get[i]:
                    get[i] = int(get[i])
                else:
                    get.remove('')
            data.append(get)

        HeadRange     = [[data[0][0]], [data[0][1]]]
        ArmRangeRight = [[data[1][0]], [data[1][1]], [data[1][2]], [data[1][3]]]
        ArmRangeLeft  = [[data[2][0]], [data[2][1]], [data[2][2]], [data[2][3]]]
        PressRange    = [[data[3][0]], [data[3][1]]]
        BodyRange     = [[data[4][0]]]
        LegRightRange = [[data[5][0]], [data[5][1]], [data[5][2]]]
        LegLeftRange  = [[data[6][0]], [data[6][1]], [data[6][2]]]
        HandsRange    = [[data[7][0]], [data[7][1]]]

        return HeadRange, ArmRangeRight, ArmRangeLeft, PressRange, BodyRange, LegRightRange, LegLeftRange, HandsRange
