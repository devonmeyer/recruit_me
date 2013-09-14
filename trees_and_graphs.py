from collections import deque
import math

"""

Since we're dealing with trees and graphs here, I'm going to use typical Python data structures.

For reference:

	Python list (arr = []) is equivalent to a Stack if you're only using append and pop
		arr.append(val) == Stack.push(val)
		arr.pop() == Stack.pop()

	Python deque (q = deque([a, b, c])) is equivalent to a Queue if you're only using append and popleft
		q.append(val) == Queue.enqueue(val)
		q.popleft() == Queue.dequeue()



First thing first: let's implement a plain ol' binary tree, along with the standard traversal algorithms.

Also, I'll add Breadth First Search and Depth First Search methods here.

"""

class Tree:
	def __init__(self, val):
		self.left_child = None
		self.right_child = None
		self.value = val

	def in_order_traverse(self):
		if self.left_child is None and self.right_child is None:
			print self.value
		else:
			if self.left_child is not None:
				self.left_child.in_order_traverse()
			print self.value
			if self.right_child is not None:
				self.right_child.in_order_traverse()

	def pre_order_traverse(self):
		if self.left_child is None and self.right_child is None:
			print self.value
		else:
			print self.value
			if self.left_child is not None:
				self.left_child.pre_order_traverse()
			if self.right_child is not None:
				self.right_child.pre_order_traverse()

	def post_order_traverse(self):
		if self.left_child is None and self.right_child is None:
			print self.value
		else:
			if self.left_child is not None:
				self.left_child.post_order_traverse()
			if self.right_child is not None:
				self.right_child.post_order_traverse()
			print self.value

	def breadth_first_search(self, val):
		"""
			Here, we want to use a queue, because we search the closest nodes before moving
			on to the next level of nodes.

			If we find a node with the desired value, we return the node. Otherwise, return False
		"""
		bfs_queue = dequeue()
		bfs_queue.append(self)
		while len(bfs_queue):
			n = bfs_queue.popleft()
			if n.value == val:
				return n
			if n.left_child is not None:
				bfs_queue.append(n.left_child)
			if n.right_child is not None:
				bfs_queue.append(n.right_child)
		return False

	def depth_first_search(self, val):
		"""
			In this case, we'd like to use a stack. This is because we examine the deepest
			levels of a tree first, and then work our way back up.
		"""
		dfs_stack = []
		dfs_stack.append(self)
		while len(dfs_stack):
			n = dfs_stack.pop()
			if n.value == val:
				return n
			if n.left_child is not None:
				dfs_stack.append(n.left_child)
			if n.right_child is not None:
				dfs_stack.append(n.right_child)
		return False

"""

Now, let's look at insert and find methods for a Binary Search Tree.

TODO Deletion and Balancing methods
-> Deletion is not terribly hard, but requires a bit of thinking.
-> Balancing is a bit more interesting, and would best be implemented with a Red-Black BST or something similar.

"""
class BinarySearchTree(Tree):
	def __init__(self, val):
		Tree.__init__(self, val)

	def push(self, val):
		prev = None
		n = self
		while n is not None:
			if val > n.value:
				prev = n
				n = n.right_child
			else:
				prev = n
				n = n.left_child
		if val > prev.value:
			prev.right_child = Tree(val)
		else:
			prev.left_child = Tree(val)

	def find(self, val):
		n = self.head
		while n.value != val:
			if val > n.value:
				if n.right_child is None:
					return False
				n = n.right_child
			else:
				if n.left_child is None:
					return False
				n = n.left_child
		return n

"""

And even though the chapter doesn't specifically ask for one, let's implement a simple graph as well!

"""

class Graph:
	def __init__(self, val):
		self.nodes = set([val])
		self.edges = {val: []}

	def add_node(self, val):
		self.nodes.add(val)
		self.edges[val] = []

	def add_edge(self, val_one, val_two):
		if val_one in self.nodes and val_two in self.nodes:
			self.edges[val_one].append(val_two)


