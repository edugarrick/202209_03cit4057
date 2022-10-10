#Task 3

def getString() :
    points = 11
    lives = 5
    ret = "You have {} points and {} lives".format(points, lives)

    return ret

def main():
    print( getString())

if __name__ == "__main__":
    main()