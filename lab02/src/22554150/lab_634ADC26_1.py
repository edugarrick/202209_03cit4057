def answer( numInput ) :
    is_prime = True
    temp=int((numInput**0.5)+1)
    # START: You code here
    for x in range( 2,temp):
        if numInput%x == 0 :
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
