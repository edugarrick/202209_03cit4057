def toFileFromLine( aline ):
    with open("test01.txt", "w") as f:
        f.write(aline)


def toFileFromEssay( liststrings ):
    with open("test02.txt", "w") as f:
        f.writelines(liststrings)

def errorFunctiontoFileFromEssay( liststrings ):
    with open("test03.txt", "w") as f:
        f.writelines(liststrings)

def main():
    line = "Hello world!"
    toFileFromLine( line )
    essay = ["Hello\n", "world\n", "!"]
    toFileFromEssay( essay )
    errorFunctiontoFileFromEssay( essay )

if __name__ == "__main__":
    main()
