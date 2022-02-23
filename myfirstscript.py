""" A quick script to practice my python with """

answer = int(input("what is your age? "))

print("you answered: ", answer)

if answer < 10:
    print ("you are very young")
elif answer == 10:
    print ("you are exactly 10")
else:
    print ("you are nearly old")

def addage(num1, num2):
    result = num1 + num2
    print ("in ", num2 , "years, you'll be ",result)

def con():
    answer = input("would you like to contine? type y/n:  ")
    if answer == "y":
        print("continuing")
    elif answer == "n":
        print ("exiting")
        exit()
    else:
        print("please answer in lower case 'y' or 'n'")
        exit()

addage(answer,30)

con()
print ("now that we have the ages covered.. we'll move on to lists")
lists = [ 'a', 1 , 12.2 ]
print (lists)
print (lists[1])
lists[1] = 'b'
print (lists)
lists.append("new")
print(lists)

print ("now we'll move on to tuples which are lists that can not be changed.")
t = (1,"a",2)
print (t[0])

print ("now we'll move on the Dicts")
dict = {"apple":2,"pear":4,"bonana":5,"pumpkin":6}

for i in dict:
    print (i)
for i in dict.items():
    print (i)
for i , x in dict.items():
    print ("you have {} {}".format(i,x))
"""a little better read"""
for fruit, quant in dict.items():
    print ("you have {} {}".format(quant,fruit))

print(dict["apple"])
dict["pear"] = 17
dict["peach"] = 1
print(dict)

start = 0
while start < 5:
    print(start)
    start +=1

from time import sleep
while True:
    try:
        print("polling... press any key to stop")
        sleep(1)
    except KeyboardInterupt:
        break
exit()
