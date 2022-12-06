def cal_area( height, base ):
    area = 0
# BEGIN : Write your function here
    area= (height*base)/2
# END : Write your function here
    return area
# Please don't change the code below!!!
def main():
    h_value = input("Please input the triangle height: ")
    b_value = input("Please input the triangle base: ")
    print( "The triangle area is {}".format(cal_area(h_value, b_value)) )

if __name__ == "__main__":
    main()
# Please don't change the code above!!!