encrypted = open("message.txt", "r")   
message = (encrypted.read()).upper()
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def most_frequent(List):
    counter = 0
    num = List[0]    
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i 
    return num

def sec_frequent(List2):
    counter = 0
    num = List2[0]     
    for i in List2:
        curr_frequency = List2.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num

def thr_frequent(List3):
    counter = 0
    num = List3[0]     
    for i in List3:
        curr_frequency = List3.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num

List =[*message.replace(" ","")]
List2 = [*(message.replace(" ","")).replace(most_frequent(List),"")]
List3 = [*((message.replace(" ","")).replace(most_frequent(List),"")).replace(sec_frequent(List2),"")]
print("most frequent letter :" + most_frequent(List))
print("Second most frequent Lettter :" + sec_frequent(List2))
print("Third most frequent Lettter :" + thr_frequent(List3))
Shift1 = LETTERS.find(most_frequent(List))-4
if Shift1 <0:
    Shift1=int(Shift1)+26

Shift2 = LETTERS.find(sec_frequent(List2))-4
if Shift2 <0:
    Shift2=int(Shift2)+26

Shift3 = LETTERS.find(thr_frequent(List3))-4
if Shift3 <0:
    Shift3=int(Shift3)+26

print ("Frist key = Shift" + " " + str(Shift1))
print ("Second key = Shift" + " " + str(Shift2))
print ("Thrid key = Shift" + " " + str(Shift3))

translated = ''
key = Shift1
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
         
        num = num - key
        if num < 0:
            num = num + len(LETTERS)
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol
print('Frist Hacking key #%s: %s' % (key, translated))

translated = ''
key = Shift2
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        num = num - key
        if num < 0:
            num = num + len(LETTERS)
        translated = translated + LETTERS[num]
    else:
         translated = translated + symbol
print('Second Hacking key #%s: %s' % (key, translated))

translated = ''
key = Shift3
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        num = num - key
        if num < 0:
            num = num + len(LETTERS)
        translated = translated + LETTERS[num]
    else:
         translated = translated + symbol
print('Thrid Hacking key #%s: %s' % (key, translated))
   
   
   
   
   
#Try compare all key
#for key in range(len(LETTERS)):
  # translated = ''
   #for symbol in message:
    #  if symbol in LETTERS:
     #    num = LETTERS.find(symbol)
      #   num = num - key
       #  if num < 0:
        #    num = num + len(LETTERS)
        # translated = translated + LETTERS[num]
      #else:
       #  translated = translated + symbol


#print('Hacking key #%s: %s' % (key, translated))





