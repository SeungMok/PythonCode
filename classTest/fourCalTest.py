class FourCal:
    def __init__(self, first = 1, second = 4):
        self.first = first
        self.second = second
        print("생성자")

    def setData(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

#####################################################

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
    def div(self):
        if self.second == 0 :
            return 0
        else:
            return self.first / self.second

cal1 = MoreFourCal(5,2)
cal2 = MoreFourCal(8,15)

# print(cal1.add())
# print(cal2.add())
# print(cal1.pow())
# print(cal2.pow())

print(cal1.div())
