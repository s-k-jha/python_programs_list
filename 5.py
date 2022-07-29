# Python Program to Split the array and add the first part to the end
def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]

        arr[n-1] = x


arr = [2,4,6,8,10]
n = len(arr)
position = 2
splitArr(arr, n, position)
for i in range(0, n):
    print(arr[i], end=' ')
