def answer( ):
    mean = 0
    # START: You code here
    sum = 0
    count = 0
    value = 1
    while value != 0:
        value = int(input("Enter a number: "))
        sum = sum + value
        count += 1
    mean = sum / (count - 1)
    # END: You code here
    return mean

# Please don't change the code below!!!
def main():
    print( "The mean is {}".format( answer() ) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!