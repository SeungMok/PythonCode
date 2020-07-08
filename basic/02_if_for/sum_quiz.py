import random

count = 0
for i in range(0,10):
    randomNum1 = random.randint(1,50)
    randomNum2 = random.randint(1,50)
    print("{} + {} = ".format(randomNum1,randomNum2))
    inputNum = int(input())
    result = randomNum1 + randomNum2
    if(result == inputNum):
        print("정답!")
        count+=1
    else:
        print("오답!")
        print("정답 : {}".format(result))

print("총 {}개 정답".format(count))