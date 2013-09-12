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

	def pop(self, val):
		if top is not None:
			t = top
			top = t.next
			return top.value
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

	def dequeue(self, val):
		if self.first is not None:
			f = self.first
			self.first = self.first.next
			return f.value
		return None
