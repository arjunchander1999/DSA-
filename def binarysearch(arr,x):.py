def binarysearch(arr,x):
    low=0
    high=len(arr)-1
    while low<high:
        mid=high//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1



print(binarysearch([1,2,3,4,5,6,7],2))
    