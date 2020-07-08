import random
import time,pickle
import json

with open("./basic/quiz/word.txt","rb") as f:
    wordList = []
    while True:
        line = f.readline().decode("utf-8").rsplit("\n")
        print("뭔가 이상하다 line : {}".format(line))
        if not line:
            break
        wordList.append(line)
        
with open("./basic/quiz/resultGameList.json","rt") as f:
    rank = json.load(f)

while True :
    print("1.타자게임 2.문제불러오기 3.문제저장하기 4.등수 5.종료하기")
    menu = input("메뉴를 선택하세요 : ")
    if menu =='1':
        cnt = 0
        prompt = '''
        --------------------------
            한 컴 타 자 연 습
        --------------------------
        '''
        print("이 게임은 나타나는 단어를 빠르고 정확하게 입력하면 되는 게임입니다.")
        input("엔터를 누르면 게임이 시작됩니다.")
        print(prompt)
        start = time.time()
        for i in range(0,3):
            word = random.choice(wordList)
            while True:
                print("단어 :",word)
                inputText = input("입력 : ")
                if inputText == word :
                    cnt+=1
                    break
        end = time.time()

        print("정확한 단어 입력 개수 : {}".format(cnt))
        print("걸린시간 : {}".format(end-start))
        name = input("playetr 이름을 입력하세요 : ")

        rank[name] = float(end-start)

        #json으로 저장
        with open("./basic/quiz/resultGameList.json", 'wt') as userResult:
            json.dump(rank, userResult, indent=4, ensure_ascii=False)
        print(rank)
        pass
    elif menu =='2':
#       f=open("./basic/quiz/word.pickle","rb") #피클은 확장자 아무거나 상관없음
#       pickle.dump(wordList,f)
#       word = pickle.load(f)
        with open('./basic/quiz/word.pickle','rb') as f:
            word = pickle.load(f)
            print(word)
        pass
    elif menu =='3':
        f=open("./basic/quiz/word.pickle","wb") #피클은 확장자 아무거나 상관없음
        with open('./basic/quiz/word.pickle', 'rb') as wordList:
            listData = pickle.load(wordList)
            pickle.dump(listData,f)
        f.close()
        pass
    elif menu =='4':
        rankList = sorted(rank.items(), key=lambda x:x[1])
        num = 1
        for k,v in rankList:
            print("{}등 {} : {}초".format(num,k,v))
            num+=1
        pass
    elif menu =='5':
        print("프로그램을 종료합니다.")
        break
    else:
        print("1~5 입력하세요.")
        pass
