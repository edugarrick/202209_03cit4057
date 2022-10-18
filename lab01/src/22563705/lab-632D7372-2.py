myInput = ["This ", "is ", "a ", "test ", "message."]

def mergeString(inputList): 
    return  "".join(myInput)## <Write your code here>
 
def main(): 
    aSentence = mergeString( myInput )
    print(aSentence)

if __name__ == "__main__":
    main()