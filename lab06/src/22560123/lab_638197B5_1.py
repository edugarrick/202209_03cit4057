
def get_list():
    return list

def number_in_list1( number, list ):
    return ret

def number_in_list2( number, list ):
    ret = False
    return ret

def number_in_list3( number, list ):
    ret = False
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
