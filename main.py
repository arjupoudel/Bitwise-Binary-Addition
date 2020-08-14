import sys
import InputNumbers
import Conversion
import BinaryAddition

def run():
    x = InputNumbers.input_numbers1()
    y = InputNumbers.input_numbers2()
    
    print ("\nFirst decimal number: " +str (x))
    print ("Second decimal number: " +str (y))
    
    binary_num1 = (Conversion.bitToByte(''.join(map(str,Conversion.dectobin(x)[::-1]))))
    print("\nFirst decimal number in binary:  " + str(binary_num1))
    
    binary_num2 = (Conversion.bitToByte(''.join(map(str,Conversion.dectobin(y)[::-1]))))
    print("Second decimal number in binary: " + str(binary_num2))

    final_sum = str(BinaryAddition.addition(binary_num1,binary_num2))

    print("\nThe bitwise addition of above binary numbers is:" + final_sum)
    
    while True:
        restart = input("\nDo you want to start again? (Y/N): ")
        print(end='')
        if restart == "Y":
            run()
        elif restart == "N":
            sys.exit()
run()
