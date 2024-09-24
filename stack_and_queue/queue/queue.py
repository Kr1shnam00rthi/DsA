class queue:
	def __init__(self,size):
		self.elements=[]
		self.size=size
		
	def isempty(self):
		if len(self.elements)==0:
			return True
		return False
	
	def isfull(self):
		if len(self.elements)==self.size:
			return True
		return False
	
	def push(self,data):
		if not self.isfull():
			self.elements.append(data)
			return f'{data} pushed'
		return 'Queue full'
	
	def pop(self):
		if not self.isempty():
			data=self.elements[0]
			self.elements.pop(0)
			return f'{data} poped'
		return 'Queue Empty'
	
	def size(self):
		return f'Current size of queue is {len(self.elements)}'
	
	def display(self):
		if not self.isempty():
			return f'Data elements: {self.elements}'
		return 'Queue Empty'
		
size=int(input("Enter size: "))
obj=queue(size)
while True:
	print("1.Push\n 2.Pop\n 3.Size\n 4.Display\n 5.Exit")
	choice=int(input("Enter Choice: "))
	if choice==1:
		data=int(input("Enter data: "))
		print(obj.push(data))
	elif choice==2:
		print(obj.pop())
	elif choice==3:
		print(obj.size())
	elif choice==4:
		print(obj.display())
	elif choice==5:
		break
	else:
		print("Wrong input")
		
	
