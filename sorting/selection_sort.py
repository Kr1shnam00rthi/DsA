def get_min(num):
	j=0
	for i in range(1,len(num)):
		if num[i]<num[j]:
			j=i
	return j
 
def get_max(num):
	j=0
	for i in range(1,len(num)):
		if num[i]>num[j]:
			j=i
	return j

def selection_sort(nums):
	l=len(nums)
	for i in range(len(nums)):
		j=get_max(nums[0:l-1-i]) # sorts in ascending order use get_max to sort in descending order
		nums[l-i-1],nums[j]=nums[j],nums[l-i-1]
	return nums

nums=[6,8,2,5,2]
print(selection_sort(nums))
	
