def XOR_function(X,Y):

    if (X =='0' and Y == '1') or (X == '1' and Y =='0'):
        ans ='1'
    else:
        ans ='0'

    return ans

def AND_function(X,Y):
    '''returns or value'''
    
    if X =='1' and Y == '1' :
        ans= '1'
    else :
        ans = '0'

    return ans

def OR_function(X,Y):

    if X =='1' or Y =='1':
        ans = '1'
    else:
        ans ='0'

    return ans


def addition(X,Y):
    A=''
    B=''
    Cin='0'
    result =''

    for i in range (7,-1,-1):
        A = X[i]
        B = Y[i]

        carry_1 = AND_function(A,B)
        answer = XOR_function(A,B)
        carry_2 = AND_function(answer,Cin)
        fanswer = XOR_function(answer,Cin)
        fcarry =OR_function(carry_1,carry_2)

# calling and_function,or_function and xor_function from function module.  
        Cin= fcarry
        result = fanswer + result

    if fcarry == '1' :
         result = fcarry + result

    return result







