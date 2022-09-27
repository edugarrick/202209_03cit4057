from operator import truediv


#otherdays = {"wednesday","thursday","friday" ,'saturday','sunday'}


day = input("Please enter the day of the week: ")
amount = float(input("Please enter the amount here: "))

def main():
    if day.lower() == "monday" :
        AmountAfterDiscount = amount * 0.9
    elif day.lower() == "tuesday" :
        AmountAfterDiscount = amount * 0.95
    else :
        AmountAfterDiscount = amount * 0.99

    print( "$ "+ str(AmountAfterDiscount ))

if __name__ == "__main__":
    main()