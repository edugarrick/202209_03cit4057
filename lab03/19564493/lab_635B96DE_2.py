def answer():
    ret = ""
    q=6
    # START: You code here
    while(q < 16+1):
        ret+=str(q) + '\n'
        q =q+1
    q=6
    while(q < 16+1):
        ret+=str(q) + '\n'
        q=q+2
        print("end")
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    print( answer() )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!