from multiprocessing.sharedctypes import Value


def answer(maxNumber):
    # START: You code here
    for i in range (0, maxNumber):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
    for i in range (maxNumber,0,-1):
        for j in range(0, i-1):
            print("*",end=" ")
        print("\r")
    
    # END: You code here

# Please don't change the code below!!!
def main():
    value = int(input("Please enter the maximum value: "))
    answer(value)

if __name__ == "__main__":
    main()
# Please don't change the code above!!!