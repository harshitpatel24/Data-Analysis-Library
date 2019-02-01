import Array_Operations as arrayOperations

def mean(npArray):
    noOfElements = arrayOperations.countNoOfElements(npArray)

    if noOfElements > 0:
        sumofElements = arrayOperations.sumOfElements(npArray)
        meanValue = sumofElements / noOfElements
        return meanValue
    else:
        return None

def median(npArray):
    arrayOperations.mergeSort(npArray)
    noOfElements = arrayOperations.countNoOfElements(npArray)
    if noOfElements > 0:
        finalMedian = 0
        if noOfElements % 2 == 0:
            firstMedian = npArray[(noOfElements // 2) - 1]
            secondMedian = npArray[(noOfElements // 2)]
            finalMedian = (firstMedian + secondMedian) / 2
        else:
            finalMedian = npArray[(noOfElements - 1) // 2]
        return finalMedian
    else:
        return None

def mode(npArray):
    noOfElements = arrayOperations.countNoOfElements(npArray)
    if noOfElements > 0:
        occurunceDict = {}
        for value in npArray:
            if value in occurunceDict.keys():
                occurunceDict[value] += 1
            else:
                occurunceDict[value] = 1
        maxValue = 0
        modeValue = 0
        for key,value in occurunceDict.items():
            if value > maxValue:
                maxValue = value
                modeValue = key
            else:
                pass
        return modeValue
    else:
        return None

def variance(npArray):
    noOfElements = arrayOperations.countNoOfElements(npArray)
    if noOfElements > 0:
        meanValue = mean(npArray)
        xMinusMeanValuesSquare = []
        for value in npArray:
            xMinusMeanValuesSquare.append((value - meanValue) ** 2)
        sumOfxMinusMeanValuesSquare = 0
        for squareValue in xMinusMeanValuesSquare:
            sumOfxMinusMeanValuesSquare = sumOfxMinusMeanValuesSquare + squareValue
        varianceValue = sumOfxMinusMeanValuesSquare / noOfElements
        return varianceValue
    else:
        return None

def standardDeviation(npArray):
    varianceValue = variance(npArray)
    if varianceValue != None:
        standardDeviationValue = varianceValue ** 0.5
        return standardDeviationValue
    else:
        return None


def skew(npArray):
    noOfElements = arrayOperations.countNoOfElements(npArray)
    if noOfElements > 0:
        meanValue = mean(npArray)
        standardDeviationValue = standardDeviation(npArray)
        sumOfCubeValues = 0
        for value in npArray:
            sumOfCubeValues = sumOfCubeValues + ((value - meanValue) / standardDeviationValue) ** 3
        skewValue = sumOfCubeValues / noOfElements
        return skewValue
    else:
        return None