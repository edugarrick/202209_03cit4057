def answer( ):
    mean = 0
    numberInput = 1
    total = 0
    count = 0
    # START: You code here
    while ( numberInput!=0):
        numberInput = int(input("Enter a number"))
        if (numberInput !=0):
            total = total + numberInput
            count = count + 1
    if count > 0:
        mean = total / count
    # END: You code here
    return mean

# Please don't change the code below!!!
def main():
    print( "The mean is {}".format( answer() ) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!