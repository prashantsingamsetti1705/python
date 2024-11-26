lst=[10,"rossum",3.46,True,2+3j,]
print(lst,type(lst))
lst[0] #+ve indexing in lst
lst[-1]#-ve indexing in lst
print(lst[0],lst[-1])
lst[0:6:2]#slicing in lst
print(lst[0:6:2])
s="mississippi" #---> string converting into list
lst=list(s)
print(lst)
lst=[range(10,21,2)] #---->range converting into list
lst=list(range(10,21,2))
print(lst)
lst=[10,"rossum",3.46,True,2+3j]# 1-->append in list it will aad at the end
lst.append(34.46)
print(lst)
lst=[10,"rossum",3.46,True,2+3j]
lst.insert(0,34.46)#2-->insert in list it contain +ve,-ve indexing to place it 
print(lst)
lst.insert(100,2+4J) 
print(lst)
lst=[10,"rossum",3.46,True,2+3j]# 3-->remove in list we can remove wath we want 
lst.remove("rossum")
print(lst)
#lst.remove(200)# we will get the value error:
#print(lst)
#lst=[]
#lst.remove(4)
#print(lst)
lst=[10,"rossum",3.46,True,2+3j]# 4-->lst in pop(index)
lst.pop(0)
print(lst)
lst=[10,"rossum",3.46,True,2+3j]# 5-->lst in pop()it will remove in last element
lst.pop()
print(lst)
lst=[10,"rossum",3.46,True,2+3j] #6-->lst in clear() it clear all list in element
lst.clear()
print(lst)
lst=[10,"rossum",3.46,True,2+3j]#del operartor
del lst[2] 
del lst[-2]
del lst [0:6:2]
print(lst)
lst1=[10,20,30,40,50,60]# 7--->lst in index
for x in enumerate(lst1):
    print(x)
for index,value in enumerate(lst1):
    print("{}---->{}".format(index,value))
lst=[10,20,30,40,50,60,10,10]#8-->count in list
lst=lst.count(10)
print(lst)
lst1=[10,20,30,40,50,60]# 9-->shalow copy in list here id is different
lst2=lst1.copy()
print(lst2,id(lst2))
print(lst1,id(lst1))
lst1=[10,20,30,40,50,60]
lst2=lst1#deep copy in list here id is same
print(lst2,lst1,id(lst1),id(lst2))
lst1=[10,60,30,23,50,65,5]#10-->sort in list
lst1.sort()
print(lst1)
lst1.sort(reverse=True)
print(lst1)
lst1.sort(reverse=False)
print(lst1)
lst2=[10,20,30,40,50,60]#11-->reverse in list
lst1=lst2.reverse()
print(lst1)#-- you will get none
lst1=lst2[::-1]
print(lst1,id(lst1),lst2,id(lst2))#id is different here lst1 and lst2
lst1=[10,20,30,40,50,60]# 12-->extend in list
lst2=[10,20,30,40,50,60]
lst3=[10,20,30,40,50,60]
lst1=lst1+lst2+lst3
print(lst1)