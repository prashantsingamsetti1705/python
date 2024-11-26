t1=(10,20,30,10,20,40,50)
print(t1,type(t1))
t1[0]#indexing in tuple
print(t1[0])
t1[-1]
print(t1[-1])
t1[::-1]# slicing in tuple
print(t1[::-1])
#t1=(10,20,30,10,20,40,50)#  you will get the type error'tuple' object does not support item assignment
#t1[0]=100
#print(t1[0])
t1=()
len(t1)
print(t1,type(t1),len(t1))
s="radar"# string convert into tuple
t=tuple(s)
print(t,type(t))
lst=[10,20,45,75,"radar",2+3j]
t=tuple(lst)
print(t,type(t))
t=(10) #diffrent way to to write tuple
print(t,type(t))
t=(10,)
print(t,type(t))

t=("python")
print(t,type(t))
t=("python",)
print(t,type(t))

t1=(10,"rs",4.56) # per define function index
t1.index(10) #--->index in tuple
print(t1.index(10))
t1=(10,20,30,30,10,10,30,50,10,50,60)
t1.count(10) #--->count in tuple
print(t1.count(10))
#t1=(10,23,-56,-1,13,15,6,-2)# we will get AttributeError: 'tuple' object has no attribute 'sort'
#t1.sort()
#print(t1.sort())
t1=(10,23,-56,-1,13,15,6,-2)# to sort we will not ude to want to sort we use sorted
x=tuple(sorted(t1))
print(x)

t1=(10,23,-56,-1,13,15,6,-2)
lst=list(t1)
lst.sort(t1)
x=tuple(t1)
print(x)
t1=t1[::-1]