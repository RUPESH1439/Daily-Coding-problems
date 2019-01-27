def join(arr):
    ans = "/"
    for elem in arr:
        ans+=elem+"/"
    return ans
def function(arr):
    arr = arr.split('/')
    newArr = []
    for x in arr:
        if x != "." and x != '':
            newArr.append(x)
    ans = []
    for elem in newArr:
        try:
            if elem == "..":
                ans.pop()
            else:
                ans.append(elem)
        except:
            continue
    
    return join(ans)
print(function("/usr/bin/../bin/./scripts/../"))