import random
from collections import deque

"""

Q 7.1

This is the base level of OOD questions. I remember the deck of cards question was the 
example used to teach OOD in my CS 200 class. Memories...

"""

# First, create a Card class.

# For later convenience, I store both the value (A, 2, 3, 4, ... 10, J, Q, K)
# and the number (2-14 inclusively... 11 = J, 12 = Q, ...)

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.number = value if value not in ["J", "Q", "K", "A"] else (11 if value == "J" else (12 if value == "Q" else (13 if value == "K" else 14)))
		self.value = value

	def __str__(self):
		return " of ".join([str(self.value), str(self.suit)])

# Now I create a generic deck.

# You should be able to initialize a deck with some collection of cards
# This allows you to re-use cards like you would in a real card game
# (You don't open a new deck every time you've played a hand of poker right?)

class Deck:
	def __init__(self, cards=None):
		if cards is None:
			self.cards = []
			for v in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']:
				for s in ['Spades', 'Clubs', 'Hearts', 'Diamonds']:
					self.cards.append(Card(s, v))
		else:
			self.cards = cards

	def shuffle(self):
		for i in range(len(self.cards)):
			j = random.randint(0, len(self.cards)-1)
			temp = self.cards[i]
			self.cards[i] = self.cards[j]
			self.cards[j] = temp

	def get_top_card(self):
		return self.cards.pop()

	def add_card_to_top(self, c):
		self.cards.append(c)

	def add_card_to_bottom(self, c):
		# If this is a common method, you may want to consider using a deque instead of a stack.
		self.cards.insert(0, c)



"""

To address the follow-up question, let's take the case of Blackjack.

A Blackjack deck has a number of decks -- usually 3-4 decks in a shoe.

So, simply change the init function to insert x copies of each card.

In general, though, you'd want to keep track of a 'discard' deck for most games, or
for a game like War, each user has their own deck and discard deck.

The implementation of these isn't terribly complicated, but it's up to the
logic of the game program to determine when to re-shuffle, etc.

"""


"""

Q 7.2

So let's look at this analogous to our Deck design question.

A Team has a number of Freshers, a Tech Lead, and a Product Manager.

Then, when you call get_call_handler(), the first return should be a free Fresher.

If the get_call_handler() method is then called again, with an instance of a Fresher
passed into it, then you wait until the TL is free, and then give it to them.

And finally, if get_call_handler() is called with a TL instance, then you wait until
the PM is free, and then return them.

"""

class Employee:
	def __init__(self, emp_name, emp_type):
		self.type = emp_type
		self.name = emp_name # Always good to include a name! We're representing humans after all!
		self.is_free = True

class CallCenter:
	def __init__(self, num_freshers):
		self.freshers = []
		names = ["Bob", "Lisa", "Jake", "Joe", "Jill", "Andrew", "Christine", "Dylan", "Suzan", "Jane"]
		for i in range(num_freshers):
			self.freshers.append(Employee(names[random.randint(0, len(names)-1)], "Fresher"))
		self.tech_lead = Employee(names[random.randint(0, len(names)-1)], "Tech Lead")
		self.project_manager = Employee(names[random.randint(0, len(names)-1)], "Project Manager")

	def get_call_handler(self, refferer=None):
		if referrer is None:
			while True:
				for emp in self.freshers:
					if emp.is_free:
						emp.is_free = False
						return emp
		elif referrer.type == "Fresher":
			while True:
				if self.tech_lead.is_free:
					break
			self.tech_lead.is_free = False
			return self.tech_lead
		elif referrer.type == "Tech Lead":
			while True:
				if self.project_manager.is_free:
					break
			self.project_manager.is_free = False
			return self.project_manager
		else:
			return None

"""

As you can see, we're making a few assumptions here.

First, we're assuming that the employee resets his/her self.is_free variable when they've
finished a call. Additionally, we're not keeping track of a queue of waiting calls, 
but instead blocking until an employee can take care of the call.

This is a straightforward solution, and for a call center with moderate traffic, would
work fine. But let's develop another solution that scales better.

"""

class Call:
	def __init__(self, customer):
		self.customer = customer
		self.representative = None

class BetterEmployee:
	def __init__(self, emp_name, emp_type):
		self.type = emp_type
		self.name = emp_name
		self.is_free = True
		self.current_call = None

class BetterCallCenter:
	def __init__(self, num_freshers):
		self.freshers = []
		names = ["Bob", "Lisa", "Jake", "Joe", "Jill", "Andrew", "Christine", "Dylan", "Suzan", "Jane"]
		for i in range(num_freshers):
			self.freshers.append(BetterEmployee(names[random.randint(0, len(names)-1)], "Fresher"))
		self.tech_lead = BetterEmployee(names[random.randint(0, len(names)-1)], "Tech Lead")
		self.project_manager = BetterEmployee(names[random.randint(0, len(names)-1)], "Project Manager")
		self.calls_queued = {"Fresher": deque(), "Tech Lead": deque(), "Project Manager": deque()}

	def get_call_handler(self, call, refferer=None):
		if referrer is None:
			self.calls_queued["Fresher"].append(call)
			self.assign_calls()
		elif referrer.type == "Fresher":
			self.calls_queued["Tech_Lead"].append(call)
			self.assign_calls()
		elif referrer.type == "Tech Lead":
			self.calls_queued["Tech_Lead"].append(call)
			self.assign_calls()
		else:
			return None

	def assign_calls(self):
		if len(calls_queued["Fresher"]):
			for e in self.freshers:
				if e.is_free:
					self.assign_call(e, calls_queued["Fresher"].popleft())
			if not len(calls_queued["Fresher"]):
				break
		if len(calls_queued["Tech Lead"]):
			if self.tech_lead.is_free:
				self.assign_call(e, calls_queued["Tech Lead"].popleft())
		if len(calls_queued["Project Manager"]):
			if self.tech_lead.is_free:
				self.assign_call(e, calls_queued["Project Manager"].popleft())

	def assign_call(self, employee, call):
		employee.is_free = False
		employee.current_call = call
		call.representative = employee

	def call_finished(self, employee):
		employee.is_free = True
		self.assign_calls()

"""

In our new case, the flow is much more natural:

Caller initiates call
Call Center adds call to queue
Call Center assigns free employee to call
Employee performs call
Employee notifies Call Center that he/she is free for another call
Call Center immediately assigns any existing call to employee

Makes sense right? Defined structure, like this, is very good for OOD.
It may not be the best way to run a call center, though! (At least the employees have names)

"""

