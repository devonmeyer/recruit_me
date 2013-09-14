"""

Class definition

DISCLAIMER : This portion is essentially given to you in the textbook, though it's pretty straightforward anyhow.

"""

class Node:
	def __init__(self, val):
		self.next = None
		self.value = val

class Stack:
	def __init__(self, val):
		self.top = Node(val)

	def push(self, val):
		t = Node(val)
		t.next = self.top
		self.top = t

	def pop(self):
		if self.top is not None:
			t = self.top
			self.top = t.next
			return t.value
		return None

class Queue:
	def __init__(self, val):
		self.first = Node(val)
		self.last = self.first

	def enqueue(self, val):
		if self.first is not None:
			self.last.next = Node(val)
			self.last = self.last.next
		else:
			self.first = Node(val)
			self.last = self.first

	def dequeue(self):
		if self.first is not None:
			f = self.first
			self.first = self.first.next
			return f.value
		return None


"""

Q 3.1

You could use a dynamically-resizing array to store all of the nodes.

Each 'stack' is essentially an index of this array where the top element is.

The Node would have the following member variables:
	Node.value // Value of the node
	Node.next // Index of which array element corresponds to the next item on the stack

Therefore, all of the logic is the same, but the implementation is altered slightly.

Also note: you can store as many stacks as you want in an array in this manner - three is just an example.

"""

class Array_Node:
	def __init__(self, val):
		self.next = -1
		self.value = val

class Array_Stacks:
	def __init__(self, val_one, val_two, val_three):
		self.arr = [None] * 6 #use double the current necessary size
		self.stack_one = 0
		self.stack_two = 1
		self.stack_three = 2

		arr[0] = Node(val_one)
		arr[1] = Node(val_two)
		arr[2] = Node(val_three)

	def push(self, stack_num, val):
		stack = None
		if stack_num == 1:
			stack = self.stack_one
		elif stack_num == 2:
			stack = self.stack_two
		else:
			stack = self.stack_three
		if arr[stack] is None:
			arr[stack] = Node(val)
		else:
			arr.append(Node(val))
			arr[stack].next = len(arr)-1

	def pop(self, stack_num):
		stack = None
		if stack_num == 1:
			stack = self.stack_one
		elif stack_num == 2:
			stack = self.stack_two
		else:
			stack = self.stack_three
		if arr[stack] is None:
			return None
		else:
			# Could definitely do some fancy things here
			# i.e. keep track of useless array data and
			# repopulate unused array values before
			# expanding the array in .push()
			n = arr[stack]
			stack = arr[stack].next
			return n.value

"""

Q 3.2

The first inclination would be to simply add a self.min value to each stack. In the case of push, this is easy:

"""

def three_point_two_a(self, val):
	new_node = Node(val)
	#...
	if new_node.value < self.min.value:
		self.min = new_node

"""

However, in the case of pop(), you have no way of updating the min value. You need some way of accessing what the
minimum value was **before** a particular node was added. 

So, the workable answer is this:

We store the min node on the stack...
and then we also store the previous min node for each node.

This is workable because if we're popping the current min node, we know for sure that the previous min
node has to exist (because it is beneath the current min node on the stack - remember, last in=first out)

Therefore, all we have to do is follow that pointer, update the min node on the stack, and we're good.

Our addendum to push() becomes:

"""

def three_point_two_b(self, val):
	new_node = Node(val)
	# ...
	if new_node.value < self.min.value:
		new_node.prev_min = self.min
		self.min = new_node

"""

And the following is added to pop()

"""

def three_point_two_c(self, val):	
	# Notice is, not ==
	# is means 'points to the same instance'
	# == uses a class's __eq__(self, other) method to compare
	if self.top is self.min:
		self.min = self.min.prev_min

"""

Q 3.3

Pretty straightforward! However, there are two things to consider:

1. How do we store the stacks?
--> Well, because you're filling them up one after another,
what you really have is a stack OF stacks

2. How do you determine when to create a new stack?
--> Keep track of the number of items in the top stack,
When that reaches the max, create a new one, append it to the
stack of stacks, and then continue like you have been!

"""

class SetOfStacks:
	def __init__(self, val, max_size):
		self.stack_of_stacks = Stack(Stack(val))
		self.top_stack_len = 1
		self.max_size = max_size

	def push(self, val):
		if self.top_stack_len == self.max_size:
			stack_of_stacks.push(Stack(val))
		else:
			s = stack_of_stacks.pop()
			s.push(val)
			stack_of_stacks.push(s)
			self.top_stack_len += 1

	def pop(self):
		s = stack_of_stacks.pop()
		val = s.pop().value()
		self.top_stack_len -= 1
		if self.top_stack_len != 0:
			self.stack_of_stacks.push(s)
		return val


"""
Now we have an interesting problem...

How do we pop a particular stack?

Well, this is the same way that a stack would handle a find() method...
Pop each value, check it, if it's not the desired val, put it in another stack

Once you've found it or reached the end, pop each value from the new stack
and place it into the original stack.

Here we'll assume a zero-base

"""
	
def pop_at_index(self, i):
	j = 0
	rev_stack = Stack(None)
	while j < i and s.next is not None:
		s = stack_of_stacks.pop()
		rev_stack.push(s)
		j += 1
	if j == i:
		val = s.pop().value
	s = rev_stack.pop()
	while s is not None:
		stack_of_stacks.push(s)
		s = rev_stack.pop()


"""

Q 3.4

This is a toughie.

TODO Come back to this and implement a recursive solution

"""

#TODO


"""

Q 3.5

Well, a queue is simply a stack where you still add to the top, yet pull from the bottom.

In this case, what we need is one stack to hold our actual queue, and then another to act
as a sort of buffer for us to keep the values in order whenever we do a push.

This is a very inefficient data structure: pushing a new value is O(N)

But this question is more of a brain teaser, using stacks to represent the reverse order of a typical stack.

"""

class MyQueue:
	def __init__(self, val):
		self.queue = Stack(val)
		self.buffer = Stack(None)

	def push(self, val):
		n = self.queue.pop()

		while n is not None:
			self.buffer.push(n)
			n = self.queue.pop()

		self.queue.push(val)

		n = self.buffer.pop()

		while n is not None:
			self.queue.push(n)
			n = self.buffer.pop()

	def pop(self):
		return self.queue.pop()

"""

Q 3.6

There are two obvious ways to do this.

The first would be to add all of the members of the stack to a sorted data structure, such as a
Binary Search Tree, and then when the stack is empty, begin inserting nodes in ascending order.

However, this question is really asking you how to use a stack to sort a stack. In that case:
While stack not empty:
	Pop an element from stack
	while current element > top element
		stack.push(new stack.pop())
	new stack.push(current element)

"""

def three_point_six(stack):
	sorted_stack = Stack(stack.pop())
	while not stack.isEmpty():
		n = stack.pop()
		while sorted_stack.peek() is not None and n > sorted_stack.peek():
			stack.push(sorted_stack.pop())
		sorted_stack.push(n)
	return sorted_stack




