l=[1,2,3,5,8]
num=int(input("Enter the number"))
for i in range(0,len(l)-1):
    if(l[i]==num):
        print("Number is at ",i," position")
        break
       
else:
    print("Not found")    
'''l=[1,2,"hello",53.7]
num=eval(input("which element you want to search"))   
for i in l:
    if(num==i):
        print("Element found at",i-1," position")
else:
    print("Not found")        '''
