def getString() :
    ret = ""
    # START: Write your code here
    points = 11
    lives = 5
    ret = "You have {} points and {} lives".format(points,lives)
    # END: Write you code here
    return ret

def main():
    print( getString())

if __name__ == "__main__":
    main()