num = input()
if num.isdecimal() :
    castNum = int(num)
    if castNum % 2 == 1 :
        print("홀수")
    else:
        print("짝수")
else:
    print("숫자가 아닙니다.")
