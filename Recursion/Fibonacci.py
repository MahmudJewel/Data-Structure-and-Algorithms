# # This program runs until n=38
# def making_fibonacci_series(n):
#     if n<=1:
#         return  n
#     return (making_fibonacci_series(n-1)+making_fibonacci_series(n-2))

# n=int(input('Enter a number '))
# fibonacci_list=[]
# for i in range(n):
#     fibonacci_list.append(making_fibonacci_series(i))
# print(*fibonacci_list)

# Function for nth Fibonacci number

# def Fibonacci(n):
#     if n<= 0:
#         print("Incorrect input")
#     # First Fibonacci number is 0
#     elif n == 1:
#         return 0
#     # Second Fibonacci number is 1
#     elif n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)

# # Driver Program

# print(Fibonacci(40))

# =================================================================
"""
This is faster and written solely by me.
Nth fibonacci number 
"""

def get_fibonacci(iterator: int, n: int, a: int, b: int):
    # validity check
    if n < 0:
        return "Please enter a positive number"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        c = a + b
        a, b = b, c
        iterator += 1
        if iterator == n:
            return c
        else:
            return get_fibonacci(iterator, n, a, b)


n = int(input("Enter a number "))
result = get_fibonacci(2, n, 0, 1)
print("result", result)
