APPLE_PRICE = 3
ORANGE_PRICE = 6

def get_total(fruits, total):
    total = fruits[0] * APPLE_PRICE + fruits[1] * ORANGE_PRICE
    fruits = [1,1]
    return total

def get_total_weird(fruits, total):
    total = fruits[0] * APPLE_PRICE + fruits[1] * ORANGE_PRICE
    fruits[0] = 1
    return total

def main():
    total = 0
    num_orange = 6
    num_apple = 10
    list = [num_apple, num_orange]
    total1 = get_total(list, total)
    total1_compare = get_total(list, total)
    total2 = get_total_weird(list, total)
    total2_compare = get_total_weird(list, total)
    print("total1 = {}, total1_compare = {}".format(total1, total1_compare))
    print("total2 = {}, total2_compare = {}".format(total2, total2_compare))

if __name__ == "__main__":
    main()
