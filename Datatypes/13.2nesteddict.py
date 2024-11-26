d1={"s.no":100,"sname":"rs","intmarks":{"cp":17,"c++":16,"vlisi":18},"extmarks":{"cp":77,"c++":76,"vlisi":78},"cname":"jntuk"}
for k,x in d1.items():
    print(k,"--->",x,"--->",type(k),type(x),type(d1))
d1={"s.no":100,"sname":"rs","intmarks":{"cp":17,"c++":16,"vlisi":18},"extmarks":{"cp":77,"c++":76,"vlisi":78},"cname":"jntuk"}
d1["intmarks"]
print(d1["intmarks"])
d1={"s.no":100,"sname":"rs","intmarks":{"cp":17,"c++":16,"vlisi":18},"extmarks":{"cp":77,"c++":76,"vlisi":78},"cname":"jntuk"}
d1["intmarks"]["dmbs"]=19
print(d1)
d1["extmarks"]["dmbs"]=78
print(d1)
d1["intmarks"].pop("cp")
print(d1)
d1["extmarks"].pop("cp")
print(d1)
for k in d1.keys():
    print(k)
for x in d1.values():
    print(x)
d2=d1["intmarks"]
print(d2,"--->",type(d2))
d2=d1["intmarks"]["bonus"]={"cp":1,"cb":2}
print(d1)
#set in dict
d3={"s.no":100,"sname":"rs","intmarks":{"cp":17,"c++":16,"vlisi":18},"extmarks":{"cp":77,"c++":76,"vlisi":78},"cname":"jntuk"}
d2=d3.pop("intmarks")
print(d3)
d3={"s.no":100,"sname":"rs","intmarks":{"cp":17,"c++":16,"vlisi":18},"extmarks":{"cp":77,"c++":76,"vlisi":78},"cname":"jntuk"}
d3.pop("extmarks")
print(d3)
d3={"s.no":100,"sname":"rs","intmarks":(17,16,18),"extmarks":(77,76,78),"cname":"jntuk"}
d3["intmarks"]
print(d3["intmarks"])
d3["extmarks"]
print(d3["extmarks"])
d1={"s.no":100,"sname":"rs","intmarks":[17,16,18],"extmarks":[77,76,78],"cname":"jntuk"}
d1["intmarks"].insert(1,15)
print(d1)
d1["extmarks"].insert(-1,15)
print(d1)
d1["extmarks"].sort()
print(d1)

d1["extmarks"].sort(reverse=True)
print(d1)
d1["extmarks"].insert(-1,[1.2,2.3])
print(d1)



