def answer(max_number):
    fibonacci = []

    a=0
    b=1
    # START: You code here
    while a <= max_number :
        fibonacci.append(a)
        c = a + b
        a = b
        b = c
      
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