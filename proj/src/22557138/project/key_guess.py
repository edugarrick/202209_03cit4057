def Count(str_raw, CountDict):
    lens = 0
    for i in str_raw:
        if i in CountDict:
            CountDict[i] += 1
            lens += 1
    for i in CountDict.keys():
        CountDict[i] /= lens
    # count only letters, calculate their frequency

def Analysis(p, CountDict):
    eps = 1
    key = 0
    q = list(CountDict.values())
    for i in range(26):
        sum = 0
        for j in range(26):
            t = (i+j) % 26
            sum += p[j]*q[t]
        tem = abs(sum - 0.0655)
        # pre-calculated as a standard value 0.0655
        # 
        # although this is not accurate in math
        # but it require less resources than calculate variance
        # can refer to find_most_possible to check
        if (tem < eps):
            eps = tem
            key = i
        # use least different one as our key
    return key


def key_guess(str_raw):
    # p = [0.082,0.015,0.028,0.042,0.127,
    #     0.022,0.020,0.061,0.070,0.001,
    #     0.008,0.040,0.024,0.067,0.075,
    #     0.019,0.001,0.060,0.063,0.090,
    #     0.028,0.010,0.024,0.020,0.001,
    #     0.001]
    # a little low accuracy than follow, but also works fine
    # its defalult value is 0.065379
    ap = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702,
          0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
          0.00772, 0.04025, 0.02406, 0.06749, 0.07507,
          0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
          0.02758, 0.00978, 0.02368, 0.00150, 0.01974,
          0.00074]
    q = [0 for i in range(26)]
    letter = list("abcdefghijklmnopqrstuvwxyz")
    CountDict = dict(zip(letter, q)) 
    # create a dict like {'a': 0, 'b': 0, ... , 'z': 0}
    Count(str_raw.lower(), CountDict)
    key = Analysis(ap, CountDict)
    return key


def main():
    path = "files/input.txt"
    with open(path,'r',encoding='utf-8') as file:
        teststr = file.read()
    print("最可能的秘钥是："+str(key_guess(teststr)))

if __name__ == "__main__":
    main()
