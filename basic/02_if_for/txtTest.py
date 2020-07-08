import json

# f = open("test.txt", 'w', encoding='UTF-8')
# f.write("txt파일 생성합니다")
# f.close()

f=open("./basic/quiz/test.txt", 'r', encoding='UTF-8')
line = "a"
while line:
    line = f.readline()
    print(line)
f.close()