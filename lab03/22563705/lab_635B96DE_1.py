import re


def answer():
    ret = ""
    # START: You code here 
    for i in range(6,17):
        ret+= str(i)+ '\n'
    for i in range(6,17,2):
        ret+= str(i)+ '\n'
    else:
        ret +='END'  
    # END: You code here
    return ret

# Please don't change the code below!!!
def main():
    print( answer() )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!