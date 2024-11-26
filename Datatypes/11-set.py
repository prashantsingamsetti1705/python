s1={10,20,30,40,50,10,20,30}
print(s1,type(s1))
s2={10,"rs",34.56,True,False,2+3j,"python"}
print(s2,type(s2))
#s2[0]#TypeError: 'set' object is not subscriptable

#for index,value in enumerate(s2): # indexing is not their to find it we use enumerate
    #print(index,"---->",value)

s1={10,20,30,40,50,10,20,30} #in aad in set it aad in any where in order 
print(s1,type(s1),id(s1))
s1.add("python")
print(s1,type(s1))
s2=set() #empty set to add 
s2.add("prashant")
s2.add(True)
print(s2,type(s2))
s1={10,20,30,40,50,10,20,30} #clear empty set we will get none
s1.clear()
print(s1)
s1={10,20,30,40,50,10,20,30} 
s1.remove(20)
print(s1)
s1={10,20,30,40,50,10,20,30}
s1.discard(200)
s1={10,20,30,40,50,10,20,30}#pop() it will remove in frist if all will be pop after we use set0bj.pop() we get keyerror bcoz set is empty
s1.pop()
s1.pop()
s1.pop()
print(s1)
s1={10,20,30,40,50,10,20,30}# id is the different here bocz it use shallowcopy
s2=s1.copy()
print(s2,type(s2),id(s2))
print(s1,type(s1),id(s1))
s1.add(100)
s2.add("python")
print(s2,type(s2),id(s2))
print(s1,type(s1),id(s1))

s1={10,20,30} #This fucntion returns True provided There is no Common Elements between SetObj1 and SetObj2
s2={30,40,50} #This fucntion returns False provided There is Atleast  One Common Element(s) between SetObj1 and SetObj2
s3={25,15,35}
s1.isdisjoint(s2)
print(s1.isdisjoint(s2))
s1.isdisjoint(s3)
s2.isdisjoint(s3)
print(s1.isdisjoint(s3),s2.isdisjoint(s3))

s1={10,20,30} #.issuper set This Function returns True Provided SetObj1 contains all the Elements of SetObj2 Otherwise It returns False
s2={10,20,} # or This Function returns True Provided All the Elements of SetObj2  Present in  SetObj1 Otherwise It returns False
s3={10,15,25,35,45,40}
s1.issuperset(s2)
s1.issuperset(s3)
s3.issuperset(s1)
print(s1.issuperset(s2),s1.issuperset(s3),s3.issuperset(s1))
s2.issubset(s1)
s1.issubset(s2)
print(s2.issubset(s1),s3.issubset(s2))

{10,20,30}.issuperset(set())# note important 
set().issubset({10,20,30})
set("RADAR").isdisjoint(set("ROCKET"))
set("RADAR").issubset(set("ROCKET"))
print({10,20,30}.issuperset(set()),set().issubset({10,20,30}),
set("RADAR").isdisjoint(set("ROCKET")),
set("RADAR").issubset(set("ROCKET")))

s1={10,20,30} # union (in uinon it will remove comman element and print remaing )
s2={10,20,}
s3=s1.union(s2)
print(s3)

s1={10,20,30} # intersection(in intersection it will print only comman element and  not print remaing )
s2={10,20,}
s3=s1.intersection(s2)
print(s3)

s1={10,20,30} # it will print only unique elment only
s2={10,20,}
s3=s1.difference(s2)
print(s3)
s1={10,20,30} # it will print only s2 elements remove common element in s1,s2 and retun to only s2
s2={10,20,}
s3=s2.difference(s1)
print(s3)

s1={10,20,30,40} # it will remove common elment s1,s2 elements print in s3 
s2={10,20,50,60}
s3=s2.symmetric_difference(s1)
print(s3)

s1={10,20,30,40} # you will get none
s2={10,20,50,60}
s3=s1.symmetric_difference_update(s2)
print(s3)

s1={10,20,30}#it wil print s1,s2 data in s1
s2={15,25}
s1.update(s2)
print(s1)
