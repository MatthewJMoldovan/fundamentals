#Basic
for x in range(0,151):
    print(x)

#Multiples of 5
for x in range(5,1001,5):
    print(x)

#Counting, the Dojo Way
for x in range(1,100):
    if x%5==0:
        print("Coding Dojo")
    else:
        print(x)

#Whoa, that sucker's huge
sum = 0
for x in range(1, 500000):
    if x%2==1:
        sum = sum + x

print(sum)

#Countdown by 4s
for x in range(2018,0,-4):
    print(x)

#Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum,highNum+1):
    if x%mult == 0:
        print(x)