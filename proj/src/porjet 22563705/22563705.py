def move_nomber(max_letter,letter):
    if ord(max_letter)>ord(letter):
        max_letter=ord(max_letter)%96-ord(letter)%96
        print(max_letter)
        return max_letter
    elif ord(max_letter)<ord(letter):
        max_letter=ord(max_letter)%96+(26-(ord(letter)%96))
        print(max_letter)
        return max_letter
    else:
        max_letter=1
        return max_letter


from collections import Counter
import re
work=str(input('輸入文字：'))
work=re.sub("\W", "", work)
work=re.sub("[\d]","",work)
work=work.lower()
d={}
all=[]
number_key=0
for again_wrok in work.lower():
    if again_wrok not in d:
        d[again_wrok]=1
    else:
        d[again_wrok] += 1
max_key= max(d,key=d.get)
print(max_key)
end=move_nomber(max_key,'e')
all.append(end)
print(end)


second_max_key=d.pop(max_key)
second_max_key=max(d,key=d.get)
print(second_max_key)
end2=move_nomber(second_max_key,'t')
all.append(end2)
print(end2)


third_max_key=d.pop(second_max_key)
third_max_key=max(d,key=d.get)
print(third_max_key)
end3=move_nomber(third_max_key,'a')
all.append(end3)
print(end3)


four_max_key=d.pop(third_max_key)
four_max_key=max(d,key=d.get)
print(four_max_key)
end4=move_nomber(four_max_key,'o')
all.append(end4)
print(end4)


if d=={} and number_key>1:
    end5=48
