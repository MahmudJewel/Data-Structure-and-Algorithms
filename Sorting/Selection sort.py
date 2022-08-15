def selection_sort(data):
    l=len(data)
    for i in range(l):
        min_index=i
        for j in range(i+1,l):
            if data[i]>data[j]:
                min_index=j
        data[i], data[min_index]=data[min_index], data[i]
    return data

data=list(map(int, input('Enter the numbers that will be sorted\n').strip().split()))
print('The arrays are before sorting => ',data)
data=selection_sort(data)
print('The arrays are after sorting  => ',data)
