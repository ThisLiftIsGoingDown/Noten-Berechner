class MarkCalculator:
    def calculateMarkScale(maxPoints):
        mark = 1
        scale = list()
        while mark <= 6:
            points = (mark/(5*maxPoints))-1
            scale.append(points)
            mark += .5
        return scale
            
    def calculateMarkScalePercent(maxPoints, percentage):
        fourPoints = (maxPoints/100)*percentage
        maxPoints = 4/((5*fourPoints)+5)
        return MarkCalculator.calculateMarkScale(maxPoints)
        
    