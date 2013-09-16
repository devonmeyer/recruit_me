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

"""






