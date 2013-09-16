import random

"""

Q 19.1

"""

def nineteen_point_one(arr, i, j):
	arr[i] = arr[i] + arr[j]
	arr[j] = arr[i] - arr[j]
	arr[i] = arr[i] - arr[j]
	return arr


"""

Q 19.2

"""

def nineteen_point_two(board):
	#check winning rows first
	i = 0
	while i < 3:
		z = None
		for j, item in enumerate(board[i]):
			if item != z and z is not None:
				break
			elif z is None:
				z = item
			else:
				if j == 2:
					print "Winning Row : ",i
					return True
		i += 1

	j = 0
	#check winning columns, now
	while j < 3:
		i = 0
		z = None
		while i < 3:
			if board[i][j] != z and z is not None:
				break
			elif z is None:
				z = board[i][j]
			else:
				if i == 2:
					print "Winning Column : ",j
					return True
			i+=1
		j+=1
	#check for the diagonals
	if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		print "Winning Diagonal : down-arrow"
		return True
	if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
		print "Winning Diagonal : up-arrow"
		return True
	#no winner
	print "No winning combination"
	return False

"""

Q 19.3

Here we need to recognize that the only way to get a trailing zero is to multiply by (n*10)

Therefore, find all of the occurances of 10 in the list of numbers leading up to 
n for n! and that will be the number of trailing zeros.

Keep in mind that for 5! you have:
5x4x3x2x1 == (5x2)x4x3x1 == 10x4x3x1

"""
	

def nineteen_point_three(n):
	fives = []
	tens = []
	twos = []
	others = []
	for i in range(1, n+1):
		x = i
		while x % 10 == 0:
			tens.append(10)
			x = x // 10
		while x % 5 == 0:
			fives.append(5)
			x = x // 5
		while x % 2 == 0:
			twos.append(2)
			x = x // 2
	num_zeros = 0
	while len(fives) and len(twos):
		fives.pop()
		twos.pop()
		num_zeros += 1
	while len(tens):
		tens.pop()
		num_zeros += 1
	return num_zeros


"""

Q 19.4

I don't think this is possible in Python, because it requires a C-level management of the int objects.

"""


"""

Q 19.5

"""

def nineteen_point_five(guess, soln):
	hits = 0
	pseudo_hits = 0
	soln = list(soln)
	guess = list(guess)
	for i, char in enumerate(guess):
		if char == soln[i]:
			hits += 1
			soln[i] = ""
			guess[i] = ""
	for char in guess:
		if char in soln and char != "":
			pseudo_hits += 1
	return hits, pseudo_hits


"""

Q 19.6

"""

