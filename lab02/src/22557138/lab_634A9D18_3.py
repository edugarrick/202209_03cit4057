def answer(startNumber, endNumber ):
    ret = []
    # START: You code here
    # if startNumber % 2 == 0:
    #     ret = range(startNumber,endNumber + 1,2)
    # else:
    #     ret = range(startNumber + 1, endNumber + 1,2)
    ret = range(startNumber + startNumber % 2, endNumber + 1, 2)
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    num1 = int(input("Please enter the starting integer: "))
    num2 = int(input("Please enter the ending integer:"))
    evenNumbers = answer( num1, num2 )
    print("The even numbers between {} and {} (inclusive) are:\n".format(num1, num2))
    for i in evenNumbers:
        print("{} ".format(i))

if __name__ == "__main__":
    main()
# Please don't change the code above!!!