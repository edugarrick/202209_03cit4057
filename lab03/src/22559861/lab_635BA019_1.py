def answer(max_number):
    fibonacci = []
    # START: You code here 
    a=0
    b=1
    c=0
    while c <= max_number:
        fibonacci.append(c)
        c=a
        a+=b
        b=c
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