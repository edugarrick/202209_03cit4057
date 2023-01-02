FILE = "lab06/src/00000000/message.txt"

def findMaxCharInString( astring ):
    maxCharIndex = 0
    charCounts = [0]*26 #initialize 26 letter counters
    for c in astring:
        c = c.lower()
        if 'a' <= c <= 'z':
            charCounts[ord(c)-ord('a')] += 1
    
    maxCharCount = max(charCounts)
    maxCharIndex = charCounts.index(maxCharCount)
    return maxCharIndex

def getStringFromFile( filename ):
    ret = ""
    with open(filename, "r") as fp:
        ret = fp.read()
    return ret

def main():
    message = getStringFromFile(FILE)
    print("Message is: {}".format(message))
    index = findMaxCharInString(message)
    char = chr(97+index)
    print("The Index with max freq: {}".format(index))
    print("The Char with max freq: {}".format(char))
    
if __name__ == "__main__":
    main()