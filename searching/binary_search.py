# for binary search array should be sorted
class binary_search:
	def __init__(self,nums):
		self.nums=nums
	
	def binary(self,element):
		l=0
		e=len(self.nums)-1
		while l<=e:
			m=(l+e)//2
			if self.nums[m]==element:
				return f'{element} found at index {m}'
			elif self.nums[m]<element:
				l=m+1
			elif self.nums[m]>element:
				e=m-1
		return f'{element} not found'

nums=[2,3,5,6,7,8,9]
element=int(input("Enter element: "))
obj=binary_search(nums)
print(obj.binary(element))
