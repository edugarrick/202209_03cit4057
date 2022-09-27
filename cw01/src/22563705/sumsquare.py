def squaresum(n) :
    sum = 0
    for i in range(1, n+1) :
        sum = sum + (i * i)
    return sum

def main():
    integerN = 4
    print("The sum of square of integer N is",
        squaresum(integerN))

if __name__ == "__main__":
    main()