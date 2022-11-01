import random
from re import I

def answer( numguessing ):
    # START: You code here 
    h = int(input('Enter a number between 1 to 100:'))
    while (numguessing!=h):
        if h>numguessing:
            print('Too high')
        elif h<numguessing:
            print('Too low')
        else:
             print('You won')
        h = int(input('Enter a number between 1 to 100:'))
    print('You won')



    # END: You code here

# Please don't change the code below!!!
def main():
    # Generate a random number
    random_num = random.randint(1,100) 
    answer(random_num)

if __name__ == "__main__":
    main()
# Please don't change the code above!!!