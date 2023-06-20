s=0
def sum(n):
    global s
    if(n==0):
            return 0
    else:

        a=n%10
        s+=a
        n=n//10
        sum(n)
        return s
r=sum(123)
print(r)    