def getString() :
    ret = ""
    # START: Write your code here
    point = 11
    live = 5
    ret="You have {} points and {} lives".format(point,live)
    # END: Write you code here
    return ret

def main():
    print( getString())

if __name__ == "__main__":
    main()