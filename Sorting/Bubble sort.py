def bubble_sort(arr):
    l=len(arr)
    for i in range(l-1):
        for j in range(l-1):
            # Ascending order 
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
    return arr

n=list(map(int, input('Enter the numbers that will be sorted\n').strip().split()))
print('The arrays are before sorting => ',n)
n=bubble_sort(n)
print('The arrays are after sorting  => ',n)
