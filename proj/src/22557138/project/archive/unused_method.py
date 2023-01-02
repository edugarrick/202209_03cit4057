# Sam's
from collections import Counter

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ap = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702,
    0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
    0.00772, 0.04025, 0.02406, 0.06749, 0.07507,
    0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
    0.02758, 0.00978, 0.02368, 0.00150, 0.01974,
    0.00074]

def trans(text):
    return ''.join([c.lower() if c.isalpha() else ' ' for c in text])

def find_most_common(text):
    list_cipher = list(text.lower().replace(' ', ''))
    letter = (Counter(list_cipher).most_common(1)[0][0])
    shift_E = ord(letter)-ord('e')
    return shift_E

def find_second_common(text):
    list_cipher = list(text.lower().replace(' ', ''))
    letter = (Counter(list_cipher).most_common(2)[1][0])
    shift_E = ord(letter)-ord('e')
    return shift_E

def find_shifted_a(text):
    words=text.split()
    shifted_word=[letter for letter in words if len(letter)==1]
    shifted_word=(Counter(shifted_word).most_common(1)[0][0])
    shift_a=ord(shifted_word)-ord('a')
    return shift_a

def decryption(text, key):
    output = ''
    for letter in text:
        if letter in alpha:
            position = alpha.find(letter)
            new_position = (position - key) % 26
            new_character = alpha[new_position]
            output += new_character
        elif letter in alpha_upper:
            position = alpha_upper.find(letter)
            new_position = (position - key) % 26
            new_character = alpha_upper[new_position]
            output += new_character
        else:
            output += letter
    return output



# Michael's

from flask import Flask, request, jsonify, Response, json
from key_guess import key_guess
indexpage = "index_en.html"
app = Flask(__name__)

def jsonreply(dictload):
    if list(dictload['properties'].keys())[0] == 'scret_msg':
        str_raw = dictload['properties']['scret_msg']['description']
        retdata = decrypt1(str_raw,key_guess(str_raw))
        retfunc = 'decrypted_text'
    else: 
        retfunc = 'format_error'
        retdata = 'request format error'
    retschema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Caesar Cipher Cracker Reply",
    "type": "object",
    "properties": 
    {
        retfunc: 
        {
        "type": "string",
        "description": retdata
        }
    },
    "required": [retfunc]
    }
    return retschema

@app.route('/json1', methods=['GET','POST'])
def json1():
    dictload = request.json
    result = jsonreply(dictload)
    resp = Response(json.dumps(result),  mimetype='application/json')
    resp.headers.add('Server', 'python flask')
    return resp

@app.route('/json2', methods=['GET', 'POST'])
def json2():
    dictload = request.json
    return jsonify(jsonreply(dictload))
# two ways to response json format

def encode(str_raw, k):
    str_list = list(str_raw.lower())
    str_list_encry = str_list
    for i in range(len(str_list)):
        if 96 < (ord(str_list[i]) + k) < 123:
            str_list_encry[i] = chr(ord(str_list[i]) + k)
        elif 96 < (ord(str_list[i]) + k - 26) < 123:
            str_list_encry[i] = chr(ord(str_list[i]) + k - 26)
    return "".join(str_list_encry)
# encryption function
# but we know the encrypt and decrypt method of Caesar cipher are reversed
# so we can skip it and using a minus key for decrypt function

def decode(str_raw, k):
    str_list = list(str_raw.lower())
    str_list_decry = str_list
    for i in range(len(str_list)):
        if 96 < (ord(str_list[i]) - k) < 123:
            str_list_decry[i] = chr(ord(str_list[i]) - k)
        elif 96 < (ord(str_list[i]) - k + 26) < 123:
            str_list_decry[i] = chr(ord(str_list[i]) + 26 - k)
    return "".join(str_list_decry)
# my first try, output are all lower letters
# mid efficient

def decrypt1(str_raw, k):
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
# second try, most efficient, capability with upper letters
# using in our final version of project

def decrypt2(str_raw, k):
    str_decry = []
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in str_raw:
        if i in alpha:
            str_decry.append(alpha[(alpha.find(i) % 26-k) % 26
                                   + 26*int(i.isupper())])
        else:
            str_decry.append(i)
    return "".join(str_decry)
# third try, mid efficient, capability with upper letters

def find_most_possible(text):
    list_cipher = list(text.lower().replace(' ', ''))
    lens = len(list_cipher)
    modcount = []
    for i in range(26):
        modcount.append([chr(i+97), Counter(list_cipher)[chr(i+97)]/lens])
    eps = 1
    for j in range(26):
        disc = 0
        for p in range(26):
            disc += (modcount[(j+p) % 26][1]-ap[p % 26])**2
        if disc < eps:
            shift = j
            eps = disc
    return shift
    # modified from Sam's idea
    # use variance to guess most possible key
    # need a lot of resources and slow
    # but can fit almost all text written by english

def main():
    path = "files//input.txt"
    with open(path, 'r', encoding='utf-8') as file:
        teststr = file.read()
    print(teststr)
    print(decryption(teststr, find_most_possible(teststr)))


if __name__ == "__main__":
    main()