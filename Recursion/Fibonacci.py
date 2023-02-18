# This program runs until n=38
def making_fibonacci_series(n):
    if n<=1:
        return  n
    return (making_fibonacci_series(n-1)+making_fibonacci_series(n-2))

n=int(input('Enter a number '))
fibonacci_list=[]
for i in range(n):
    fibonacci_list.append(making_fibonacci_series(i))
print(*fibonacci_list)

