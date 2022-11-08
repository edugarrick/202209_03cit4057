import random

def answer( numguessing ):
    # START: You code here  
    value = 0
    while value != numguessing:
        value = int(input("Enter a number between 1 to 100: "))
        if 0 < value < 101:
            if value < numguessing:
               print("Too low")
            elif value > numguessing:
               print("Too high")
    print("You won")
    # END: You code here

# Please don't change the code below!!!
def main():
    # Generate a random number
    random_num = random.randint(1,100) 
    answer(random_num)

if __name__ == "__main__":
    main()
# Please don't change the code above!!!