n=int(input('Enter a number: '))
fibonacci_list=[]
n1,n2=0,1
fibonacci_list.append(n1)
fibonacci_list.append(n2)
for i in range(2,n):
    n3=n1+n2
    fibonacci_list.append(n3)
    n1,n2=n2,n3
print(*fibonacci_list)