from ast import Num


def answer( numInput ) :
    is_prime = True
    # START: You code here
    for i in range(1, numInput):
        if numInput%i ==0:
            is_prime = True
            continue
    else:
        if numInput%i !=0:
            is_prime = False
            
    

    # END: You code here
    return is_prime

# Please don't change the code below!!!
def main():
    value = int(input("Please enter the number: "))
    if ( answer(value) ):
        print("{} is a prime number.".format(value))
    else:
        print("{} is NOT a prime number.".format(value))

if __name__ == "__main__":
    main()
# Please don't change the code above!!!
