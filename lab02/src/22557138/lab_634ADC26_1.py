from re import T


def answer( numInput ) :
    is_prime = True
    # START: You code here
    if numInput < 2:
        is_prime = False
    else:
        # i = 2
        for i in range(2,int(numInput**0.5)+1):
            if (numInput % i) == 0:
                is_prime = False
                break
            # else:
            #     is_prime = True
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
