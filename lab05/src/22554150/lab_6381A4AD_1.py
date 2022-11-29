

def get_list():
    list= [2,10,7,3,10,1,5,9,1000,230]
    return list

def answer(numlist):
    sum = []
    for value in numlist:
        value = value ** 3 
        sum.append(value)
    return sum

def answer2(numlist):
    sum = [ value ** 3 for value in numlist ]
    return sum

def answer3(numlist):
    sum = list(map(lambda x: x ** 3, numlist))
    return sum


def main():
    numberlist = get_list()
    print("The cubes of the number in the list")
    print(numberlist)
    print("is: {}".format(answer(numberlist)))
    print("The cubes of the number in the list")
    print(numberlist)
    print("is: {}".format(answer2(numberlist)))
    print("The cubes of the number in the list")
    print(numberlist)
    print("is: {}".format(answer3(numberlist)))

if __name__ == "__main__":
    main()
