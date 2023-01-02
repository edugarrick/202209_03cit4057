STACK = "Hello world"

def answer(needle):
    found = False
    # START: You code here
    STACK_lower =STACK.lower()
    needle=needle.lower()
    for letter in STACK_lower:
        if needle in letter:
            found=True
            break


    
    # END: You code here
    return found

# Please don't change the code below!!!
def main():
    letter = input("Please enter a letter: ")
    if answer(letter) :
        print("Found.")
    else:
        print("Not found.")

if __name__ == "__main__":
    main()
# Please don't change the code above!!!