def getString(firstName, lastName) :
    fullName = ""
    # START: Write your code here
   
    fullName = "{} {}".format(firstName,lastName)
    # Please use .format()

    # END: Write you code here
    return fullName

def main():
    firstName = input("Enter a first name: ") 
    lastName = input("Enter a last name: ") 
    print("Fullname: " + getString(firstName,lastName ))

if __name__ == "__main__":
    main()