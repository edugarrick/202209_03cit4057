# 1. Try commen
'''
This program calculates the sum of 
square of first N natural 
numbers
'''

def squaresum(n):
   sum = 0
   for i in range(1, n+1) :
       sum = sum + (i * i)
   return sum

def main():
        integerN = 4
        # Try line wrap within parentheses
        print("The sum of square of integer N is ",
        squaresum(integerN))
        
        if __name__ == "__main__":
            main()