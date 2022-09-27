# 1. Try Arithmetic operator
def simple_interest(p,t,r):
    si = (p*t*r)/100
    return si 

def main():
    principal = 8
    time = 6
    rate = 8
    print('The principal is =', principal)
    print('The time period is', time)
    print('The rate of interest is', rate)
    # Try line wrap within parentheses
    # si = simple_interest(principal, time, rate)
    print('The Simple Interest is', si)
    
if __name__ == "__main__":
    main()