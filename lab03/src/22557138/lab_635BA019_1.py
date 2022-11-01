def answer(max_number):
    fibonacci = []
    # START: You code here  
    num = 0
    step = 1
    temp = 0
    while num <= max_number:
        fibonacci.append(num)
        temp = num
        num += step
        step = temp
    # END: You code here
    return fibonacci

# Please don't change the code below!!!
def main():
    num_input = int(input("Please enter a number: "))
    print("Fibonacci Sequence is:")
    print( answer(num_input) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!