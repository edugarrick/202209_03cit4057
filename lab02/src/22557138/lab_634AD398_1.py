def answer(maxNumber):
    # START: You code here
    for i in range(maxNumber):
        for j in range(i):
            print("* ", end="")
        print()
    for i in range(maxNumber, 0, -1):
        for j in range(i):
            print("* ", end="")
        print()
    # for i in range(maxNumber):
    #     for j in range(i):
    #         print("* ",end="")
    #     print()
    # for i in range(maxNumber):
    #     for j in range(maxNumber-i):
    #         print("* ",end="")
    #     print()
    # END: You code here

# Please don't change the code below!!!
def main():
    value = int(input("Please enter the maximum value: "))
    answer(value)

if __name__ == "__main__":
    main()
# Please don't change the code above!!!
