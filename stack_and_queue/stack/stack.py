class Stack:
    def __init__(self, size):
        self.nums = []
        self.size = size
    
    def isfull(self):
        return len(self.nums) == self.size
    
    def isempty(self):
        return len(self.nums) == 0
    
    def push(self, data):
        if not self.isfull():
            self.nums.append(data)
            return f'{data} pushed'
        return 'Stack full'
    
    def pop(self):
        if not self.isempty():
            data = self.nums.pop()
            return f'{data} popped'
        return 'Stack empty'
    
    def top(self):
        if not self.isempty():
            return f'{self.nums[-1]} is the top element'
        return 'Stack empty'
    
    def current_size(self):
        return f'Size of stack: {len(self.nums)}'
    
    def clear(self):
        self.nums = []
        return 'Stack cleared'

    def display(self):
    	if(not(self.isempty())):
    		return self.nums
    	return 'Stack empty'
    	
# Main execution
size = int(input("Enter the size of the stack: "))
obj = Stack(size)

while True:
    print("1. Push\n2. Pop\n3. Top\n4. Size\n5. display \n6.clear")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        data = int(input("Enter data: "))
        print(obj.push(data))
    elif choice == 2:
        print(obj.pop())
    elif choice == 3:
        print(obj.top())
    elif choice == 4:
        print(obj.current_size())
    elif choice == 5:
        print(obj.display())
    elif choice ==6:
    	print(obj.clear())
    else:
        print("Invalid Input")

