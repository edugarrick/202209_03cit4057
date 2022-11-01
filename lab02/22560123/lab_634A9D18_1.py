import random

def answer( numguessing ):
    # START: You code here
    numberInput = 0
    while (numguessing!=numguessing):
        numberInput = int(input ("Enter a number between 1 to 100:"))
        if numberInput == numguessing:
            print("You won")
        elif numberInput < numguessing:
            print("too low")
        else: 
             numberInput > numguessing
             print("too high") 
    # END: You code here

# Please don't change the code below!!!
def main():
    # Generate a random number
    random_num = random.randint(1,100) 
    answer(random_num)

if __name__ == "__main__":
    main()
# Please don't change the code above!!!