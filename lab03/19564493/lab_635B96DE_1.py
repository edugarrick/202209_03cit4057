def answer():
    ret = ""
    # START: You code here
    for q in range(6,16+1):
        ret+=str(q) + '\n'
    for q in range(6,16+1,2):
        ret+=str(q) + '\n'
        
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    print( answer() )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!