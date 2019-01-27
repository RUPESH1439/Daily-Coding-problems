function_calls = 0

def func(arr):
    global function_calls
    function_calls+=1
    mid = len(arr)//2
    if (len(arr) > 2):
        left = mid -1
        right = mid+1
        if arr[left] < arr[right]:
            start = 0
            end = mid
        if arr[right] < arr[left]:
            start = right
            end = -1
        if arr[mid] < arr[left] and arr[mid] < arr[right]:
            return arr[mid]
        else:
            return func(arr[start:end])
    else:
        return min(arr)
test = [5,7,10,3,4]
print(func(test))
print("calls ",function_calls)
            