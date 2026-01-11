def partition(arr, left, right):
    pivot = right
    i = left - 1

    for j in range(left, right):
        if arr[j] <= arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
    return i + 1     

def quicksort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot-1)
        quicksort(arr, pivot+1, right)

   
   
def badquicksort(arr):
    if len(arr) >= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        biggers = [x for x in arr[1:] if x > pivot]
        return(badquicksort(smaller) + [pivot] + badquicksort(biggers))




arr = [3, 6, 78, 3, 7, 9, 10, 34, 21, 4, 1, 0,]
quicksort(arr, 0, len(arr)-1)
print(arr)


