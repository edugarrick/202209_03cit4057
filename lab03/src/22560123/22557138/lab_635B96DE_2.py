def answer():
    ret = ""
    # START: You code here
    num = 6
    while num < 17:
        ret += str(num) + "\n"
        num += 1
    num = 6
    while num < 17:
        ret += str(num) + "\n"
        num += 2
    else:
        ret += "END"
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    print( answer() )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!