def answer(weekd, value):
    weekd =  weekd.lower()
    ret = 0
    if weekd == "saturday":
        ret = (value *0.95)
    elif weekd == "sunday":
            ret = (value *0.90)
    else:
        ret = value

    
    # END: You code here
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