def getString() :
    fullName = ""
    # START: Write your code here
    firstName = "Garrick,"
    lastName ="Ho "
    fullName = firstName + lastName
    # END: Write you code here
    return fullName

def main():
    firstName = input("Enter a first name: ") 
    lastName = input("Enter a last name: ") 
    print("Fullname: " + getString())

if __name__ == "__main__":
    main()