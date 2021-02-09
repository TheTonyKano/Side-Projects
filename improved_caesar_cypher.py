data = str(input("Enter text to be encrypted: "))

def encryptdata(string, shift):
    code = ""
    cypher = ''
    for char in string:
        code = ord(char) + shift 
        if char.isalpha(): 
            if ord(char) <= 90 and ord(char) >= 65:
                if code > 90 and code < 121:
                    phase = 64 + (shift - (90 - (code - shift)))
                    cypher += chr(phase)
                else:
                    cypher += chr(code)
            elif ord(char) <= 122 and ord(char) >= 97:
                if code > 122:
                    phase = 96 + (shift - (122 - (code - shift))) 
                    cypher += chr(phase)
                else:
                    cypher += chr(code)
            else: 
                cypher += chr(code)        
        elif char == chr(32):
            cypher += chr(32)
        elif char.isdigit():
            cypher += char
        else:
            cypher += char
    return cypher        
                
 
def shiftVerification ():
    shift = int(input("Enter value to shift by (1 to 25): "))
    if shift > 0 and shift < 26:
        return shift
    else:
        shiftVerification()
             

print(encryptdata(data, shiftVerification ()))