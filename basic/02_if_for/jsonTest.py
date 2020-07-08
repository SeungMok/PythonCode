import json

data = {
    'coffeeName' : '아메리카노',
    'price' : 2000
}

#json파일 만드는 방법 1
#indent : json파일을 보기 좋게 저장.
with open("./basic/quiz/coffeeList.json","w", encoding="utf-8") as jsonFileMake:
    json.dump(data, jsonFileMake, indent = 4, ensure_ascii=False)

#json파일 만드는 방법 2
with open("./basic/quiz/coffeeList2.json","w", encoding="utf-8") as jsonFileMake:
    jsonFileMake.write(json.dumps(data,indent=4, ensure_ascii=False))

