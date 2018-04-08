import random

range = "123456789"
randomlist = random.sample(range,5)
# print(randomlist)
print("GUESS THE 5 DIGIT NUMBER")
userinput = input()

gamestart = 0

if len(userinput) > 5:
    print(" PLEASE ONLY ENTER 5 NUMBERS")
    gamestart = 1


def cows():
    global v
    score =  [str(x) for x in userinput]
    v = 0
    print(score)
    if randomlist[0] == score[0]:
        v += 1
    if randomlist[1] == score[1]:
        v += 1
    if randomlist[2] == score[2]:
        v += 1
    if randomlist[3] == score[3]:
        v += 1
    if randomlist[4] == score[4]:
        v += 1
    print("you have {} cows".format(v))


def bulls():
    userList = [str(x) for x in userinput]
    global v
    z= 0
    # print(randomlist, userList)
    for x in randomlist:
        for y in userList:
            if x == y:
                z += 1

    print("you have {} BULL".format(z))
    z = 0
    #print (v, z)
    if v == 5:
        print("you've won the game")
    return






while gamestart == 0:
    cows()
    bulls()
    userinput = input()
    # del userList
    if userinput == "cheat":
        print(randomlist)



#[int(x) for x in str(num)]
# n = 0
# userList = userinput[n]+userinput[n+1]
# print(userList)