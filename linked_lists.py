"""

All of the linked list questions here are done assuming I have a *singly* linked-list

"""


"""

Class definition

DISCLAIMER : This portion is essentially given to you in the textbook, though it's pretty straightforward anyhow.

"""

class Node:
	def __init__(self, val):
		self.next = None
		self.value = val

	def append_to_tail(self, value):
		new_node = Node(value)
		n = self
		while n.next is not None:
			n = n.next
		n.next = new_node

	def __str__(self):
		n = self
		ret = str(n.value)
		while n.next is not None:
			ret = ", ".join([ret, str(n.next.value)])
			n = n.next
		return ret


def delete_node(head, data):
	n = head
	if n.value == data:
		#either just return a list without the head or None -> an empty list
		return n.next
	while n.next.value != data:
		n = n.next
		if n.next is None:
			#before you check an empty next node, just return that the element was not found
			return -1
	# if we've made it here, our n.next.value == data, so just make n.next = n.next.next
	n.next = n.next.next
	return head

"""

Now onto the questions!

Q 2.1

Iterate through, keep a set of already-found items. If a duplicate surfaces,
delete it by calling delete_node starting at the current item, so the delete_node method
only takes 1 iteration.

This keeps time-complexity at O(N)

"""

def two_point_one(head):
	n = head
	counts = {}
	items = set()
	items.add(n.value)
	while n.next != None:
		if n.next.value in items:
			n.next = delete_node(n.next, n.next.value)
		else:
			items.add(n.next.value)
			n = n.next
	return head

"""

Q 2.2

Here, we really just need the size. We'll iterate through the list to get the size, and then 
go back through but stop at the correct index.

If we're not worried about data, we could just put every element in an array, and then
return the i'th element. But that'd be too easy!


ex: head => 0 => 5 => 3 => 9 => 6 => 20 => 13 : i = 1 : return 20

"""

def two_point_two(head, i):
	n = head
	size = 0
	while n.next is not None:
		size = size+1
		n = n.next
	j = 0
	n = head
	while j < size - i:
		n = n.next
		j += 1
	return n.value

"""

Q 2.3

a->b->c->d->e ==> a->b->d->e

This one tripped me up. Admittedly, I looked for a hint in the back of the book.
I simply couldn't conceive of a way to do this... but you don't need to *get* to b from c,
You just need to have b-> the data in d, d-> e, etc.

"""

def two_point_three(c):
	n = c
	n.value = n.next.value
	while n.next.next is not None:
		n.next.value = n.next.next.value
		n = n.next
	n.next = None

"""

Q 2.4

This is simple -- add the two together, generate a carry-out, and then increment.
If you reach the end of one, treat the remainder of the other as adding with zero.

"""

def two_point_four(a, b):
	result = Node((a.value+b.value) % 10)
	carry = (a.value+b.value) // 10
	n_a = a.next
	n_b = b.next
	while n_a is not None or n_b is not None:
		if n_a is None:
			result.append_to_tail((n_b.value + carry) % 10)
			carry = (n_b.value + carry) // 10
			n_b = n_b.next
		elif n_b is None:
			result.append_to_tail((n_a.value + carry) % 10)
			carry = (n_a.value + carry) // 10
			n_a = n_a.next
		else:
			result.append_to_tail((n_a.value + n_b.value + carry) % 10)
			carry = (n_a.value + n_b.value) // 10
			n_a = n_a.next
			n_b = n_b.next
	if carry > 0:
		result.append_to_tail(carry)
	return result


"""

Q 2.5

This is also simple, but it has a trick.

Reverse the list - if you return to the starting node, then there is a cycle.

"""

def two_point_five(head):
	n = head
	next = n.next
	temp = next.next
	n.next = None
	while temp is not None:
		next.next = n
		n = next
		next = temp
		temp = next.next
	if n == head:
		return True
	return False