"""

Now to the questions!

Q 4.1

Here we'd like to use a modified DFS. Instead of finding a value, we
look for leaf nodes, and keep track of their distance from the root in
a list.

Keep in mind that len(leaf_levels) must always be < 3, so searching in this
list would still remain O(1)

"""

def four_point_one(tree):
	dfs_stack = []
	dfs_stack.append([0, tree])
	leaf_levels = []
	while len(dfs_stack):
		level, n = dfs_stack.pop()
		if n.left_child is None and n.right_child is None:
			if any(math.fabs(e-level) > 1 for e in leaf_levels):
				return False
			else:
				if level not in leaf_levels:
					leaf_levels.append(level) 
		if n.left_child is not None:
			dfs_stack.append([level+1, n.left_child])
		if n.right_child is not None:
			dfs_stack.append([level+1, n.right_child])
	return True

"""

Q 4.2

This is a very common algorithm - it simply uses Breadth-First Search.

But in order to avoid recirculating cyclic graphs, you need to keep a set of previously-explored Nodes.

"""

def four_point_two(graph, val_one, val_two):
	explored_nodes = set()
	bfs_queue = deque([val_one])
	while len(bfs_queue):
		n = bfs_queue.popleft()
		if n == val_two:
			return True
		for c in graph.edges[n]:
			if c not in explored_nodes:
				explored_nodes.add(c)
				bfs_queue.append(c)
	return False


"""

Q 4.3

First thing to notice: The problem doesn't ask you to create a BST. Only a Binary Tree.
This has a super simple solution which makes use of a queue to keep track of which 
node to fill to keep minimal height, and is provided below in four_point_three_a.

"""

def four_point_three_a(arr):
	nodes_to_fill = deque()
	n = Tree(arr[0])
	head = n
	for item in arr[1:]:
		if n.left_child is None:
			n.left_child = Tree(item)
			nodes_to_fill.append(n.left_child)
		elif n.right_child is None:
			n.right_child = Tree(item)
			nodes_to_fill.append(n.right_child)
			n = nodes_to_fill.popleft()
	return head

"""

Let's make this question a bit more interesting, and assume we want to make a BST.

Well, we know that around the halfway point of the array we'll find the median value.
And then the median of the left subtree of the BST would be the halfway point of the
sub-array on the left of the median, and the same goes for the right subtree.

So, let's use a recursive solution to create this tree! Solution is provided in four_point_three_b.

"""

def four_point_three_b(arr):
	if len(arr) == 1:
		return Tree(arr[0])
	else:
		n = Tree(arr[len(arr)/2])
		n.left_child = four_point_three_b(arr[:len(arr)/2])
		if len(arr) > 2:
			n.right_child = four_point_three_b(arr[(len(arr)/2)+1:])
		return n


"""

Q 4.4

Let's just keep a map of depths to a list of nodes at that depth.

Then, we simply use a BFS or DFS approach (identical results), and append each depth-list with the current node.

Obviously, we have to keep track of each node's depth in each call.

Here, I use a DFS approach because Python doesn't like when you try to append a list to a deque.

This has an easy work-around - simply pop two items at a time:
	the first will be the node
	the second will be the depth of the node

"""

def four_point_four(tree):
	dfs_stack = []
	dfs_stack.append([0, tree])
	depths = {}
	depths_found = set()
	while len(dfs_stack):
		depth, n = dfs_stack.pop()
		if depth in depths_found:
			depths[depth].append(n)
		else:
			depths[depth] = [n]
			depths_found.add(depth)
		if n.left_child is not None:
			dfs_stack.append([depth+1, n.left_child])
		if n.right_child is not None:
			dfs_stack.append([depth+1, n.right_child])
	return depths


"""

Q 4.5

The 'next' node in a BST will come in one of two cases:

1. The node has a right_child:
	The next node is the left most node of the node's right subtree

2. The node has no right_child, and is its parent's left_child:
	The next node is the parent node

3. The node has no right_child, and is its parent's right_child:
	The next node is the parent of the first parent of the node which is a left_child

Sound complicated? Don't worry! Just divide the problem up, and conquer each part individually.

"""

