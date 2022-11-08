from ast import Num
import random

def answer( numguessing ):
    # START: You code here  
    while True:
        print("Guess a number between 1 and 100.")
        guess = input()
        i = int(guess)
        if i == numguessing:
            print("You won")
            break
        elif i < numguessing:
            print ("Too low")
        else:
            i > numguessing
            print ("Too high")
    
    # END: You code here

# Please don't change the code below!!!
def main():
    # Generate a random number
    random_num = random.randint(1,100) 
    answer(random_num)

if __name__ == "__main__":
    main()
# Please don't change the code above!!!