def answer( ):
    mean = 0
    # START: You code here
    sum = 0
    count = -1
    value = 1
    while value != 0:
        value = int(input("Enter a number: "))
        sum += value
        count += 1
    if count > 0:
        mean = sum / count
    # sum = 0
    # count = 0
    # while 1:
    #     value = int(input("Enter a number: "))
    #     if value != 0:
    #         sum += value
    #         count += 1
    #     else:
    #         break
    # if count != 0:
    #     mean = sum / count
    # END: You code here
    return mean

# Please don't change the code below!!!
def main():
    print( "The mean is {}".format( answer() ) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!