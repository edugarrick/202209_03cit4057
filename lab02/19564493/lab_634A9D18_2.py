def answer( ):
    mean = 0
    numberinput =1
    tatol =0
    count =0
    # START: You code here
    while (numberinput != 0):
        numberinput = int (input("enter a number:"))
        if(numberinput != 0):
            tatol = tatol + numberinput
            count = count +1
    if count > 0:
        mean = tatol / count
    # END: You code here
    return mean

# Please don't change the code below!!!
def main():
    print( "The mean is {}".format( answer() ) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!