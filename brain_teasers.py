"""

Brain teasers are all about getting that 'aha!' moment.

"""

"""

Q 6.1

How about

(3+1)/(3/6)
4 / (1/2)
= 8

"""


"""

Q 6.2

My initial guess is that because it doesn't mention that you can't hang half of a domino off of the board,
in which case it very well is possible.

However, if there is an assumption that dominos cannot hang off of the board, then this is impossible.

"""


"""

Q 6.3

Yes, it's very simple.

1. Fill up the 3Q jug								3Q => 3 	5Q => 0
2. Pour into the 5Q jug								3Q => 0		5Q => 3
3. Fill up the 3Q jug								3Q => 3 	5Q => 3
4. Use the 3Q jug to fill up the 5Q jug				3Q => 1 	5Q => 5
5. Pour out the water in the 5Q jug					3Q => 1 	5Q => 0
6. Pour the 1Q into the 5Q jug						3Q => 0 	5Q => 1
7. Fill up the 3Q jug								3Q => 3 	5Q => 1
8. Pour the remaining 3Q into the 5Q jug			3Q => 0 	5Q => 4 !!!

Done!

"""

"""

Q 6.4

BEFORE I READ SOLUTION:

If I can't see the hat on my own head and I can't communicate to any other man in any way that they have a hat,
then it is essentially a randomized distribution.

First, assume you know the number c.

Then, there are n CHOOSE c possible combinations of c men who have a hat on.

In that case, it would take, worst case, n CHOOSE c nights to be sure that the hats are all gone.

Assuming we have no knowledge of c, it becomes a (n CHOOSE n) + (n CHOOSE (n-1)) + ... + (n CHOOSE 1) problem.

So, the knowledge of c allows us to eliminate unnecessary combinations
	(i.e. dunking everyone the first night, when only one person has a hat)

AFTER I READ SOLUTION:

Oh.... obviously. Goodness.

Well just to re-iterate the solution here:

If c == 1, and person A has a hat on, he can look around and see that nobody else has a hat.
	Therefore, he must have the hat, and it only takes one night.

If c == 2, persons A and B have hats. They can see that eachother has a hat, but don't know if they do.
	If, after the first night, the hat is still around, this means that there are two hats (b/c case 1 didn't happen)
	Therefore, c must == 2, and the two dunk themselves that night. This takes 2 nights.

Therefore, for c <= n, it takes c nights to remove all of the hats.

"""

"""

Q 6.5

First intuition is that this is a form of binary search with a little twist.

Start at N = 100/2 = 50

If the egg breaks, you know that N <=50. But now you have to check each floor from 1-50. That's bad.

The trick, perhaps, is to keep the number of divisions of the 100 floors equivalent to the 
number between each division. Let's harness the metric system and use a division of 10.

So in our new method, you start at N = 10. If the egg breaks, you then go back to N = 1 incrementing up.
If the egg breaks on 1-9, then you know the correct floor. If it doesn't break on 9, you have no reason
to re-do the final drop, because you already know it broke on floor 10.

If it did not break on floor 10, increment N by 10, and continue.

Worst case is 19 drops:
10 => 20 => 30 => 40 => 50 => 60 => 70 => 80 => 90 => 91 => 92 => 93 => 94 => 95 => 96 => 97 => 98 => 99 => 100

AFTER READING SOLUTION:

It appears that instead of using a division of 10, we should use a division of 14 to ensure the fewest
drops necessary to find the correct N.

"""

"""

Q 6.6

Well, this appears to be a problem of divisors.

For instance, if a locker is prime, and therefore has only two dividends ([1, 5], [1, 11], ...) then it will
only be visited once after being opened. Therefore, the lockers corresponding to prime numbers will be closed.

This can be generalized: any number with an even number of divisors between 2-100 will be closed,
while any number with an odd number of divisors between 2-100 will be open.

AFTER READING SOLUTION

It would appear that there is one step I missed ==> the only time x has an odd number of divisors
is when x is a perfect square. In which case there are 10 perfect squares, and therefore 10 open lockers
between 1-100.

"""

"""

That's all for the brain-teasers! Now on to OOD!

"""







