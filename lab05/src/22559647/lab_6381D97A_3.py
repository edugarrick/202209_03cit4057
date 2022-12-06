def get_set():
    my_set= {7,1,5,23,8,1}
    return my_set

def answer(your_set):
    total = 0
    for number in your_set :
        total += number
    return total

def answer2(your_set):
    total = sum(your_set)
    return total

def main():
    numset = get_set()
    print("Set:")
    print(numset)
    print("The sum of the values = {}".format(answer(numset)))
    print("The sum of the values = {}".format(answer2(numset)))

if __name__ == "__main__":
    main()
