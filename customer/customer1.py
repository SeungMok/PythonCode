import json
import re
import io

page=-1
with open("./customer/customer.json", "rt", encoding="utf-8") as f:
    custlist = json.load(f)

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

    if choice=="I": 
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
        page += 1
        print(page)
        with io.open("./customer/customer.json", "wt", encoding="utf-8") as f:
            json.dump(custlist, f, indent = 4, ensure_ascii=False)
        
    elif choice=="C":
        print("현재 고객 정보 조회")
        if page >= 0:
            print("현재 페이지는 {}쪽 입니다.".format(page+1))
            print(custlist[page])
        else:
            print("입력된 정보가 없습니다.")
    elif choice == 'P':
        print("이전 고객 정보 조회")
        if(page <= 0):
            print("첫 번째 페이지이므로 이전 페이지이동이 불가합니다.")
            print(custlist[page])
    elif choice == 'N':
        print("다음 고객 정보 조회")
        if page >= len(custlist)-1:
            print('마지막 페이지이므로 다음페이지로 이동이 불가능합니다.')
    elif choice=='D':
        print("고객 정보 삭제")
        
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

    elif choice=="U": 
        idx = -1
        print("고객 정보 수정")
        for i in custlist:
            print(i['name'],':',i['email'])
        
        inputEmail = input('수정할 고객의 이메일을 입력하세요 : ')
        for i in range(0, len(custlist)):
            if custlist[i]['email'] == inputEmail:
                idx = i
                while True:
                    menu = input('''
                    수정할 정보의 숫자를 입력하세요
                    1. 이름(Name)
                    2. 성별(Gender)
                    3. 출생년도(BirthYear)
                    4. 수정할 내용 없음.종료(exit)
                    ''')
                    if menu == '1':
                        print("현재 이름 : {}".format(custlist[idx]['name']))
                        custlist[idx]['name'] = input('변경할 이름 : ')
                        print("변경 된 이름 : {}".format(custlist[idx]['name']))
                        pass
                    elif menu == '2':
                        print("현재 성별 : {}".format(custlist[idx]['gender']))
                        custlist[idx]['gender'] = input('변경할 성별 : ')
                        pass
                    elif menu == '3':
                        print("현재 출생년도 : {}".format(custlist[idx]['birthyaer']))
                        custlist[idx]['birthyaer'] = input('변경할 출생년도 : ')
                        pass
                    elif menu == '4':
                        print("수정 종료")
                        break
                    else:
                        print("1~4사이 값을 입력하시오")
        
        with io.open("./customer/customer.json", "wt", encoding="utf-8") as f:
                    json.dump(custlist, f, indent = 4, ensure_ascii=False)


    elif choice=="Q":
        print("프로그램 종료")
        break