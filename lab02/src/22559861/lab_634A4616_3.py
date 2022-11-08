from calendar import SATURDAY, weekday


def answer(weekd, value):
    ret = 0
    if weekd == "Saturday":
        ret = (value/100) *95
    elif weekd == "Sunday":
        ret = (value/100) *90
    else:  
        weekd != "saturday" or "Sunday"
        ret = value

    return ret

# Please don't change the code below!!!
def main():
    weekday = input("Enter the weekday: ") 
    amt = input("Enter an amount: ") 
    amt = float( "{:.2f}".format(float(amt)) )
    print( answer(weekday,amt) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!