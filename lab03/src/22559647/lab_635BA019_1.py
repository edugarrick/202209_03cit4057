def answer(max_number):
    fibonacci = []
    # START: You code here  
    count = 0
    Ncount = 1
    while  count <= max_number:
        fibonacci.append(count)
        MAXcount = count+Ncount
        count = Ncount
        Ncount = MAXcount
        


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