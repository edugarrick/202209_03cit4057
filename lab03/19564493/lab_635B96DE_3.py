STACK = "Hello world"

def answer(needle):
    found = False
    # START: You code here
    needle = needle.lower()
    for i in list(STACK.lower()):
        if needle == i:
            found = True
            break  
    # if needle != STACK.isalpha():

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