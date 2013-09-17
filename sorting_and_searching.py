from collections import deque

"""

This is chapter 9?! I feel like sorting and searching are, almost by definition,
the very core of CS problems.

Perhaps it's personal opinion, but the biggest issue in CS is not how to do X--
there are algorithms galore and it just takes a tricky combination of some of them
to come up with the right answer.

But organizing the chaos that is 'data' is quite the challenge. Once it's organized
and made-sense-of, anyone can benefit from it.

...

Hmm, I like that. Software Engineers: Bringing order to chaos.

"""


"""

Q 9.1

Hello merge-sort

Assuming increasing order.

This turned out to be quite a bit more complex than it probably should be.
	BUT it keeps O(len(a)+len(b)) merging time.

TODO: re-implement - simpler!!

"""

def nine_point_one(arr_a, arr_b):
	i = 0
	j = 0
	a_vals = deque()
	while i < (len(arr_a)) and j < (len(arr_b)) :
		if arr_a[i] is None:
			if len(a_vals):
				a_v = a_vals.popleft()
				if a_v < arr_b[j]:
					arr_a[i] = a_v
				else:
					arr_a[i] = arr_b[j]
					a_vals.appendleft(a_v)
					j += 1
			else:
				arr_a[i] = arr_b[j]
				j += 1
		else:
			if arr_a[i] > arr_b[j] or len(a_vals):
				if len(a_vals):
					a_v = a_vals.popleft()
					a_vals.append(arr_a[i])
					if a_v < arr_b[j]:
						arr_a[i] = a_v
					else:
						a_vals.appendleft(a_v)
						arr_a[i] = arr_b[j]
						j += 1
				else:
					a_vals.append(arr_a[i])
					arr_a[i] = arr_b[j]
					j += 1
		i += 1
	while len(a_vals):
		arr_a[i] = a_vals.popleft()
		i += 1
	return arr_a



"""

Q 9.2

[abc, bac, bcd, acb, bkl]
{abc : [0, 1, 3], bcd : [2], blk : [4]}

"""

def nine_point_two(arr):
	anagrams = {}
	found = set()
	for i, string in enumerate(arr):
		s = "".join(sorted(string))
		if s in found:
			anagrams[s].append(i)
		else:
			found.add(s)
			anagrams[s] = [i]
	result_array = []
	for item in found:
		for i in anagrams[item]:
			result_array.append(arr[i])
	return result_array



"""

Q 9.3

First: Find where the array has been rotated (O(logn))
Second: Use that information to complete a binary sort for the value

"""

def nine_point_three(arr, n):
	a = arr
	i = len(a)/2
	j = len(a)-1
	actual_left = 0
	while a[i] < a[i+1]:
		if a[i] < a[j]:
			a = a[:i]
			i = len(a)/2
			j = len(a)-1
		else:
			actual_left = actual_left + i
			a = a[i:j+1]
			i = len(a)/2
			j = len(a)-1
	actual_left = actual_left+i+1
	i = ((actual_left + len(arr))/2) % len(arr)
	l = len(arr)
	actual_right = actual_left-1
	while arr[i] != n:
		if arr[i] > n:
			actual_right = i
			l = l / 2
			actual_left = ((actual_right - l) / 2) % len(arr)
			i = (actual_right - (l/2)) % len(arr)
		else:
			actual_left = i
			l = l / 2
			actual_right = ((actual_left + l)) % len(arr)
			i = (actual_left + (l/2)) % len(arr)

	return i

"""

Q 9.4

Definitely would use Quicksort, using a lexigraphical compare.

This would allow me to do the sort within the file, as opposed to merge-sort, which
requires that I essentially copy the file over to another file.

"""

"""

Q 9.5

Use a binary sort, but instead of comparing directly to the value in the median,
call another method that returns the 'closest' string to that value.

TODO Fix

"""

def nine_point_five(arr, s):
	i = len(arr) / 2
	closest_s = closest_str(arr, i)
	a = arr
	while s != closest_s:
		if s > closest_s:
			a = a[:i]
		else:
			a = a[i+1:]
		i = len(arr) / 2 - 1
		if i < len(arr)-1 and i >= 0:
			closest_s = closest_str(a, i)
		else:
			return -1
	return closest_s


def closest_str(arr, i):
	if arr[i] != "":
		return arr[i]
	j = i
	while arr[j] == "" and arr[i] == "":
		j += 1
		i -= 1
	if arr[j] == "":
		return arr[i]
	return arr[j]

"""

Q 9.6

I'd assume that this means that a[x][0] > a[x][i] for all x and for all i > 0,
and that a[0][x] > a[i][x] for all x and for all i > 0

Then do a binary search!

TODO Fix

"""

def nine_point_six(arr, val):
	a = arr
	i = len(a) / 2
	left = 0
	right = len(a) - 1
	j = 0
	if a[i][j] > val:
		a = a[:i]
		i = len(a)/2
		while a[i][0] > val:
			a = a[:i]
			i = len(a)/2
		j = 0
	else:
		a = a[i:]
		i = len(a) / 2
		while a[i][0] < val:
			a = a[i:]
			i = len(a) / 2
		i -= 1
		j = 0
	while a[i][j] < val:
			if j == len(a[i]) - 1:
				j = 0
				i += 1
			else:
				j += 1
			if i == len(a):
				return -1
	if a[i][j] == val:
		return [i, j]
	return -1
















