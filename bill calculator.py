print("what is the unit: ")
u= input()
u=int(u)

print ("your unit is is " + str(u) + "Kilowatt")

a= 75*3.8
b= (200-75)*5.14
c= (300-200)*5.36
d= (400-300)*5.63
e= (600-400)*8.70

if u<51: #lifeline slab
    s=u*3.33
elif u<76:
    s=u*3.8
elif u<201:
    s= a + (u-75)*5.14
elif u<301:
    s= a + b + (u-200)*5.36
elif u<401:
    s= a+ b+ c + (u-300)*5.63
elif u< 601:
    s= a + b + c + d + (u-400)*8.70
else:
    s= a+ b + c + d + e + (u-600)*9.98

if s<100: #minimum bill is 100tk
    s= 100

net = s+55 #55 additional charge

total= net*1.05 #vat 5%

print("your bill is: taka " + str(total))
    
