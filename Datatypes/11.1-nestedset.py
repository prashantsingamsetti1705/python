#s1={10,"rossum",{10,16,18},{77,78,76},"jntu"} #set in set not possible
#s1={10,"rossum",[10,16,18],[77,78,76],"jntu"} #list in set is not possible
#s2={10,"rossum",(10,16,18),(77,78,76),"jntu"} #tuple in set is possible
s3=[10,"rossum",{10,16,18},{77,78,76},"jntu"]
s3[2].add(19)
print(s3)
s3=(10,"rossum",{10,16,18},{77,78,76},"jntu")
s3[2].add(19)
print(s3)
