#type conversion
a=6
b=9.7
sum=a+b
print(sum)   #automatic- type conversion (float is more superior value than integer)
a="23"
b="71"
sum=a+b
print(sum)     #concatenate the string not add
a,b=1,"8"
b=int(b)        #type casting- manually convert the type
print(type(b))
sum=a+b
print(sum)