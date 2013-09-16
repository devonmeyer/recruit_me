from collections import deque

"""

Q 8.1

This is much easier to do iteratively, but I'll do it both ways here.

"""

def eight_point_one_iterative(n):
	one = 0
	two = 1
	if n == 0:
		return one
	if n == 1:
		return two
	for i in range(n-1):
		x = one + two
		one = two
		two = x
	return x

def eight_point_one_recursive(n):
	if n == 1:
		return 1
	if n == 0:
		return 0
	return eight_point_one_recursive(n-1) + eight_point_one_recursive(n-2)

"""

Q 8.2

For a given nxm rectangle (for a square, just input 4,4; 3,3; etc.) eight_point_two_a returns
the number of possible paths from the top left corner to the bottom right.

For a given nxm rectangle, eight_point_two_b returns all of the possible paths
from top-left to bottom-right. I've commented out a call that could be implemented
for a grid that essentially returns True or False depending on whether or not there's 
an obstacle.

And after implementing it, I see that you can calculate the number of possible
paths numerically, which would seem obvious, but I couldn't figure it out before.

Essentially you have to go right (n-1) times and down (n-1) times. So the number
of possible paths you can take is the number of permutations of (n-1) "Down"s and
(n-1) "Right"s.

"""

def eight_point_two_a(n, m):
	if (n == 2 and m == 1) or (n == 1 and m == 2):
		return 1
	a = 0
	b = 0
	if n > 1:
		a = eight_point_two_a(n-1, m)
	if m > 1:
		b = eight_point_two_a(n, m-1)
	return a + b

def eight_point_two_b(n,m):
	if n == 2 and m == 1:
		q = deque()
		q.appendleft("Right")
		return [q]
	if n == 1 and m == 2:
		q = deque()
		q.appendleft("Down")
		return [q]
	paths = []
	#if not has_obstacle(n-1, m):
	if n > 1:
		for a in eight_point_two_b(n-1, m):
			a.appendleft("Right")
			paths.append(a)
	#if not has_obstacle(n, m-1):
	if m > 1:
		for b in eight_point_two_b(n, m-1):
			b.appendleft("Down")
			paths.append(b)
	return paths




"""

Q 8.3

I kinda brute forced this -- should have thought it up a bit more.

So basically a set of, say, 3 elements (A, B, C) consists of sets:

(A), (B), (C), (A, B), (A, C), (B, C), (A, B, C)

Therefore, take an element out, append it to the set of sets, then get
all of the unique subsets for the remaining set, then add these to
the set of sets, then add the union of the current element and each
unique set to the set of sets, and then return the set. :)

"""

def eight_point_three(s):
	if len(s) == 2:
		a = s.pop()
		b = s.pop()
		return [set([a]), set([b]), set([a,b])]
	i = s.pop()
	sets = eight_point_three(s)
	ret_sets = [set([i])]
	for j in sets:
		ret_sets.append(j)
	for j in sets:
		ret_sets.append(j.union(set([i])))
	return ret_sets

"""

Q 8.4

I can't count the number of times I've done this...

"""

def eight_point_four(s):
	if len(s) == 2:
		return [s, s[::-1]]
	s = list(s)
	strings = []
	for i, char in enumerate(s):
		if i == len(s)-1:
			remainder = "".join(s[:i])
			options = eight_point_four(remainder)
		else:
			bef = "".join(s[:i])
			aft = "".join(s[i+1:])
			remainder = "".join([bef, aft])
			options = eight_point_four(remainder)
		for option in options:
			strings.append("".join([char, option]))
	return strings


"""

Q 8.5

This one is closer to the set-of-sets question.

Take n = 1:
	()
take n = 2:
	()(), (())
take n = 3:
	()(), (()()), ()(()), (())()

"""


def eight_point_five(n):
	if n == 2:
		return ["()()","(())"]
	rets = []
	for option in eight_point_five(n-1):
		a = "".join(["()", option])
		b = "".join([option, "()"])
		c = "".join(["(", option, ")"])
		if a not in rets:
			rets.append(a)
		if b not in rets:
			rets.append(b)
		if c not in rets:
			rets.append(c)
	return rets


"""

Q 8.6

This is really just a recursive version of the A* search algorithm.

I've implemented this for a class before, so I'm going to move beyond, and come back to this one...

TODO Implement this

"""

"""

Q 8.7

Another pretty simple one! Admittedly it took a little trial and error to get the actual solution, but
you just have to think through the problem in terms of real values before you start coding.

"""

def eight_point_seven(n):
	if n < 5:
		return 1

	a = 0
	b = 0
	c = 0

	if n >= 25:
		a = eight_point_seven(n-25)
	if n >= 10:
		b = eight_point_seven(n-10)
	if n >= 5:
		c = eight_point_seven(n-5)
	d = 1

	return a+b+c+d


"""

Q 8.8

I'm pulling the lazy card on these damn multi-dimensional array questions.

Perhaps I should implement them in Java or something since it'd actually be a tad easier.

TODO : Implement......... and clean your room.

"""







