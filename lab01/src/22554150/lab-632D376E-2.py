def getString(firstName, lastName ) :
    fullName = ""
    #fullName.join([fist])
    # START: Write your code here
    # Please use .join()
    name = (firstName,lastName)
    
    fullName = (" ".join(name))
    
    
    # END: Write you code here
    return fullName

def main():
    firstName = input("Enter a first name: ") 
    lastName = input("Enter a last name: ") 
    print("Fullname: " + getString(firstName,lastName ))

if __name__ == "__main__":
    main()