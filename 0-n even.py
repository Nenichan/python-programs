n=int(input("enter n val:"))
# i=int(input("enter i val:"))
i=0
print("Even numbers: ")

while(n>=i):
    if(i%2==0):
        print(i,end=" ")
    i=i+1

i=0
print("\nOdd numbers: ")
while(n>=i):
    if(i%2==1):
        print(i,end=" ")
    i=i+1