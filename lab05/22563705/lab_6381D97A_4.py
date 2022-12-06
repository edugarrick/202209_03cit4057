def get_list():
    my_list = ["Apple","Orange","Banana","Grape","Orange","Grape"]
    return my_list

def answer(your_set):
    return list(set(your_set))
    
def main():
    fruitlist = get_list()
    print("List:")
    print(fruitlist)
    print("After remove duplicates:")
    print(answer(fruitlist) )

if __name__ == "__main__":
    main()
