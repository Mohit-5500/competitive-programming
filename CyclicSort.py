def sort(nums):
    i=0

    while(i<len(nums)):
        current = nums[i] - 1
        if(nums[i]!=nums[current]):
            swap(nums,i,current)
        else:
            i+=1
def swap(nums,first,second):
    temp=nums[first]
    nums[first]=nums[second]
    nums[second]=temp

nums=[3,4,5,1,2]
sort(nums)
print(nums)