from collections import UserList
from ctypes.wintypes import WORD
from email import message


def splitString(inputString): 
    # START: Write your code here
    return inputString.split(" ")   ## <Write your code here> 
    # END: Write you code here
 
def main(): 
    userInput = input("Enter a sentense: ")
    word_arr = splitString( userInput )
    word_idx = 1
    for aWord in word_arr :
        print ( "{} word : {} ".format(word_idx, aWord ))
        word_idx = word_idx + 1

if __name__ == "__main__":
    main()