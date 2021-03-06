import json, io, re
with open("./customer/customer.json", "rt", encoding="utf-8") as f:
    custlist = json.load(f)
page = len(custlist)-1
custlistLen = len(custlist)-1

def exe(choice):
        if choice=='I':
            insertData()
        
        elif choice=='C':
            curSearch()
        
        elif choice=='P':
            preSearch()

        elif choice=='N':
            nextSearch()

        elif choice=='U':
            updateData()
        
        elif choice=='D':
            deleteData()
        
        elif choice=='Q':
            quit()
            
def insertData():
    customerInfo={} 
    print("고객 정보 입력")
    customerInfo["name"] = input("이름 : ")
        
    while True:
        gender = input("성별(남자 M, 여자 F) : ").upper()
        if gender in ('M','F'):
            customerInfo["gender"] = gender
            break
        else:
            print("m,M 또는 f,F를 입력하세요")
        
    while True:
        check = 0
        p = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}.[a-z]{2,5}')
        customerInfo["email"] = input("email : ")
        email = customerInfo["email"]
        if p.match(email) != None :
            for i in custlist:
                if i['email'] == customerInfo['email']:
                    check = 1
            if check==0:
                break
            print("중복되는 이메일이 있습니다.")
        else:
            print("형식에 맞지 않습니다.")
    
    while True:
        customerInfo["birthyear"] = input("출생년도 4자리 : ")
        if len(customerInfo['birthyear']) == 4 and customerInfo['birthyear'].isdecimal() :
            customerInfo['birthyear'] = int(customerInfo['birthyear'])
            break
        
    custlist.append(customerInfo)
    global page
    page += 1
    print(page)
    with io.open("./customer/customer.json", "wt", encoding="utf-8") as f:
        json.dump(custlist, f, indent = 4, ensure_ascii=False)
            
    pass
  
def curSearch():
    print("현재 고객 정보 조회")
    global page
    if page >= 0:
        print("현재 페이지는 {}쪽 입니다.".format(page+1))
        print(custlist[page])
    else:
        print("입력된 정보가 없습니다.")
    pass

def preSearch():
    print("이전 고객 정보 조회")
    global page
    if page <= 0 :
        print("첫 번째 페이지이므로 이전 페이지이동이 불가합니다.")
        print(custlist[page])
    else:
        page -= 1
        print(custlist[page])
        print(page)
    pass
        
def nextSearch():
    print("다음 고객 정보 조회")
    global page
    global custlistLen
    if page >= custlistLen :
        print("마지막 페이지이므로 이전 페이지이동이 불가합니다.")
        print(custlist[page])
    else:
        page += 1
        print(custlist[page])
        print(page)
    pass

def deleteData():
    print("고객 정보 삭제")
    global page
    for i in custlist:
        print(i['name'],':',i['email'])
    
    inputEmail = input('삭제할 고객의 이메일을 입력하세요 : ')
    delok = 0
    for i in range(0, len(custlist)):
        if custlist[i]['email'] == inputEmail:
            print('{} 님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
            del custlist[i]
            delok = 1
            with io.open("./customer/customer.json", "wt", encoding="utf-8") as f:
                json.dump(custlist, f, indent = 4, ensure_ascii=False)

        if delok == 1:
            break
    if delok == 0:
        print('일치하는 이메일이 없습니다.')
    print()
    page = len(custlist)-1
    pass

def updateData(): 
    idx = -1
    print("고객 정보 수정")
    for i in custlist:
        print(i['name'],':',i['email'])
    
    inputEmail = input('수정할 고객의 이메일을 입력하세요 : ')
    for i in range(0, len(custlist)):
        if custlist[i]['email'] == inputEmail:
            idx = i
            while True:
                choice = input('''
                수정할 정보를 입력하세요
                name, gender, birthyear
                수정을 종료하시려면 exit
                >>>''')
                if choice in ('name','gender','birthyear'):
                    print("현재 {} : {}".format(choice,custlist[idx][choice]))
                    custlist[idx][choice] = input('변경할 {} : '.format(choice))
                    print("변경 된 {} : {}".format(choice,custlist[idx]['name']))
                    pass
                elif choice == 'exit':
                    print("수정을 종료합니다.")
                    break
                else:
                    print("입력값이 잘못 되었습니다.")
    
    with io.open("./customer/customer.json", "wt", encoding="utf-8") as f:
                json.dump(custlist, f, indent = 4, ensure_ascii=False)

    pass


              
while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()

    exe(choice)