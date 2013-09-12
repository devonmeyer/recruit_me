"""

Q 1.1

Two approaches

1 - Store each element in a hash-based set, and for each element determine if it already belongs to the set, if not add it to the set. This is space-complexity O(N), time-complexity O(N).  

2 - Sort the string lexicographically (i.e. a<b<A<C<Z) and then run through the sorted string and return False if there are any repeated characters. This requires no additional data structure, time-complexity O(N*log(N))

"""

def one_point_one_a(s):
	chars = set()
	for char in s:
		if char in chars:
			return False
		chars.add(char)
	return True

def one_point_one_b_naive(s):
	for i, char in enumerate(s):
		if i == len(s)-1:
			return True
		for rest_char in s[i+1:]:
			if char == rest_char:
				return False

def recurse(s):
	if len(s) == 1:
		return s
	else:
		left_half = recurse(s[:len(s)/2])
		right_half = recurse(s[len(s)/2:])
		sorted_halves = []
		while len(left_half) and len(right_half):
			if left_half[0] > right_half[0]:
				sorted_halves.append(left_half[0])
				left_half.remove(0)
			else:
				sorted_halves.append(right_half[0])
				right_half.remove(0)
		if len(right_half) and not len(left_half):
			sorted_halves += right_half
		elif len(left_half) and not len(right_half):
			sorted_halves += left_half
		return sorted_halves


def one_point_one_b_optimum(s):
	s = recurse(s)
	for i, char in s[:len(s)-1]:
		if char == s[i+1]:
			return False
	return True


"""

Q 1.2

Assume s[len(s)-1] is the null character. Reverse the string that preceeds it.

"""

def one_point_two(s):
	i = 0
	j = len(s)-2
	s = list(s)
	while i < j:
		temp = s[i]
		s[i] = s[j]
		s[j] = temp
		i += 1
		j -= 1
	return "".join(s)

"""

Q 1.3

Python's .join() method ignores empty parts, so just set each duplicate elements to empty, and then join the product.

Solution A Assumes you only want to remove characters that come after first appearance. O(N)

Solution B Removes ANY character that duplicates, by splitting the for loop into two parts. O(2N) -> O(N)

"""

def one_point_three_a(s):
	chars = set()
	s = list(s)
	for i, char in enumerate(s):
		if char in chars:
			s[i] = ""
		else:
			chars.add(char)
	return "".join(s)

def one_point_three_b(s):
	chars = set()
	s = list(s)
	for char in s:
		if char not in chars:
			chars.add(char)
	for i, char in enumerate(s):
		if char in chars:
			s[i] = ""
	return "".join(s)

"""

Q 1.4

Store the number of times a certain element occurs in string a, ensure that it occurs the same number of times in string b.

"""

def one_point_four(a, b):
	a_count = {}
	a_chars = set()

	for char in a:
		if char in a_chars:
			a_count[char] += 1
		else:
			a_count[char] = 1
			a_chars.add(char)

	for char in b:
		if char not in a_chars:
			#this char occurs more in b than in a
			return False
		a_count[char] -= 1
		if a_count[char] == 0:
			#last time we can see this char without breaking
			a_chars.remove(char)
	if len(a_chars):
		#any remaining chars occur more in a than in b
		return False
	return True

"""

Q 1.5

Super easy with Python. Turn the string into a list, and then replace each occurance, then rejoin the list.
O(N) time-complexity

"""

def one_point_five(s):
	s = list(s)
	for i, char in enumerate(s):
		if char == " ":
			s[i] = "%20"
	return "".join(s)

"""

Q 1.6

Solution A - Append rotated array to new array.

Solution B - Without using a new array (i.e. solve in-place) TODO ???
			-> idea: recursively do this. start with edges, work your way in, or vice-versa

"""

def one_point_six_a(arr):
	#arr comes in the form of [[a, b],[c, d]], returns [[c, a][d, b]]
	#[a, b]  ===>  [c, a]
	#[c, d]  ===>  [d, b]
	i = 0
	new = []
	while i < len(arr[0]):
		new_row = []
		for j in range(len(arr[0])-1, -1, -1):
			new_row.append(arr[j][i])
		new.append(new_row)
		i += 1
	return new

"""

Q 1.7

We want to iterate through the MxN array, find all zeroes, and then set all columns/rows with a zero to zero.

"""

def one_point_seven(arr):
	zero_rows = set()
	zero_cols = set()
	for i, row in enumerate(arr):
		for col, item in enumerate(row):
			if item == 0:
				zero_rows.add(i)
				zero_cols.add(col)

	for i, row in enumerate(arr):
		for col, item in enumerate(row):
			if i in zero_rows:
				row[col] = 0
			if col in zero_cols:
				row[col] = 0
	
	return arr	

"""

Q 1.8

Assume that if a = b, then b.isSubstring(a) == True, then this becomes a very simple problem

	In fact, you don't even need the method, you can use simple equality, but the problem requests you use it.

"""

def one_point_eight(a, b):
	index_of_a_zero = b.find(a[0])
	if index_of_a_zero >= 0:
		return a.isSubstring("".join([b[index_of_a_zero:],b[:index_of_a_zero]]))
	return False