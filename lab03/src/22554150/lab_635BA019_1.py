def answer(max_number):
    fibonacci = []
    # START: You code here  
    F1 = 0
    F2 = 1
    while F1 <= max_number :
        # fibonacci += str(F1) + ", "
        fibonacci.append(F1)
        Fth = F1 +F2
        F1 = F2
        F2 = Fth

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