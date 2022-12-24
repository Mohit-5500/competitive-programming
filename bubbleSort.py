def bubbleSort(nums):
    swapped=False
    n=len(nums)
    # run the steps n-1 times
    for i in range(0,n):
        #for each step the max element will come at the last position of the array
        for j in range(1,n-1):
             #swap the element if the element is smaller than the previous element
            if nums[j]<nums[j-1]:
                temp=nums[j]
                nums[j]=nums[j-1]
                nums[j-1]=temp
                swapped=True
                # if you did not swap the particular value for the ith step it means that the array is sorted hence stop the program
        if(swapped==False):
            break


nums=[3,1,2,5,4]
bubbleSort(nums)
print(nums)
