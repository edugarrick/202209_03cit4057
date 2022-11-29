def get_mlist():
    mlist= [[9,3,2],8,[6,0,1,11],9,[5,2,1]]
    return mlist

def answer(numlist):
    sum=0
    for value in numlist:
        if isinstance(value, list):
            for subvalue in value:
                sum=sum+subvalue
            else:
                sum=sum+subvalue
    return sum

def main():
    numberlist = get_mlist()
    print("The sum of number in the multi dimension list")
    print(numberlist)
    print("is: {}".format(answer(numberlist)))

if __name__ == "__main__":
    main()
