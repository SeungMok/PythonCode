import pickle

data = {1:'python',2:'you need'}

print(type(data))

#피클 저장
# with open("test.pickle",'wb')as f:
#     pickle.dump(data,f)

#피클 load
with open("test.pickle",'rb')as f:
    data = pickle.load(f)
    print(data)
    print(type(data))

