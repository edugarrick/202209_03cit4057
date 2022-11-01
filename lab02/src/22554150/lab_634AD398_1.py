from sys import maxunicode


def answer(maxNumber):
    # START: You code here
    
    for i in range(maxNumber):
        for j in range(i+1):
            print( "* ",end="")
        print()
    """      
    for k in range(maxNumber -1,0,-1):
        for l in range (k):
            print( "* ",end="")
        print()
    
    """
    for k in range(maxNumber):
        for l in range(maxNumber - k -1):
            print( "* ",end="")
        print()


    # END: You code here

# Please don't change the code below!!!
def main():
    value = int(input("Please enter the maximum value: "))
    answer(value)

if __name__ == "__main__":
    main()
# Please don't change the code above!!!
