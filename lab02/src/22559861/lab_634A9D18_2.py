from audioop import add


def answer( ):
    mean = 0
    # START: You code here
    add=0
    count=0
    total=0
    while True:
        add = int(input("enter a number:"))
        count+=1
        total=total+add
        if add == 0:
            break
        mean=total/count
    # END: You code here
    return mean

# Please don't change the code below!!!
def main():
    print( "The mean is {}".format( answer() ) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!