def nineteen_point_six(i):
	thousands = i // 1000
	ones = i % 1000

	english_ones = {0 : "", 1: "One", 2: "Two", 3: "Three", 4: "Four",
					5 : "Five", 6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine"}
	english_tens = {0 : "", 1: "", 2: "Twenty", 3: "Thirty", 4: "Fourty",
					5 : "Fifty", 6 : "Sixty", 7 : "Seventy", 8 : "Eighty", 9 : "Ninety"}
	english_teens = {0 : "Ten", 1: "Eleven", 2: "Twelve", 3: "Thirteen", 4: "Fourteen",
					5 : "Fifteen", 6 : "Sixteen", 7 : "Seventeen", 8 : "Eighteen", 9 : "Nineteen"}

	t_h = thousands // 100
	t_t = thousands % 100 // 10
	t_o = thousands % 10

	h = ones // 100
	t = ones % 100 // 10
	o = ones % 10

	s = ""

	t_h = " ".join([english_ones[t_h], "Hundred"]) if t_h > 0 else ""
	if t_t > 1:
		t_r = " ".join([english_tens[t_t], english_ones[t_o] if t_o > 0 else ""])
	elif t_t == 1:
		t_r = english_teens[t_o]
	else:
		t_r = english_ones[t_o] if t_o > 0 else ""

	s_thousands = " ".join([t_h, t_r, "Thousand"]) if (t_h != "" or t_r != "") else ""

	h = " ".join([english_ones[h], "Hundred"]) if h > 0 else ""
	if t > 1:
		r = " ".join([english_tens[t], english_ones[o] if o > 0 else ""])
	elif t == 1:
		r = english_teens[o]
	else:
		r = english_ones[o] if o > 0 else ""

	s_rem = " ".join([h, r]) if (h != "" or r != "") else ""

	return " ".join([s_thousands, s_rem]).strip()


"""

Q 19.7

"""

def nineteen_point_seven(arr):
	max_sums = []
	max_sum = None
	for i, val in enumerate(arr):
		if i == 0:
			max_sums.append(val)
			max_sum = val
		else:
			x = val if val > (max_sums[i-1] + val) else (max_sums[i-1] + val)
			if x > max_sum:
				max_sum = x
			max_sums.append(x)
	return max_sum

"""

Q 19.8

This is a thought-problem. Here's a good approach:

Data
	What is the data you need?
	How do you get the data you need?
Storage
	How do you store the data you need?
	What data structures would be good for storing this data?
Solution
	How do you find the requested information?

So for this problem:

The data we need is a count of how many times each word that appears in a given book is repeated.

The way to get that data is to transform it into a .pdf, and then use an OCR tool to
read the text. Then, parse that text as if it were a plaintext file.

The storage of this data should come in two forms:
	A set containing all of the unique words present in the book
	A map of all repeated words to the number of times they're repeated
		i.e. if a word appears only once, it'd appear in the set, but not the map

The data structure to store this should be:
	- A Tree-based set and Tree-based map using lexigraphical values as keys or...
	- A Hash-set/hash-map. This could work splendidly, as there are certainly
	some really good hash algorithms that compute evenly distributed values for
	words. In short, this is likely a solved problem.

Finding the information we need is simple:
	1. Hash the request word
	2. Use the hash to access a bucket for that hash in the set of unique words.
	3. If the word is not in that bucket, return NOT FOUND
	4. Now use the same hash to access a bucket for that hash in the map.
	5. If the word is not in that bucket, return 1 (appeared once, but never again)
	6. Else, return the value for that word in the map.

"""


"""

Q 19.9

This question requires use of an XML library, which I'm not too keen on learning for a particular example.
TODO return to this and implement elementtree

"""


"""

19.10

I've seen this one before. It's pretty straightforward :)

Basically, if you have one rand5(), you have 5 possible outputs:
1, 2, 3, 4, 5

If you have two, you have 
2, 3, 4, 5, 6, 7, 8, 9, 10

But, let's take a lesson from the game of Craps
--> since this will not have an even distribution of probabilities from 2-10, it'd be
	a bad idea to use this as our rand7()-generating algorithm.


So, is there another way to do it? Of course! And it's much more interesting.

How about instead of adding the two together, which eliminates the variability of different permutations:
(i.e. 2,5 == 5,2 == 4,3 == 3,4 == 7)
And instead treat it like an n-ary tree!

If we approach the problem this way, we're given 25, equal-probability options.

So, how about we assign 3 options to each value.

This leaves us with 4 values left over, and to maintain an even distribution, we can't
just assign these to existing values. So if we get one of them, we re-try.

This means that we have a (78%) chance of getting a perfect, randomly-distributed value between 1-7
on the first try, and by the fourth try we have a (99.7%) chance.

This means that we require:
  2 * .78
+ 4 * .172
+ 6 * .038
+ 8 * .008
============
~ 2.54 rand5() calls on average to compute a rand7()

"""

def nineteen_point_ten():
	one = [[1,1], [1,2], [1,3]]
	two = [[1,4], [1,5], [2,1]]
	three = [[2,2], [2,3], [2,4]]
	four = [[2,5], [3,1], [3,2]]
	five = [[3,3], [3,4], [3,5]]
	six = [[4,1], [4,2], [4,3]]
	seven = [[4,4], [4,5], [5,1]]
	a = random.randint(1,5)
	b = random.randint(1,5)
	while a not in [1,2,3,4] and b != 1:
		a = random.randint(1,5)
		b = random.randint(1,5)
	if [a,b] in one:
		return 1
	elif [a,b] in two:
		return 2
	elif [a,b] in three:
		return 3
	elif [a,b] in four:
		return 4
	elif [a,b] in five:
		return 5
	elif [a,b] in six:
		return 6
	elif [a,b] in seven:
		return 7

"""

Q 19.11

If I'm allowed to use additional data structures, it's pretty straight-forward:
Add each member of the array to a hash-based set
Iterate through the array and determine if set.contains(value - arr[i])
Expected run-time would be O(N)
--> Once through to add every value to the set
--> Once through to check if the required value is in the set for each value of the array.

To avoid duplicate pair printings, we must keep another set of values that have already been printed.

This is shown in nineteen_point_eleven_a

If I'm supposed to do this within the array, then there's no way to avoid an O(N^2) algorithm,
because in the worst case there are no pairs that add up to the value, and we can't really
use any information to help us determine a case like that.

However, it's always good to optimize, so here we go:
1. While iterating through to check, if we find a pair, set the value of the array (arr) at
both indexes to None, and then all subsequent appearances of either value to None. We then
don't waste time on repeat pairs.
2. Instead of checking each value arr[j] for an arr[i] where i != j, let's just use
arr[j] for arr[i] where j > i. If there was a value before arr[i] for which arr[i]+arr[j] == val
then we'd already have found arr[i] and set it to None.

That's about it! Let's implement this in nineteen_point_eleven_b

NOTE this is actually a bit tricky thanks to Python's way of doing for-loops. But it works :P

"""

def nineteen_point_eleven_a(arr, num):
	vals = set()
	dupes = set()
	for i, val in enumerate(arr):
		if val not in vals:
			vals.add(val)
		else:
			if 2*val == num and val not in dupes:
				print "[ ",val,",",val," ]"
				dupes.add(val)

	for val in arr:
		if (num-val) in vals and val not in dupes:
			print "[ ",val,",",str(num-val)," ]"
			dupes.add(val)
			dupes.add(num-val)

def nineteen_point_eleven_b(arr, num):
	for i, i_val in enumerate(arr):
		if i_val is not None:
			for j, j_val in enumerate(arr[(i+1):]):
				if j_val is not None and j_val == num - i_val:
					print "[ ",i_val,",",str(num-i_val)," ]"
					for k, k_val in enumerate(arr[(i+j+1):]):
						if k_val == j_val:
							arr[k+i+j+1] = None
					arr[j+i] = None
					break


