def answer(num1, num2):
    ret = ""
    # START: You code here  
    
    if (num1 == 10 and num2 == 10):
        ret = ('both strings equals to 10')
    elif (num1 == 10 and num2 == 15) :
        ret = ('one is {0} and other = {1}').format(num1, num2)
    elif (num1 == 15 and num2 == 10) :
        ret = ('one is {0} and other = {1}').format(num2, num1)
    else:
        ret = 'the number is not 10 nor 15'

            
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    firstNum = float(input("Enter a number: ")) 
    secondNum = float(input("Enter another number: ")) 
    print( answer(firstNum,secondNum) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!