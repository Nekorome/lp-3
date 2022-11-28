#fibo without recurssion

a=int(input("Enter 1st number-"))
b=int(input("Enter 2nd number-"))
n=int(input("Enter n terms-"))
print(a)
print(b)
while(n-2):
    c=a+b
    a=b
    b=c
    print(c)
    n=n-2


#USING RECURSSION
def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
n=int(input("Enter n terms-"))
for i in range(n):
    print(fibo(i))
