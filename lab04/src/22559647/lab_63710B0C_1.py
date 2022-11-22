STACK = "This is a test input"

def answer( str_val ):
    ret = ""
    # START: You code here 
    ret = str_val[0:6]
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    userInput = input("Enter a string: ")
    print( answer(userInput) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!