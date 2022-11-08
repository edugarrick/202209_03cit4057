import random

def answer( numguessing ):
    # START: You code here  
    while True:
        guess = int(input("Enter a number between 1 to 100: "))
        if guess > int(numguessing):
            print("Too high")
            continue
        elif guess < numguessing :
            print("Too low")
            continue
        else :
            print("You won")
            break
    # END: You code here

# Please don't change the code below!!!
def main():
    # Generate a random number
    random_num = random.randint(1,100) 
    answer(random_num)

if __name__ == "__main__":
    main()
# Please don't change the code above!!!