else:
    fifth_max_key=d.pop(four_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end5=48
elif d!={} and number_key==0:
    fifth_max_key=max(d,key=d.get)
    print(fifth_max_key)
    end5=move_nomber(fifth_max_key,'i')
    all.append(end5)
print(end5)


if d=={} and number_key>1:
    end6=47
else:
    six_max_key=d.pop(fifth_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end6=47
elif d!={} and number_key==0:    
    six_max_key=max(d,key=d.get)
    print(six_max_key)
    end6=move_nomber(six_max_key,'n')
    all.append(end6)
print(end6)


if d=={} and number_key>1:
    end7=46
else:
    seven_max_key=d.pop(six_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end7=46
elif d!={} and number_key==0:
    seven_max_key=max(d,key=d.get)
    print(seven_max_key)
    end7=move_nomber(seven_max_key,'s')
    all.append(end7)
print(end7)


if d=={} and number_key>1:
    end8=45
else:
    eight_max_key=d.pop(seven_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end8=45
elif d!={} and number_key==0:
    eight_max_key=max(d,key=d.get)
    print(eight_max_key)
    end8=move_nomber(eight_max_key,'h')
    all.append(end8)
print(end8)


if d=={} and number_key>1:
    end9=44
else:
    night_max_key=d.pop(eight_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end9=44
elif d!={} and number_key==0:
    night_max_key=max(d,key=d.get)
    print(night_max_key)
    end9=move_nomber(night_max_key,'r')
    all.append(end9)
print(end9)


if d=={} and number_key>1:
    end10=43
else:
    ten_max_key=d.pop(night_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end10=43
elif d!={} and number_key==0:
    ten_max_key=max(d,key=d.get)
    print(ten_max_key)
    end10=move_nomber(ten_max_key,'d')
    all.append(end10)
print(end10)


if d=={} and number_key>1:
    end11=42
else:
    eleven_max_key=d.pop(ten_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end11=42
elif d!={} and number_key==0:
    eleven_max_key=max(d,key=d.get)
    print(eleven_max_key)
    end11=move_nomber(eleven_max_key,'l')
    all.append(end11)
print(end11)


if d=={} and number_key>1:
    end12=41
else:
    twelve_max_key=d.pop(eleven_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end12=41
elif d!={} and number_key==0: 
    twelve_max_key=max(d,key=d.get)
    print(twelve_max_key)
    end12=move_nomber(twelve_max_key,'c')
    all.append(end12)
print(end12)


if d=={} and number_key>1:
    end13=40
else:
    thirteen_max_key=d.pop(twelve_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end13=40
elif d!={} and number_key==0: 
    thirteen_max_key=max(d,key=d.get)
    print(thirteen_max_key)
    end13=move_nomber(thirteen_max_key,'u')
    all.append(end13)
print(end13)


if d=={} and number_key>1:
    end14=39
else:
    fourteen_max_key=d.pop(thirteen_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end14=39
elif d!={} and number_key==0: 
    fourteen_max_key=max(d,key=d.get)
    print(fourteen_max_key)
    end14=move_nomber(fourteen_max_key,'m')
    all.append(end14)
print(end14)


if d=={} and number_key>1:
    end15=38
else:
    fifteen_max_key=d.pop(fourteen_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end15=38
elif d!={} and number_key==0: 
    fifteen_max_key=max(d,key=d.get)
    print(fifteen_max_key)
    end15=move_nomber(fifteen_max_key,'w')
    all.append(end15)
print(end15)


if d=={} and number_key>1:
    end16=37
else:
    sixteen_max_key=d.pop(fifteen_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end16=37
elif d!={} and number_key==0: 
    sixteen_max_key=max(d,key=d.get)
    print(sixteen_max_key)
    end16=move_nomber(sixteen_max_key,'f')
    all.append(end16)
print(end16)


if d=={} and number_key>1:
    end17=36
else:
    seventeen_max_key=d.pop(sixteen_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end17=36
elif d!={} and number_key==0: 
    seventeen_max_key=max(d,key=d.get)
    print(seventeen_max_key)
    end17=move_nomber(seventeen_max_key,'g')
    all.append(end17)
print(end17)


if d=={} and number_key>1:
    end18=35
else:
    eighteen_max_key=d.pop(seventeen_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end18=35
elif d!={} and number_key==0:    
    eighteen_max_key=max(d,key=d.get)
    print(eighteen_max_key)
    end18=move_nomber(eighteen_max_key,'y')
    all.append(end18)
print(end18)


if d=={} and number_key>1:
    end19=34
else:
    nineteen_max_key=d.pop(eighteen_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end19=34
elif d!={} and number_key==0:
    nineteen_max_key=max(d,key=d.get)
    print(nineteen_max_key)
    end19=move_nomber(nineteen_max_key,'p')
    all.append(end19)
print(end19)


if d=={} and number_key>1:
    end20=33
else:
    twenty_max_key=d.pop(nineteen_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end20=33
elif d!={} and number_key==0:
    twenty_max_key=max(d,key=d.get)
    print(twenty_max_key)
    end20=move_nomber(twenty_max_key,'b')
    all.append(end20)
print(end20)


if d=={} and number_key>1:
    end21=32
else:
    twenty_one_max_key=d.pop(twenty_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end21=32
elif d!={} and number_key==0:    
    twenty_one_max_key=max(d,key=d.get)
    print(twenty_one_max_key)
    end21=move_nomber(twenty_one_max_key,'v')
    all.append(end21)
print(end21)


if d=={} and number_key>1:
    end22=31
else:
    twenty_two_max_key=d.pop(twenty_one_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end22=31
elif d!={} and number_key==0:
    twenty_two_max_key=max(d,key=d.get)
    print(twenty_two_max_key)
    end22=move_nomber(twenty_two_max_key,'k')
    all.append(end22)
print(end22)


if d=={} and number_key>1:
    end23=30
else:
    twenty_three_max_key=d.pop(twenty_two_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end23=30
elif d!={} and number_key==0: 
    twenty_three_max_key=max(d,key=d.get)
    print(twenty_three_max_key)
    end23=move_nomber(twenty_three_max_key,'j')
    all.append(end23)
print(end23)


if d=={} and number_key>1:
    end24=29
else:
    twenty_four_max_key=d.pop(twenty_three_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end24=29
elif d!={} and number_key==0:    
    twenty_four_max_key=max(d,key=d.get)
    print(twenty_four_max_key)
    end24=move_nomber(twenty_four_max_key,'x')
    all.append(end24)
print(end24)


if d=={} and number_key>1:
    end25=28
else:
    twenty_fifth_max_key=d.pop(twenty_four_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end25=28
elif d!={} and number_key==0:
    twenty_fifth_max_key=max(d,key=d.get)
    print(twenty_fifth_max_key)
    end25=move_nomber(twenty_fifth_max_key,'q')
    all.append(end25)
print(end25)


if d=={} and number_key>1:
    end26=27
else:
    twenty_six_max_key=d.pop(twenty_fifth_max_key)
if d=={} and number_key==0:
    number_key=Counter(all).most_common(1)[0][0]
    print(number_key)
    end26=27
elif d!={} and number_key==0:
    twenty_six_max_key=max(d,key=d.get)
    print(twenty_six_max_key)
    end26=move_nomber(twenty_six_max_key,'z')
    all.append(end26)
print(end26)

print(number_key)

number_key2=0
answer=[]
for work2 in work:
    work2=ord(work2)
    if number_key2==0:
        number_key2=number_key
    while number_key2 >0:
        if work2<123 and work2!=97:
            number_key2=number_key2-1
            work2=work2-1
        elif work2==97:
            number_key2=number_key2-1
            work2=122
    work2=chr(work2)
    answer.append(work2)
str=''
def main():
    print(str.join(answer))

if __name__ == "__main__":
    main()
