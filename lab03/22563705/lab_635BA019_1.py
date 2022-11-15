from operator import truediv


def answer(max_number):
    fibonacci = []
    # START: You code here
    a=0
    b=1
    c=0
    while(a<max_number):
        if a>max_number:
            break
        fibonacci.append(a)
        if b>max_number:
            break
        fibonacci.append(b)
        c=a+b
        if c >max_number:
            break
        fibonacci.append(c)
        a=b
        b=c
        a=a+b
        b=a+b
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