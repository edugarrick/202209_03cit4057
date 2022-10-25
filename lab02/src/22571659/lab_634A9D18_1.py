import random

def answer( numguessing ):
    # START: You code here  
    yourNum = int(imput("Please enter an intenger between 1 to 100:"))
    while(numguessing < yourNum):
        print("Too low")
        break
    while(numguessing > yourNum):
        print("Too high")
        break
    while(numguessing == yourNum):
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