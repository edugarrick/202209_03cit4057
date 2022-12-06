
def answer():
    fileh = open("test.txt", "r", encoding= "utf-8")
    content = fileh.read()
    fileh.close()
    return content

def answer2(num_char):
    fileh = open("test.txt", "r", encoding= "utf-8")
    content = fileh.read(num_char)
    fileh.close()
    return content

def answer3():
    fileh = open("test.txt", "r", encoding= "utf-8")
    content = fileh.readline()
    fileh.close()
    return content

def main():
    print(answer())
    num = 20
    print(answer2(num))
    print(answer3())

if __name__ == "__main__":
    main()
