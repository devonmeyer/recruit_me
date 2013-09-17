import math

"""

While bit manipulation is a very important topic, I chose to move on to
the more complex questions for now.

TODO return to this chapter and implement the solutions

"""

"""

Q 5.1

The strategy I employ is:

if N = xxxxxxx
if M = yyy
if j = 5
if i = 3

		xxxxxxx
	&	1100011
	============
a =		xx000xx
m =		  yyy00

	 	xx000xx
	|	  yyy00
	============
		xxyyyxx
"""

def five_point_one(n, m, i, j):
	all_ones = 0 ^ 0

	all_ones << (j-i+1)
	for x in range(i):
		all_ones << 1
		all_ones = all_ones & 1
	a = n & all_ones
	m = m << (i)
	return bin(m | n)

"""

Q 5.2

Admittedly, I'm not too sure of when it's impossible to represent a decimal number in binary.

I tried it for all sorts of ridiculous values and it was fine.

Either way, simply divide the problem into left-of-decimal and right-of-decimal and
proceed accordingly.

"""


def five_point_two(num):
	n = num // 1
	high_bit = math.ceil(math.log(n, 2))
	high_bit = pow(2, high_bit)
	left_of_dec = []
	right_of_dec = []
	d = num % 1
	while high_bit > 1:
		if n >= high_bit:
			n -= high_bit
			left_of_dec.append("1")
		else:
			left_of_dec.append("0")
		high_bit = high_bit/2
	left_of_dec.append("1" if n == 1 else "0")
	i = 1
	while d > 0:
		if d >= pow(2, (0-i)):
			d -= pow(2, (0-i))
			right_of_dec.append("1")
		else:
			right_of_dec.append("0")
		i +=1
	if d < 0:
		return False
	return ".".join(["".join(left_of_dec), "".join(right_of_dec)])


"""

Q 5.3

First, count the number of 1 bits.

	101011
	next-largest 	= 101110
	next-smallest 	= 100111 


TODO Return to this -.-

"""

def five_point_three(num):
	n = num
	num_ones = 0
	next_smallest = num
	next_largest = num
	while n > 1:
		if n % 2:
			num_ones += 1
		n = n // 2
	n += (1 if n % 2 else 0)
	#if number is even, next-smallest will just be
	if not (num % 2):
		next_smallest = next_smallest >> 2
		next_smallest = next_smallest << 2
		next_smallest = next_smallest & 1

	#if number is odd, next-smallest will be
	#find the first 10 pair, and flip them


"""

Q 5.4

0101 && 0100 == 0100 != 0
1010 && 1001 == 1000 != 0
1111 && 1110 == 1110 != 0 False
0001 && 0000 == 0000 == 0
0010 && 0001 == 0000 == 0
0100 && 0011 == 0000 == 0
1011 && 1010 == 1010 != 0

So, it would appear that what it does is return true if there is only one 
bit in a number n set as 1.

"""

"""

Q 5.5

This one is sort of similar to 5.2.

It's also similar to the common greedy 'what is the minimum number of coins required'
question. Basically, start with the max value of a number as long as a in binary
see if subtracting it from a would be larger than b, if so, add one to your running total
and subtract it. Otherwise, move on to the next-smaller value

"""

def five_point_five(a, b):
	high_bit = math.ceil(math.log(a, 2))
	# should return upper bound of a in binary
	high_bit = pow(2, high_bit)
	n = a
	x = 0
	while high_bit > 1:
		if (n - high_bit) > b:
			n = n-high_bit
			x += 1
		high_bit = high_bit // 2
	if n != b:
		return x + 1
	return x


"""

Q 5.6

Uh.... a << 1?

010100
101000

Basically, for each pair, we have two options
00 ==> 00
01 ==> 10
10 ==> 01
11 ==> 11

00 ^ 11 == 11
01 ^ 11 == 10
10 ^ 11 == 01
11 ^ 11 == 00

There's gotta be a trick here >.<

"""



"""

Q 5.7

Yep - Add together the number of times you see a 1 in a particular position j

000
010
110
001
101
011
111
= [3, 4, 4]
so it would appear that we're missing a one in the Most Significant bit
Therefore the missing number is 100, which it is!

"""

def five_point_seven(a):
	arr = []
	i = 0
	while i < len(a):
		for j in range(len(a[i])):
			if i == 0:
				arr.append(a[i][j])
			else:
				if a[i][j] == 1:
					arr[j] += 1
		i += 1
	ret = []
	for i in arr:
		if i == len(a)/2:
			ret.append(0)
		else:
			ret.append(1)
	return "".join(ret)










