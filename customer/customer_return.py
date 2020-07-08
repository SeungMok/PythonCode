import json, io
import customer_Func

with open("./customer/customer.json", "rt", encoding="utf-8") as f:
    custlist = json.load(f)
page = len(custlist)-1
custlistLen = len(custlist)-1

def exe(choice,page):
        if choice=='I':
            page = customer_Func.insertData(page,custlist)

        elif choice=='C':
            customer_Func.curSearch(page,custlist)
        
        elif choice=='P':
            page = customer_Func.preSearch(page,custlist)

        elif choice=='N':
            page = customer_Func.nextSearch(page,custlist)

        elif choice=='U':
            customer_Func.updateData(custlist)
        
        elif choice=='D':
            customer_Func.deleteData(page,custlist)
        
        elif choice=='Q':
            quit()
            
              
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
    >>>''').upper()

    exe(choice,page)