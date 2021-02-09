def readint(prompt, min, max):
    test = True
    while test:
        try:
            number = int(input(prompt))
            if number in list(range(min, max + 1)):
                return number
            else:
                raise LookupError
        except ValueError:
            print('Error: wrong input')
        except LookupError:
            print('Error: the value is not within permitted range (', min,'..',max,')', sep='')
            print('Please try again...')
            
v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)