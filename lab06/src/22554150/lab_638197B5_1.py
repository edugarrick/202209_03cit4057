
def get_list():
    list= [2,10,7,3,10,1,5,9,1000,230]
    return list

def number_in_list1( number, list ):
    ret = False
    for value in list :
        if ( number==value ):
            ret=True
    return ret

def number_in_list2( number, list ):
    ret = False
    if ( number in list) :
        ret=True
    return ret

def number_in_list3( number, list ):
    ret = False
    test = list.count(number)
    if ( test>0 ) :
        ret=True
    return ret

def main():
    value = 6
    numberlist = get_list()
    print("number_in_list1(): {} exists in the list {}".format(value, 
        number_in_list1(value, numberlist)))
    print("number_in_list2(): {} exists in the list {}".format(value, 
        number_in_list2(value, numberlist)))
    print("number_in_list3(): {} exists in the list {}".format(value, 
        number_in_list3(value, numberlist)))


if __name__ == "__main__":
    main()
