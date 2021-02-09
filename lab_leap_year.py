def isYearLeap(year, calcLY):
    if year in calcLY:
        return True
    else:
        return False

testData = [1900, 2000, 2016, 1987, 923, 2100]
listYears = [i + (4 + j) for i in range(396, 2401, 400) for j in range(0,97,4)]
for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->" ,end=" ")
    result = isYearLeap(yr, listYears)
    if result == True:
        print("OK")
    else:
        print("Failed")