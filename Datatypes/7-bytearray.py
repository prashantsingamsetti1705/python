lst=(0,2,47,56,244,137,255)
ba=bytearray(lst)
print(ba)
for val in ba:
    print(val)
ba[1:3]=[150,155] # replacing the value
for val in ba:
    print(val)
lst=[10,20,30,40,255]#slicing
ba=bytearray(lst)
for val in ba[2:4]:
    print(val)
lst=[10,20,30,40,255]# reverse slicing
ba=bytearray(lst)
for val in ba[::-1]:
    print(val)
