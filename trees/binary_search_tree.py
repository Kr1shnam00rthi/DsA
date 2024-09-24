class node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		
class binarySearchtree:
	def insert(self,node,data):
		pass
	
	def delete(self):
		pass
		
	def preorder(self,node):
		if not node:
			return
		print(node.data,end=" ")
		self.preorder(node.left)
		self.preorder(node.right)
		
	def inorder(self,node):
		if not node:
			return 
		self.inorder(node.left)	
		print(node.data,end=" ")
		self.inorder(node.right)
	
	def postorder(self,node):
		if not node:
			return
		self.postorder(node.left)
		self.postoder(node.right)
		print(node.data,end=" ")
		
	def levelorder(self,node):
		queue=[]
		queue.append(node)
		while True:
			l=len(queue)
			for i in range(l):
				element=queue.pop(0)
				print(element.data,end=" ") 
				if element.left:
					queue.append(element.left)
				if element.right:
					queue.append(element.right)
			print("")
	
	def iterative_preorder(self,node):
		
		stack=[node]
		while len(stack)!=0:
			n=stack.pop()
			print(n.data)
			if n.right:
				stack.append(right)
			if n.left:
				stack.append(left)
		 
		
	def iterative_inorder(self,node):
		
		stack=[]
		while True:
			if node:
				stack.append(node)
				node=node.left
			else:
				if len(stack)==0:
					break
				node=stack.pop()
				print(node.val)
				node=node.right
						
	def iterative_postorder(self,node):
		
		stack1=[node]
		stack2=[]
		while len(stack1)!=0:
			n=stack1.pop()
			stack2.append(n)
			if n.left:
				stack1.append(n.left)
			if n.right:
				stack1.append(n.right)
		stack2.reverse()
		for x in stack2:
			print(x.val)
		
	
	
		
