def answer(maxNumber):
    # START: You code here
    for x in range(maxNumber):
        for o in range(x):
            print("* ", end="")
        print("")
    for x in range(maxNumber,0,-1):
        for o in range(x):
            print("* ", end="")
        print("")
    # END: You code here

# Please don't change the code below!!!
def main():
    value = int(input("Please enter the maximum value: "))
    answer(value)

if __name__ == "__main__":
    main()
# Please don't change the code above!!!
