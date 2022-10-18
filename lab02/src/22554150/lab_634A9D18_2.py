def answer( ):
    mean = 0
    # START: You code here
    trynum = 0
    sum = 0
    
    while True:
        userinput = int(input("Enter a number: "))
        if userinput != 0 :
            trynum =  trynum + 1
            sum = sum + userinput
            continue
        else :
            mean = sum / trynum
            break

    # END: You code here
    return mean

# Please don't change the code below!!!
def main():
    print( "The mean is {}".format( answer() ) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!