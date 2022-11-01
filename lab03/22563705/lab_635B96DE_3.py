STACK = "Hello world"

def answer(needle):
    found = False
    # START: You code here
    if needle.isalpha():
        for letter in list(STACK.lower()):
            if needle.lower()==letter:
                found = True
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