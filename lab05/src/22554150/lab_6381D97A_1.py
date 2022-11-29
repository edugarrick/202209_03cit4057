def get_tuple():
    my_tuple = (1,3,2,7,4,8)
    return my_tuple

def answer(your_tuple):
    new_tuple =your_tuple+ (9,)
    return new_tuple

def main():
    numberlist = get_tuple()
    print("Original tuple:")
    print(numberlist)
    print("New tuple:")
    print(answer(numberlist))

if __name__ == "__main__":
    main()
