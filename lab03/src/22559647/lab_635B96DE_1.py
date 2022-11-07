def answer():
    ret = ""
    # START: You code here 
    for num in range(6,17):
        ret += str(num) + "\n"
    for num in range(6,17,2):
        ret += str(num) + "\n"
    ret += "END" 
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    print( answer() )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!