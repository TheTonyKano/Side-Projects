#listYears = [year for year in range(400, 2801) if year % 4 == 0] figure out list comprehen



def calculationLY():
    listYears = []
    for i in range(400, 2401, 400):
        listYears.append(i)
        for j in range(0,93,4):
            listYears.append(i + (4 + j)) 
    return listYears


def isYearLeap(year):
    if year in calculationLY():
        return True
    else:
        return False

# for year in range(400, 2801, 100): if year % 4 == 0

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->",end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")