from itertools import count


def answer( ):
    mean = 0
    # START: You code here
    count = 0
    sum=0
    while True :
        num = int(input("Enter a number:"))
        if num !=0 :
            count=count+1
            sum=sum+num
            continue
        else :
            mean=(sum/count)
            break
    # END: You code here
    return mean

# Please don't change the code below!!!
def main():
    print( "The mean is {}".format( answer() ) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!