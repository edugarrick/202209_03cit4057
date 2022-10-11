
#
#
#def main():
#    while True:
#        
#        userinput = int(input("Please enter a number between 1 to 10: "))
#        
#        if userinput > 10 or userinput < 0 :
#            print("Sorry please enter again")
#            continue
#        else:
#            break
#
#    if userinput >= 6 and userinput <= 10 :
#                print ("The number is between 1 to 10")
#
#    
#
#if __name__ == "__main__":
#    main()
#

def check( userinput ) :
    ret = False
    # START: Write your code here
    if int(userinput) >= 1 and int(userinput) <=10 :
        ret = True
    
    # END: Write you code here
    return ret

def main():
    userinput = input("Enter a number between 1 and 10: ")
    if check(userinput) :
        print("The number is in between 1 to 10.")

if __name__ == "__main__":
    main()