num = str(input("Type in up to 7 numbers:"))
numlist = [int(i) for i in num]
print(numlist)
while True:
    for i in numlist:
        if numlist == 1:
            print('  #')
            print('  #')
            print('  #')
            print('  #')
            print('  #')
        elif numlist == 2:
            print(' ###')
            print('   #')
            print(' ###')
            print(' #  ')
            print(' ###')
        elif numlist == 3:
            print(' ###')
            print('   #')
            print(' ###')
            print('   #')
            print(' ###')
        elif numlist == 4:
            print(' # #')
            print(' # #')
            print(' ###')
            print('   #')
            print('   #')
        elif numlist == 5:
            print(' ###')
            print(' #  ')
            print(' ###')
            print('   #')
            print(' ###')
        elif numlist == 6:
            print(' ###')
            print(' #  ')
            print(' ###')
            print(' # #')
            print(' ###')
        elif numlist == 7:
            print(' ###')
            print('   #')
            print('   #')
            print('   #')
            print('   #')
        elif numlist == 8:
            print(' ###')
            print(' # #')
            print(' ###')
            print(' # #')
            print(' ###')
        elif numlist == 9:
            print(' ###')
            print(' # #')
            print(' ###')
            print('   #')
            print(' ###')
        elif numlist == 0:
            print(' ###')
            print(' # #')
            print(' # #')
            print(' # #')
            print(' ###')
        else:
            continue