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

addage(answer,30)

exit()
