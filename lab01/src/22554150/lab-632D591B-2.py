from operator import truediv

#day = input("Please enter the day of the week: ")
#amount = float(input("Please enter the amount here: "))
#
#def main():
#    if day.lower() == "monday" :
#        AmountAfterDiscount = amount * 0.9
#    elif day.lower() == "tuesday" :
#        AmountAfterDiscount = amount * 0.95
#    else :
#        AmountAfterDiscount = amount * 0.99
#
#    print( "$ "+ str(AmountAfterDiscount ))
#
#if __name__ == "__main__":
#    main()

def getDiscount( day, amount ) :
    amountAfterDiscount = 0
    # START: Write your code here
    if day.lower() == "monday" :
       amountAfterDiscount = (amount / 100) * 90
    elif day.lower() == "tuesday" :
       amountAfterDiscount = (amount / 100) * 95
    else :
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