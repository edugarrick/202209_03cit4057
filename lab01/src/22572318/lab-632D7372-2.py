myInput = ["This ", "is ", "a ", "test ", "message."]

def mergeString(inputList): 
    mergeString = "".join(myInput)
    return mergeString## <Write your code here>
 
def main(): 
    aSentence = mergeString( myInput )
    print(aSentence)

if __name__ == "__main__":
    main()