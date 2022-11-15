def answer(input_number_str):
    ret = 0
    # BEGIN: You code here
    ret=int(input_number_str)+ 5
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    num_str = input("Please enter a number: ")
    print("{} + 5 = {}".format(num_str, answer(num_str)))

if __name__ == "__main__":
    main()
# Please don't change the code above!!!