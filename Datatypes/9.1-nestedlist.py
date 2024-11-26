lst=[[[10,20,30],[40,50,60],[70,80,90]] , [[1,2,3],[4,5,6],[7,8,9]]]
for matrix in lst:
    for row in matrix:
       print(row)
    print("-----------")
lst1=[100,"rossum",[16,18,17],[78,72,76],"jntu"]
lst1[2][-1]
lst1[2].sort()
print(lst1[2][-1],lst1[2])
lst1=[100,"rossum",[16,18,17],[78,72,76],"jntu"]
lst1[2].append(19)
print(lst1)
lst1[2].insert(1,15)
print(lst1)
del lst1[2][1:3]
print(lst1)
lst1[2].sort()
print(lst1)