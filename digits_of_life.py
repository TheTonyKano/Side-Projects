#    def fctionCheck(lst):
#        totalLst = convertStrListtoNumList(lst)
#        total = iterateList(totalLst)
#        print(type(total), total)
#        if total >= 10:
#            tLst = sorted(str(total))
#            total2 = fctionCheck(tLst)
#            print(type(total2))
#        elif total < 10 and len(str(total)) < 2:
#            return total
#        else:
#            return None
#     
#    def convertStrListtoNumList(number):
#        for i in range(0, len(number)):
#            number[i] = int(number[i])
#        return number
#            
#    def iterateList(lst):
#        total = 0
#        print(lst)
#        for i in lst:
#            total += i
#        print(total)    
#        return total
#        
#    date = sorted(input("Enter birthday(in YYYYMMDD format): "))
#    result = fctionCheck(date)
#    print(result)

dateStr = input("Enter birthday(in YYYYMMDD format): ")

def addNumbers(string):
    total = 0
    for i in range(0, len(string)):
        total += int(string[i])
    if total >= 10:
        addNumbers(str(total))
    else:
        print(total)
    
addNumbers(dateStr)