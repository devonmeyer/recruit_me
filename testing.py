"""

Q 11.1

Assuming the idea is 'print all numbers from 100 to 0 inclusively, in reverse'

i <= 0		should be		i >= 0
--i 		should be		i--

"""


"""

Q 11.2

A. Input manipulation --> if the input affects the access of other variables
(i.e. cin >> x, array[x] = ...) then a simple difficulty in expected input
can trickle down and cause problems anywhere.

B. Conditional exit clauses --> if there are exit clauses that are based on user input
or random values, that could be the source of the issue. (see above)

C. Array arithmetic could be off --> If you're expecting a value a that's less than b,
but you've accessed the wrong part of a sorted array, your code will go haywire!

The way I'd test the first two is to see if putting identical information into the system,
and eliminating random variables (i.e. set rand7 to some constant between 1-7), if it still
acts erratically. If not, then I investigate each use, and segment the code by inputs and
random variables, and determine where it's performing erratically.

If it still breaks after doing the above steps, then I'll take a look at my array arithmetic and
use some logs to ensure that what I'm getting is what I'd expect to get at certain
points in the code.

"""



"""

Q 11.3

Well, I'd keep a log of every request made to that method, and then directly access
the space specified. Essentially, I'd log the x,y value and then whether or not there
already exists a piece, whether or not that x,y value is accessible given the requesting
piece, etc.

"""


"""

Q 11.4

Write one hell of a script.

Create a bunch of curls to the server, have some wait certain amounts of time before re-requesting.
		--> Have some random variables in there (i.e. intervals between connections, etc.)
		--> Have each client act in a random manner (i.e. find a link on the page and request that, repeat 20 times)
Also, I'd create a launch script to occur at certain intervals (i.e. every 5th minute on the second)
to create cases of simultaneous access to the server.

Etc.

"""


"""

Q 11.5

A pen?

This is a thought question - I'd write on a number of different, very different-textured objects.
I'd write for varying amounts of time, in varying situations (very hot, very cold)
I'd use varying levels of pressure (very light, very hard)
I'd try some point testing (drawing points, not lines) and then line testing (very long lines)

It'd be great if I could measure the amount of ink left in the pen after each trial, to determine
under what conditions it begins to fail.

I'd also force it to fail, and ensure that it fails gracefully.
		--> Write for 200 hours straight?
		--> Try to write without an ink tube?
		--> Try to write without a ball point?
		--> Try to write without an exterior?

Etc.


"""


"""

Q 11.6

I'd like to attack some more difficult problems today, so I'll come back to this one

TODO Return to this problem -- it will be similar to 11.5 U 11.4

"""