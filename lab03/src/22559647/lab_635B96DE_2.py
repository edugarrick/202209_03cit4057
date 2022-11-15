def answer():
    ret = ""
    # START: You code here
    count = 6
    while count < 17:
       ret += str(count) + "\n"
       count = count + 1
    count = 6   
    while count < 17:
        ret += str(count) + "\n"
        count = count + 2
    ret += "END"
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    print( answer() )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!