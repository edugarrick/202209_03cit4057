def answer(maxNumber):
    # START: You code here
    for x in range (maxNumber):
        for y in range (x):
            print("x",end="")
        print ("")

    for y in range (maxNumber,0,-1):
        for x in range (y):
            print("x",end="")
        print ("")    
    # END: You code here

# Please don't change the code below!!!
def main():
    value = int(input("Please enter the maximum value: "))
    answer(value)

if __name__ == "__main__":
    main()
# Please don't change the code above!!!