class NodeWithParent:
	def __init__(self, val, par=None):
		self.value = val
		self.left_child = None
		self.right_child = None
		self.parent = par

def four_point_five(node):
	if node.right_child is not None:
		#case 1
		n = node.right_child
		while n.left_child is not None:
			n = n.left_child
		return n
	if node.right_child is None and node is node.parent.left_child:
		#case 2
		return node.parent
	if node.right_child is None and node is node.parent.right_child:
		n = node.parent
		while n is n.parent.right_child and n is not None:
			n = n.parent
		return n


"""

Q 4.6

I actually had this question in an interview with Pocket Gems. In my solution, I implemented
a DFS, and then essentially kept a dict mapping nodes to their parents.

Doing this without another data structure, and no reference to a parent from a particular
node makes this problem a tad more difficult.

If you find both nodes A and B from a DFS starting at node C, then C is a common ancestor of A and B.

So really, you just have to keep track of what node you found both A and B from first!

As for efficiency, this algorithm is O(N*log(N))
--> There are log(N) levels in a balanced Binary Tree
--> For each level, the algorithm performs two DFS
--> Each DFS is, itself, O(N)
--> Therefore, we're using N*log(N) operations, which is not terrible.

"""

def four_point_six(tree, a, b):
	n = tree
	prev = None
	while prev is not n:
		prev = n
		found = False
		if n.left_child is not None:
			if n.left_child.depth_first_search(a) and n.left_child.depth_first_search(b):
				n = n.left_child
				found = True
		if n.right_child is not None and not found:
			if n.right_child.depth_first_search(a) and n.right_child.depth_first_search(b):
				n = n.right_child
	return n.value

"""

Q 4.7

First observation:
If T1 has A nodes, it has log(A) levels if it is balanced, or A levels if not.
If T2 has B nodes, it has log(B) levels if it is balanced, or B levels if not.

So, let's assume they're both balanced, but if that cannot be an assumption, simply replace all references
to log(A) or log(B) with A or B.

If B is a subtree of A, you'd find its head at most (log(A) - log(B)) levels from the root.

So the solution here, to maximize performance, is to do a DFS or BFS
on the root, ensuring that if you pass level (log(A) - log(B)), you haven't found it, and can return.

"""

def four_point_seven(a, b):
	dfs_stack = []
	dfs_stack.append([0, a])
	max_depth = math.log(a.size, 2) - math.log(b.size, 2)
	while len(dfs_stack):
		depth, n = dfs_stack.pop()
		if n.value == b.value:
			if n.in_order_traverse() == b.in_order_traverse():
				return True
		if depth < max_depth:
			if n.left_child is not None:
				dfs_stack.append([depth+1, n.left_child])
			if n.right_child is not None:
				dfs_stack.append([depth+1, n.right_child])
	return False


"""

Q 4.8

This is similar to the common-ancestor problem.

If a path is allowed to include backwards-edges, then this becomes a pretty standard dynamic
programming problem.

However, let's assume that you can only move down. In that case, you want to keep a stack of nodes
and work your way down the graph. Each time you move further down, you add your current node to
the stack, and then find which child contains the desired element.

Once you reach the desired element, you pop each element, add it to the current sum (starting at 0),
and print that.

"""

def four_point_eight(tree, val):
	path = []
	n = tree
	found = False
	while not found:
		path.append(n)
		if n.value == val:
			found = True
		else:
			found = False
			if n.left_child is not None:
				if n.left_child.depth_first_search(val):
					n = n.left_child
					found = True
			if n.right_child is not None and not found:
				if n.right_child.depth_first_search(val):
					n = n.right_child
					found = False
			else:
				found = False
	if path[len(path)-1].value != val:
		print "No such value"

	n = path.pop().value
	p = p = str(n)
	s = n
	print p," => ", s
	while len(path):
		n = path.pop().value
		p = ",".join([p, str(n)])
		s += n
		print p," => ", s


