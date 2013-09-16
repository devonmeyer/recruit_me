"""

MATH PROBLEMS!!!

"""


"""

Q 10.1

If p is the probability of making a particular shot...

p(winning game 1) 	= p

p(winning game 2) 	= p * p + (p * (1-p) * p) + ((1-p) * p * p)
					= 3 p^2 - 2 p^3

So, solve for when 3 p^2 - 2 p^3 < p to figure out what p values we ought to play Game 1:

			3p + 2p^2 < 1
			2p^2 - 3p + 1 > 0
			(2p -1)(p - 1) > 0
			p > 1 or 2p > 1 == p > .5 we should play game 1

"""

"""

Q 10.2

Essentially, both ants at vertices joined by an edge would have to pick the same edge, of their two choices.

In fact, let's make this even more specific: the only way that there are NO collisions is if 
every ant chooses the same side (either right, or left).

Therefore, for our Triangle, it'd be

P(collision) 	= 1 - (P(all left) + P(all right))
				= 1 - (.5^3 + .5^3)
				= 1 - 2(.5^3)
				= .75

For an n-vertex polygon, it would seem we have an expandable case:

P(collision) 	= 1 - (P(all left) + P(all right))
				= 1 - (.5^n + .5^n)
				= 1 - 2(.5^n)
				= 1 - 2^(1-n)

"""

"""

Q 10.3

If the lines come in the form of y = mx+b -- assuming infinite lines and an infinite plane,
we know that they will absolutely intersect if they are not parallel OR share a y-intercept.

If the lines come in the form of two points on each line -- still assuming infinite lines and an infinite plane,
we use their two (x,y) points to calculate their y=mx+b and determine if they are parallel OR share a y-intercept.

"""

"""

Q 10.4

Ah, hardware design.

"""

def ten_point_four_mult(a, b):
	#want to return a * b
	mult = a
	i = 1
	while i < b:
		a = a + mult
		i = i + 1
	return a

def ten_point_four_sub(a, b):
	#want to return a - b
	return a + (-b)

def ten_point_four_div(a, b):
	#want to return a / b
	q = 0
	while a >= b:
		a = a + (-b)
		q = q + 1
	return q


"""

Q 10.5

I definitely struggled to figure out the trick to this particular question.

But the trick is to remember that a line that goes through the center of a square must, by
definition, cut it in half. So really, just figure out the center of each square and
create a line between the two...

"""

class Square:
	def __init__(self, bottom, left, width):
		self.bottom = bottom
		self.left = left
		self.width = width
		self.right = self.left + width
		self.top = self.bottom + width
		self.center_x = (self.left + (width/2))
		self.center_y = (self.bottom + (width/2))


def ten_point_five(square_a, square_b):
	x_a, y_a = square_a.center_x, square_a.center_y
	x_b, y_b = square_b.center_x, square_b.center_y


	#handle vertical line case:
	if x_b == x_a:
		print "x = ",x_b
	else:
		# slope = change in y over change in x
		m = (y_b - y_a) / (x_b - x_a)
		# y-intercept => m*x_a + b = y_a => b = y_a - (m*x_a)

		b = y_a - (m*x_a)

		print "y = (",m," * x ) + ",b


"""

Q 10.6

TODO Return to this -- it seems like you will have to iterate through each pair of points,
draw a line through them, and then determine which line ticks the most additional points.

"""


"""

Q 10.7

A number where the only prime factors are 3, 5, and 7 would look like this:

(3^a) * (5^b) * (7^c)

So we need to be smart about figuring out when to increment a, b, or c.

For instance
# 0 			3^0 * 5^0 * 7^0			= 1
# 1 			3^1 * 5^0 * 7^0			= 3
# 2 			3^0 * 5^1 * 7^0			= 5
# 3				3^0 * 5^0 * 7^1			= 7
# 4		???		3^1 * 5^1 * 7^0			= 15
				3^2 * 5^0 * 7^0			= 9 <== this is #4

This already appears to be a dynamic programming problem, because the 
answer to n < x lend themselves to the answer for n == x.

Now, it appears that 

Let's do some pseudo-code.

n = the 'th element
val[0] = [0, 0, 0, 0] 	=> elements in the array are as follows
						=> [a, b, c, num]

for i <= n:
	min_val = val[i-1][3] * 7
	min_j = -1
	to_add = -1
	must_be_gt = val[i-1][3]
	for j = 0 to i:
		option = val[j]
		opt_one = 3*option[3]
		opt_two = 5*option[3]
		opt_three = 7*option[3]
		if opt_one > must_be_gt and opt_one < min_val:
			min_val = opt_one
			min_j = j
			to_add = 0
		elif opt_two > must_be_gt and opt_two < min_val:
			min_val = opt_two
			min_j = j
			to_add = 1
		elif opt_three > must_be_gt and opt_three < min_val:
			min_val = opt_three
			min_j = j
			to_add = 2

There is DEFINITELY a better solution. But for now, the brute-force method shall do.

TODO : Implement a nice, good-looking, much more efficient algorithm.

"""

def ten_point_seven(n):
	val = [[0,0,0,1]]
	for i in range(1, n+1):
		min_val = val[i-1][3] * 7
		min_j = -1
		to_add = -1
		must_be_gt = val[i-1][3]
		for j in range(0, i):
			option = val[j]
			opt_one = 3*option[3]
			opt_two = 5*option[3]
			opt_three = 7*option[3]
			if opt_one > must_be_gt and opt_one < min_val:
				min_val = opt_one
				min_j = j
				to_add = 0
			if opt_two > must_be_gt and opt_two < min_val:
				min_val = opt_two
				min_j = j
				to_add = 1
			if opt_three > must_be_gt and opt_three < min_val:
				min_val = opt_three
				min_j = j
				to_add = 2
		final = []
		for item in val[min_j]:
			final.append(item)
		final[to_add] += 1
		final[3] = min_val
		val.append(final)
	return val[len(val)-1][3]





