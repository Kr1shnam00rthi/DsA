class linear_search:
	def __init__(self,nums):
		self.nums=nums
	
	def search(self,element):
		for i in range(len(self.nums)):
			if element==self.nums[i]:
				return f'{element} found at index {i}'
		return f'{element} not found'
	
nums=[2,3,4,6,1,2,4]
obj=linear_search(nums)
element=int(input("Enter search element: "))
print(obj.search(element))

