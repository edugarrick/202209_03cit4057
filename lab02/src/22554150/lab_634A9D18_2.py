def answer( ):
    mean = 0
    # START: You code here
    trynum = 0
    sum = 0
    userinput = 1
    
    while userinput !=0 :
        userinput = int(input("Enter a number: "))
        if userinput != 0 :
            trynum += 1
            sum += userinput
            continue
    if trynum >0 :
        mean = sum / trynum

    # END: You code here
    return mean

# Please don't change the code below!!!
def main(): 
    print( "The mean is {}".format( answer() ) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!