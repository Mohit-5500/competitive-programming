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
    return -1
arr=[2,3,5,9,14,16,18]
target=14
result=binarysearch(arr,target)
if(result==-1):
    print("No is not present")
else:
    print(f"No is present at index no {result}")