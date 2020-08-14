#defining a function to change decimal to binary number
def dectobin(num):
    answer=[]
    while num > 0:
        if num % 2 == 0:
            num = int(num//2)
            remainder = 0
            answer.append(remainder)
            
        elif num % 2 == 1:
            num = int(num//2)
            remainder = 1
            answer.append(remainder)
    return answer


#defining function to convert bits to a byte
def bitToByte(z):
    while len(str(z)) < 8:
        z = '0' + str(z)
        if len(str(z)) == 8:
            pass
    return z


    





















