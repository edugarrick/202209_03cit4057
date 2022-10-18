def answer(nm1, nm2 ):
    net = ""
    # START: You code here
    if ( nm1 == 10 and nm2 == 10):
        net = "both string equal 10"
    elif ( nm1 == 10 and nm2 == 15 ) or ( num1 == 15 and num2 == 10):
        net = "One is 10 and other is 15"
    else:
        net = "the unmber are 10 nor 15"
    # END: You code here
    return net

# Please don't change the code below!!!
def main():
    firstNum = float(input("Enter a number:"))
    secondNum = float(input("Enter another number:")) 
    print( answer(firstNum,secondNum)) 

if __name__ == "__main__":
    main()
# Please don't change the code above!!!