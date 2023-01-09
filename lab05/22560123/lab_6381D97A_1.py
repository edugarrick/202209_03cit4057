def get_tuple():
    return my_tuple

def answer(your_tuple):
    return new_tuple

def main():
    numberlist = get_tuple()
    print("Original tuple:")
    print(numberlist)
    print("New tuple:")
    print(answer(numberlist))

if __name__ == "__main__":
    main()
