#아래로 쭉
for i in range(1,10):
    print()
    for j in range(2,10):
        print("{} * {} = {:2}  ".format(j,i,i*j), end='')

print()


#좌우로 쭉
for i in range(2,10):
    for j in range(1,10):
        print("{} * {} = {:2}".format(i,j,i*j))


a = [1,2,3,4,5]
result = [num*3 for num in a if num % 2 == 0]
print(result)

for num in a :
    if num%2 == 0:
        result.append(num*3)
