import random
import time
 
cnt = 0
input("자 게임을 시작하지. (Enter를 누르면 게임이 시작됩니다)")
start = time.time()
for i in range(0,3):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    operatorList = ["+", "-", "*", "//"]

    operator = random.choice(operatorList)

    
    print("{} {} {} = ".format(num1,operator,num2))
    inputNum = int(input())

    result = 0

    if(operator == "+"):
        result = num1 + num2
    elif(operator == "-"):
        result = num1 - num2
    elif(operator == "*"):
        result = num1 * num2
    elif(operator == "//"):
        result = num1 // num2

    if(result == inputNum):
        print("정답")
        cnt+=1
    else:
        print("오답")
        print("정답 : {}".format(result))
end = time.time()
print("소요시간 : {}".format(abs(end-start)))
print("정답 갯수 : {}".format(cnt))