from tkinter import END


def answer():
    ret = ""
    # START: You code here
    i=6
    while(i<=16):
        ret+= str(i)+"\n"
        i+=1
    while(i<=16):
        ret+= str(i)+"\n"
        i+=2
    print('END')
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    print( answer() )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!