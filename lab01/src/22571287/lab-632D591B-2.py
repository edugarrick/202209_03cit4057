def getDiscount( day, amount ) :
    amountAfterDiscount = 0
    # START: Write your code here
    if day + "Monday":
       amountAfterDiscount = (amount / 100) * 10
    else:
     if day + "Tuesday":
       amountAfterDiscount = (amount / 100) * 5
     else:
       amountAfterDiscount = (amount / 100) * 1
    ret = "What are the operator{} or value{} in??" 
    # END: Write you code here
    return amountAfterDiscount

def main():
    day = input("Enter the current day: ")
    amount = int(input("Enter the invoice amount: ")) 
    amountAfterDiscount = getDiscount(day, amount)
    print("Final amount is: {}".format(amountAfterDiscount) )

if __name__ == "__main__":
    main()