class Person:
    count = 0

    def __init__(self, name, age = 1):
        self.name = name
        self.__age = age    #private
        Person.count += 1
        print(self.name +"("+str(self.__age)+")")

    def work(self, company):
        print(self.name + "is working in "+company)
        self.__getage()

    def sleep(self):
        print(self.name+"is sleeping")

    def __getage(self):     #private
        print(self.__age)

    @classmethod    #클래스 매소드
    def getCount(cls):
        return cls.count
    

#####################################################3
obj1 = Person("hong")
obj2 = Person("Kim",20)

obj1.work("abc")
obj2.sleep()
#obj1.__getage()

print(obj1.name)
#print(obj1.__age) #접근안됨
print(obj1._Person__age)
print(obj2._Person__age)

print(obj1.getCount())
print(obj1.getCount())
print(Person.getCount())

obj2.count = 8
print(obj2.count)

print(obj2.getCount())