Array
=====

definition
----------

fixed-size, indexed, contiguous structures whose elements are all of the same
type, and whose elements can be accessed in constant time given their indices.

implementation
--------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class array:
    def __init__(self, size, object, init_value=None):
        self.size = size
        self.actual_size = size*object.size
        self.zero = malloc(self.actual_size)
        self.object_size = object.size
        for i in range(size):
            (self.zero + (i * self.object_size))* = init_value
    
    def get(self, index):
        return *(self.zero + (index * self.object_size))
    
    def set(self, index, object):
        *(self.zero + (index * self.object_size)) = object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### get(i)

**O(1)**

usage
-----

### general

-   size of input is unchanging

-   iterating upon items in array numerically

-   index of item is the key method of finding it

    -   not the value of the item

### real life

-   store list of Students by class rank

    -   constant time to find student by rank

    -   number of students in a class is unlikely to get larger

        -   those who drop can have their value set to None

-   store all raffle participants and use random number generator to find winner

    -   instant lookup of winner

    -   number of participants won't change

-   store a string and then reverse it

    -   can constant-time access the *n'th *character

    -   can easily overwrite the value of the *n'th* character

    -   can operate on it using numeric indexes

operations
----------

### insert

**O(N)**

*about 2N to be specific - plus memory allocation is a much heavier command than
say subtraction or multiplication*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def insert(self, index, object):
    new_zero = malloc(self.actual_size + self.object_size)
    for i in range(index):
        (new_zero + (i * self.object_size))* = self[i]
    (new_zero + (index * self.object_size))* = object
    for i in range(index, self.size):
        (new_zero + ((i+1) * self.object_size))* = self[i]
    self.size = self.size+1
    self.actual_size = self.size * self.object_size
    free(self.zero)
    self.zero = new_zero
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### delete

**O(N)**

*about 2N to be specific - plus memory allocation is a much heavier command than
say subtraction or multiplication*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def delete(self, index):
    new_zero = malloc(self.actual_size - self.object_size)
    for i in range(index):
        (new_zero + (i * self.object_size))* = self[i]
    for i in range(index+1, self.size):
        (new_zero + ((i-1) * self.object_size))* = self[i]
    self.size = self.size-1
    self.actual_size = self.size * self.object_size
    free(self.zero)
    self.zero = new_zero
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### find

**O(N)**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def find(self, object):
    for i in range(self.size):
        if self[i] == object:
            return i
    return -1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

traversal
---------

### method

Iterate through the array incrementally by object, operating on each item from
beginning to end.

### implementation

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def traverse(self, perform_action, *args):
    for i in range(self.size):
        perform_action(self[i], *args)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### ordering

