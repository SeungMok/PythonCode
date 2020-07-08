prompt = '''

--------------------------------
        커피 자판기 메뉴
--------------------------------
1. 커피 메뉴 입력
2. 커피 메뉴 삭제
3. 커피 주문하기
4. 커피 추출하기
5. 커피 메뉴 리스트
6. 종료
--------------------------------
메뉴선택 >>>> '''

coffeeList = {'아메리카노': 2000, '카페라떼': 2500, '카페모카' : 3000, '아메에리카' : 6000, '아이스아메리카노' : 4000}
coffeeStock = {'원두' : 200, '우유': 300, '물' : 1000}
amerianoRecipy = {'원두' : 50, '물' : 400}
cafelatteRecipy = {'원두' : 50, '우유' : 350}

customerSelectCoffee = ""

while True:
    print(prompt)
    menu = input()
    if menu == '1':
        print("커피 메뉴를 추가 합니다.")
        coffeeName = input("커피 이름 : ")
        coffePrice = input("커피 가격 :  ")
        coffeeList[coffeeName] = int(coffePrice)
        pass
    elif menu == '2':
        print("커피 메뉴를 삭제 합니다.")
        coffeeName = input("삭제하실 커피 이름 : ")
        del coffeeList[coffeeName]
        pass
    elif menu == '3':
        money = 0
        customerCoffee = input("주문하실 커피명 : ")
        coffeePrice = coffeeList[customerCoffee]
        print("가격 : ", coffeePrice)
        while True :
            money += int(input("금액을 투입하세요 : "))
            print("입력금액 : {}".format(money))
            if money >= coffeePrice : 
                print("투입금액 : {}, 잔액 : {}".format(money,money-coffeePrice))
                print("4를 입력하시면 {}가 나옵니다.".format(customerCoffee))
                break
            else:
                print("금액이 부족합니다.")
                print("투입금액 : {}, 부족한 금액 : {}".format(money,coffeePrice-money))
            if money < coffeePrice:
                continue
        pass
    elif menu == '4':
        
        pass
    elif menu == '5':
        print("-----------------------------")
        print("     메뉴         가격        ")
        for k,v in coffeeList.items():
            print("{:#<10}|{:>8,}원".format(k,v))
        pass
    elif menu == '6':
        print("프로그램 종료")
        break
    else :
        print("1~6 를 입력하세요")