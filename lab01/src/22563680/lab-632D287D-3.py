def getString() :
    ret = ""
    # START: Write your code here
    points=11
    lives=5
    ret = "You have {} point and {} lines".format(str(points), str(lives))
    # END: Write you code here
    return ret

def main():
    print( getString())

if __name__ == "__main__":
    main()