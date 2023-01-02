def decrypt(str_raw, k):
    str_decry = []
    for i in str_raw:
        if i.isalpha():
            if i.islower():
                str_decry.append(chr(97+(ord(i)-97-k) % 26))
            else:
                str_decry.append(chr(65+(ord(i)-65-k) % 26))
        else:
            str_decry.append(i)
    return "".join(str_decry)

def main():
    filepath = "./files/input.txt"
    while 1:
        print("1. 终端\n2. 选择文件\n3. 读取input.txt")
        operation = input("请选择：\t")
        if operation == "1":
            raw = input("请输入原文:\t")
        elif operation == "2":
            path = input("请输入文件地址:\t")
            raw = open(path, "r", encoding="utf-8").read()
        elif operation == "3":
            path = filepath
            raw = open(path, "r", encoding="utf-8").read()
        else:
            print("您的输入有误！")
        print("1. 加密\n2. 解密")
        func = input("请选择：\t")
        if func == "1":
            steps = int(input("请输入偏移:\t"))
            print("结果为：\t"+decrypt(raw, -steps)+"\n")
        elif func == "2":
            steps = int(input("请输入偏移:\t"))
            print("结果为：\t"+decrypt(raw, steps)+"\n")
        else:
            print("您的输入有误！")


if __name__ == "__main__":
    main()
