import time

input("엔터를 누르면 시작합니다.")
start = time.time()
input("20초 후에 다시 엔터를 누르세요.")
end = time.time()
et = end - start
print("실제시간 : ", et,"초")
print("차이 : ", abs(et-20),"초")