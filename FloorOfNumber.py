#Floor of the array: Greatest number smaller or equal to target. 
def binarysearch(arr,target):
    start=0
    end=len(arr)-1
    mid=0
    while(start<=end):
        mid=(start+end)//2

        if(target>arr[mid]):
            start=mid+1
        elif (target<arr[mid]):
            end=mid-1
        else:
            return mid
    return end
arr=[2,3,5,9,14,16,18]
target=15
result=binarysearch(arr,target)
print(f"Floor number of target is {result}")
