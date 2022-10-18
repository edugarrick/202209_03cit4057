def answer(maxNumber):
    # START: You code here
    i = 0
    j = 0
    for i in range(maxNumber):
        for j in range(i+1):
            print("* ",end="")
        print()
    i = 0
    j = 0
    for i in range(maxNumber,1,-1):
        for j in range(i-1):
            print("* ",end="")
        print()
    # END: You code here

# Please don't change the code below!!!
def main():
    value = int(input("Please enter the maximum value: "))
    answer(value)

if __name__ == "__main__":
    main()
# Please don't change the code above!!!
