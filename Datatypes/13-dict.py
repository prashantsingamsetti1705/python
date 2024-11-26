d1={} # empty dict
print(d1,type(d1),id(d1))
d1[100]=1.2 
print(d1)
d1[200]=2.2
print(d1)
d1["c++"]="prashant" # adding only str in dict
d1["python"]="rossum"
print(d1)
#d1={10:"apple",20:"mango",30:"kiwi",40:"sberry"} # key error
#print(d1,type(d1))
#d1[0]
#print(d1)
d1={10:"apple",20:"mango",30:"kiwi",40:"sberry"} # key error
print(d1,type(d1))
d1[20]="grapes"
print(d1)
d1={10:2.2,10:1.2,10:0.2} # same key value it will print updated vlaue only
print(d1)
d1={10:2.2,10:1.2,10:0.2}#predfine function in dict clear
d1.clear()
print(d1) #{}empty dict  clear we get key error
d1={10:2.2,20:1.2,30:0.2}
d1.pop(10)
print(d1)
d1={10:2.2,20:1.2,30:0.2} # it will remove last elment of dict bot key and value
d1.popitem()
print(d1)
d2={10:1.2,20:3.4,30:1.2,40:4.5,50:3.4}#get it gives value obtaing a key
d2[10]
print(d2[10])
d2={10:1.2,20:3.4,30:1.2,40:4.5,50:3.4} # it will give keys only 
ks=d2.keys()
print(ks)
for k in ks:
    print(k)
for k in d1.keys():
    print(k)
d2={10:1.2,20:3.4,30:1.2,40:4.5,50:3.4} # it will give keys only 
v=d2.values()
print(v)
for v in v:
    print(v)
d2={10:1.2,20:3.4,30:1.2,40:4.5,50:3.4} # it will give keys only it gives key and values
t=d2.items()
print(t)
for t,v in t:
    print(t)
    print(t,"---->",v,"--->",type(t),type(d2))




