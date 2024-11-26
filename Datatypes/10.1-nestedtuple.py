t1=(10,'rossum',(17,16,18),(77,78,66),"jntu") #tuple in tuple we can add the new tuple and indexing and sorting
print(t1)
t1[0]
t1[2][1]
t1[-2][-1]
print(t1[0],t1[2][1],t1[-2][-1])

t1=(10,'rossum',[17,16,18],[77,78,66],"jntu") #tuple in list in this we can sort  list
print(t1[2],type(t1[2]))
t1[2].sort()
print(t1)
t1=(10,'rossum',[17,16,18],[77,78,66],"jntu")
print(t1[2],type(t1[2]))
t1[3].sort(reverse=True)
print(t1)
l1=[10,'rossum',(17,16,18),(77,78,66),"jntu"]
print(l1[2],type(l1[2]))
