def answer():
    ret = ""
    # START: You code here
    i=6 
    j=6
    while i<=16:
        ret+=str(i)+"\n"
        i+=1
    while j<=16:
        ret+=str(j)+"\n"
        j+=2
    else:
        ret+="End"
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    print( answer() )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!