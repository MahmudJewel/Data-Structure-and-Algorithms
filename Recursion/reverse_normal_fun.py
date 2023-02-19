def reverse(st):
    result=''
    ln=len(st)
    for i in range(ln-1,-1,-1):
        result=result+st[i]
    return result

print(reverse('ok123'))

