def selectionSort(nums):
    n=len(nums)
    for i in range(0,n):
        minpos=i
        for j in range(i,n):
            if nums[j]<nums[minpos]:
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp

nums=[3,1,2,5,4]
selectionSort(nums)
print(nums)