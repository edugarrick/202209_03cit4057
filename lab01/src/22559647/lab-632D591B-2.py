def getDiscount( day, amount ) :
    amountAfterDiscount = 0
    # START: Write your code here
    if day == "Monday":
     amountAfterDiscount = (amount / 100) * 90
    else:
     if day == "Tuesday":
        amountAfterDiscount = (amount / 100) * 95
     else:
        amountAfterDiscount = (amount / 100) * 99
    # END: Write you code here
    return amountAfterDiscount

def main():
    day = input("Enter the current day: ")
    amount = int(input("Enter the invoice amount: ")) 
    amountAfterDiscount = getDiscount(day, amount)
    print("Final amount is: {}".format(amountAfterDiscount) )

if __name__ == "__main__":
    main()