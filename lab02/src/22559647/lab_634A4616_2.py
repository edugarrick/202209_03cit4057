def answer(num1, num2):
    ret = ""
    # START: You code here  
    if (num1 == 10) and (num2 == 10 ):
        print ("both strings equal")
    elif (num1 == 10 and num2 == 15) or (num1 == 15 and num2 == 10):
        print ("One is 10 and other is 15")
    else :
        print ("The numbers are not 10 not 15")
    # END: You code here
    return ret
10
# Please don't change the code below!!!
def main():
    firstNum = float(input("Enter a number: ")) 
    secondNum = float(input("Enter another number: ")) 
    print( answer(firstNum,secondNum) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!