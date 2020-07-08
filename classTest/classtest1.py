# class Cookie:
#     pass
# a = Cookie()

# print(type(a))

class FourCal:
    mode = 1
    def __init__(self):
        print("생성자")

    def setData(self,first,second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first+ self.second
        return result

a = FourCal()
a.setData(3,6)
print(a.first)
print(a.second)

b = FourCal()
b.setData(3,6)

result = a.add()
print("a.add() = {}".format(result))

print(id(a.first))
print(id(b.first))




print("mode test~~~")
print(FourCal.mode)
print(a.mode)
print(b.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))


print("mode -- > 11")
FourCal.mode = 11
print(FourCal.mode)
print(a.mode)
print(b.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))

print("a.mode --> 10")
a.mode = 10
print(FourCal.mode)
print(a.mode)
print(b.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))