The ordering of the traversal will just be the iterative order of the array
(i.e. array[0], array[1], array[2], etc.



Vector
======

definition
----------

also known as "growable arrays" or ArrayLists. Objects that are backed by a
fixed-size array, which resize themselves as necessary.

implementation
--------------

usage
-----

### general

### real life

operations
----------

### insert

### delete

### find

traversal
---------

### method

### implementation

### ordering



Linked List
===========

definition
----------

lists made of nodes that contain a data item and a pointer/reference to the next
node. Doubly-linked lists also contain a pointer/reference to the previous node

implementation
--------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class linked_list:
    def __init__(self, first_object=None):
        self.head = Node(first_object)
        self.tail = self.head
        self.size = 1
    
    def get(self, index):
        if index > self.size / 2:
            n = self.tail
            for i in range(self.size, self.size-index, -1):
                n = parent
        else:
            n = self.head
            for i in range(index):
                n = n.child

    class Node:
        def __init__(self, value, parent=None, child=None):
            self.value = value
            self.parent = parent
            self.child = child

  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### get(i)

**O(N)**

usage
-----

### general

-   when the size of the input is dynamic, changing

-   when in most cases you just want to access first/last element

### real life

-   stacks/queues/dequeues are typically implemented with linked list

    -   super easy to pop, push, etc. (**O(1)**)

    -   rarely a need to get to a 'middle' element

-   hash tables use linked lists for bucket storage

operations
----------

### insert

**O(N)**

*asymptotically similar, but realistically much better than Array*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def insert(self, obj_val, index):
    n = self.get(index)
    new_n = Node(obj_val, parent=n.parent, child=n)
    n.parent = new_n
    new_n.parent.child = new_n
    self.size = self.size + 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### delete

**O(N)**

*asymptotically similar, but realistically much better than Array*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def delete(self, index):
    n = self.get(index)
    n.parent.child = n.child
    n.child.parent = n.parent
    self.size = self.size - 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### find

**O(N)**

*essentially the same idea as Array*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def find(self, obj_val):
    n = self.head
    while(n.value != obj_val and n != self.tail):
         n = n.child
    if n.value == obj_val:
        return n
    else:
        return -1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

traversal
---------

### method

One of two traversals, but basically reversals of one-another:

1.  Start at the head, perform action, continue until you hit the tail

2.  Start at the tail, perform action, continue until you hit the head

Both are **O(N)**

### implementation

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def traverse(self, perform, args*):
    n = self.head
    while n != self.tail:
        perform(n, args*)
        n = n.child
    perform(n, args*)

def reverse_traverse(...):
    n = self.tail
    while n != self.head:
        ...
        n = n.parent
    ...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### ordering

Depending on the type, it is either FIFO or LIFO:

-   First-in-first-out: The first node to be performed upon is the first node
    that entered (the tail of the list)

-   Last-in-first-out: The first node to be performed upon is the last node that
    entered (the head of the list)



Hash Map
========

definition
----------

amortized constant-time access data structures that map keys to values, and are
backed by a real array in memory, with some form of collision handling for
values that hash to the same location.

implementation
--------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class hash_map:
    def __init__(self, size):
        self.array = [linked_list()]*size
    
    def get(self, key):
        index = hash(key) % size
        if self.array[index]:
            self.array[index].find(Mapping(key, None))

    class Mapping:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            return self.key == other.key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### get(key):

**worst-case: O(N)**

**amortized: O(1)**

usage
-----

### general

-   input is in form of a key-value pair

-   number of keys can be generally estimated

-   a proper hash function exists for the type of key

### real life

-   storing occurrences of an object in a list of repeated objects

-   pattern recognition algorithms

    -   can enumerate a pattern and hash it

-   if number of input is limited or known, hash map avoids much of the overhead
    of tree-based map

operations
----------

### insert

**Worst case : O(N)**

**Amortized : O(1)**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def insert(self, key, object):
    index = hash(key) % size
    self.array[index].append(Mapping(key, value))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### delete

**Worst case : O(N)**

**Amortized : O(1)**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def delete(self, key):
    index = hash(key) % size
    self.array[index].delete(Mapping(key, None))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### find

**Worst case : O(N)**

**Amortized : O(1)**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def find(self, key):
    index = hash(key) % size
    return self.array[index].find(Mapping(key, None))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

traversal
---------

### method

**generally not something you'd do on a hash map**

however, as the base of the hash map is simply an array, you can simply traverse
the underlying array

in every case, the complexity is **O(max(N, size))**

### implementation

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def traverse(self, perform, *args):
    for item in self.array:
        if len(item): item.traverse(perform, *args)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### ordering

**random ordering**

the strength of the hash map is in this random assignment to buckets

as a result, however, it is impossible to sort in its inherent form

trees
=====

definition
----------

Consist of nodes with optional data elements and one or more child
pointers/references, and possibly parent pointers, representing a heirarchical
or ordered set of data elements.

implementation
--------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Tree:
    class Node:
        def __init__(self, value=None, parent=None, left=None, right=None):
            self.value = value
            self.parent = parent
            self.left = left
            self.right = right
            self.lowest = self.head
            self.second_lowest = self.head

    def __init__(self, start_val=None):
        self.head = Node(value=start_val)
        self.size = 1 if start_val is not None else 0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

usage
-----

### general

-   extremely versatile

-   when you want to access things at log(n)

-   when you want to specify relationships and levels of connectedness

### real life

-   heaps

-   binary search trees

    -   treemaps

-   simplified graphs (no side or backwards edges, undirected)

operations
----------

### insert

**Worst Case : O(N)**

**Typically : O(log(n))**

*need to have a balanced tree to have log(n)*

*assuming no specific requirements - i.e. not a heap or bst, etc.*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def insert(self, val):
    n = self.lowest
    if n.value is None:
        n.value = val
        return True
    if n.left is None:
        n.left = Node(value=val, parent=n)
        return True
    # we know that n.right is none...
    n.right = Node(value=val, parent=n)
    # now we need to reset the lowest
    while n is n.parent.right:
        n = n.parent
    n = n.parent.right
    while n.left is not None:
        n = n.left
    self.second_lowest = self.lowest
    self.lowest = n
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### delete

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def delete(self, val):
    n = self.find(val)
    self.lowest = self.second_lowest.parent
    n = self.second_lowest
    if self.lowest.left = self.second_lowest:
        self.lowest.left = None
    else:
        self.lowest.right = None
    return True
    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### find

traversal
---------

### method

### implementation

### ordering

graphs
======

definition
----------

Represent arbitrary relationships between members of any data set, represented
as networks of nodes and edges.
