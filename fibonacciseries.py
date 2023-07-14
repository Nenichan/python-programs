n=int(input("enter n value:"))
f1=0
f2=1
print(f1,end=" ")
print(f2,end=" ")
i=1
while(i<=n): #while((f1+f2)<=n):
  f3=f2+f1
  print(f3,end=" ")
  f1=f2
  f2=f3
  i=i+1