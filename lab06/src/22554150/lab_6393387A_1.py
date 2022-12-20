FILE = "lab06/src/22554150/message.txt"


def findMaxCharInString( astring ):
    maxCharIndex = 0
    charCounts = [0]*26
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
    print("The index with max freq: {}".format(
        findMaxCharInString(message)))

if __name__ == "__main__":
    main()
