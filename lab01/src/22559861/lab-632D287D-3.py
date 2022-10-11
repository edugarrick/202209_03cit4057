def getString() :
    ret = ""
    points = 11
    lives = 5
    ret = "You have {} points and {} lines".format(points, lives) 
    
    return ret

def main():
    print( getString())

if __name__ == "__main__":
    main()