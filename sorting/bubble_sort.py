def bubble_sort(nums):
	for i in range(0,len(nums)):
		for j in range(0,len(nums)-i-1):
			if nums[j]>nums[j+1]:   # change to < for sort in descending
				nums[j],nums[j+1]=nums[j+1],nums[j]
	return nums
	
nums=[7,1,2,3,4,5,6]
print(bubble_sort(nums))
