from collections import deque

"""

Q 20.1

"""

def twenty_point_one(a, b):
	binary_a = deque()
	binary_b = deque()
	while a > 0:
		binary_a.append(a % 2)
		a = a >> 1
	while b > 0:
		binary_b.append(b % 2)
		b = b >> 1
	#Now I have a and b in a deque in binary format
	c = 0
	s = deque()
	while len(binary_a) and len(binary_b):
		bit_a = binary_a.popleft()
		bit_b = binary_b.popleft()
		s.appendleft(str(bit_a ^ bit_b ^ c))
		c = (bit_a & bit_b) or (bit_a & c) or (bit_b & c)
	while len(binary_a):
		bit_a = binary_a.popleft()
		s.appendleft(str(bit_a ^ c))
		c = (bit_a & c)
	while len(binary_b):
		bit_b = binary_b.popleft()
		s.appendleft(str(bit_b ^ c))
		c = bit_b & c
	s.appendleft(str(c))
	print int("".join(s), 2)