def insertion_sort(data):
    l=len(data)
    for i in range(1,l):
        key=data[i]
        j=i-1
        while j>=0 and key<data[j]:
            data[j+1]=data[j]
            j=j-1
        data[j+1]=key
    return data

data=list(map(int, input('Enter the numbers that will be sorted\n').strip().split()))
print('The arrays are before sorting => ',data)
data=insertion_sort(data)
print('The arrays are after sorting  => ',data)

