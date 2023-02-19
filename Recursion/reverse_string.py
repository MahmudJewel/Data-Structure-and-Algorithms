#1 Created by me ==> 19feb23
# def reverse(st,ln):
#     if ln==0:
#         return 0
#     ln=ln-1
#     print(st[ln], end='')
#     return(reverse(st,ln))
# st=input('Enter a string==> ')
# print('Reverse string==> ', end='')
# reverse(st,len(st))

#2 using slice method
def rreverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]
print(rreverse('abcd'))
