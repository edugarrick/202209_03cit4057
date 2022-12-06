APPLE_PRICE = 3
ORANGE_PRICE = 6

def get_total(num_apple, num_orange):
    total = num_apple * APPLE_PRICE + num_orange * ORANGE_PRICE
    return total

def callupdate_bykeyword():
    ret = get_total(num_apple = 10, num_orange= 6 )
    return ret

def callupdate_bykeyword2():
    ret = get_total(num_orange= 6, num_apple = 10 )
    return ret

def callupdate_byposition():
    ret = get_total(10,6)
    return ret

def callupdate_byposition2():
    ret = get_total(6,10)
    return ret

# Please don't change the code below!!!
def main():
    print("Total: {}".format(callupdate_bykeyword()))
    print("Total: {}".format(callupdate_bykeyword2()))
    print("Total: {}".format(callupdate_byposition()))
    print("Total: {}".format(callupdate_byposition2()))

if __name__ == "__main__":
    main()
# Please don't change the code above!!!