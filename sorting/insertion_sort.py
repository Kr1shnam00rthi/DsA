def insertion_sort(nums):
	for i in range(1,len(nums)):
		j=i
		while j>0 and nums[j]<nums[j-1]: # change > to sort in descending order
			nums[j],nums[j-1]=nums[j-1],nums[j]
			j-=1
	return nums

nums=[3,4,51,2,3,4]
print(insertion_sort(nums))

