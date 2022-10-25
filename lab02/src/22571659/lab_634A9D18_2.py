def answer( ):
    mean = 0
    count = 0
    y = 0
    # START: You code here   
    x = int(input("Enter a number:")) 
    while ( x != 0 ):
        x = int(input("Enter a number:")) 
        y += x
        count += 1
    if count > 0:
        mean = y / count
    # END: You code here
    return mean

# Please don't change the code below!!!
def main():
    print( "The mean is {}".format( answer() ) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!