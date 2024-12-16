# Data Structures Easy to Advanced Course - Full Tutorial from a Google Engineer
[Youtube Videos](https://www.youtube.com/watch?v=RBSGKlAvoiM&ab_channel=freeCodeCamp.org)

## Introduction
* What is a Data Structure?
A **data structure** is a way of organizing data so that it can be used effectively.

They are essential ingredients in creating fast and powerful algorithms.
They help to manage and organize data.
They make code cleaner and easier to understand.

## Abstract Data Types vs. Data Structures

### Abstract Data Type
An **abstract data type** is an abstraction of a data structure which provides only the interface to which a data structure must adhere to.

The interface does note give any specific details about how somethin should be implemented or in what programming language.

![Abstraction vs Implementation Examples](./abstraction_implementation_examples.png)

## Computational Complexity Analisys

How much **time** does this algorithm need to finish?
How much **space** does this algorith need for its comoutation?

### Big-O Notation

*n: input size*

Constant Time: O(1)
Logarithmic Time: O(log(n))
Linear Time: O(n)
Linearithmic Time: O(nlog(n))
Quadric Time: O(n²)
Cubic Time: O(n³)
Exponential Time: O(b^n), b > 1
Factorial Time: O(n!)

## Static and Dynamic Arrays

### Static Array
A static array is a fixed length container containing n elements **indexable** from the range [0, n-1].

When and where is a static Array used?
1. Storing and acesing sequential data;
2. Temporarily storing objects
3. Used by IO routines and buffers
4. Lookup tables and inverse lookup tables
5. Can be used to return multiple values from a function
6. Used in dynamic programming to cache answers to subproblems 

### Dynamic Array
The dynamic array can **grow** and **shrink** in size.

1. Create a static array with an inicital capacity;
2. Add elements to the underlying static array, keeping track of the number of elements;
3. If adding another element will exceed the capacity, then create a new static array with twice the capacity and copy the original elements into it.

### Complexity:
![Static and Dynamic Array Complexity](./static_and_dinamic_array_complexity.png)

## Singly and Doubly Linked Lists

### Linked list

A **linked list** is a sequential list of nodes that hold data which point to other nodes also containing data.

* Terminology:
    * Head: The first node;
    * Tail: The last node;
    * Pointer: Reference to another node;
    * Node: An object containing data and pointer(s)

### Singly linked list vs. Doubly linked list
Singly linked list only hold a reference to the next node.
Doubly linked list hold a reference to the next and previous node.

#### Pros and Cons
| | Pros | Cons |
| --- | --- | ---
| Singly linked | Uses less memory / Simpler implementation | Cannot easilyacess previous elements
| Doubly linked | Can be traversed backwards | Takes 2x memory

#### Complexity

| | Singly Linked | Doubly linked |
| --- | --- | --- |
| Search | O(n) | O(n) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(1) | O(1) |
| Remove at head | O(1) | O(1) |
| Remove at tail | O(n) | O(1) |
| Remove in middle | O(n) | O(n) |

## Stack

Is a one-ended linear data structure which moels a real world stack by having two primary operations, namely **push** and **pop**.

### Complexity

| --- | --- |
| Pushing | O(1) |
| Popping | O(1) |
| Peeking | O(1) |
| Searching | O(n) |
| Size | O(1) |

## Queues

A queue is a linear data structure which models real world queues by having two primary operations, namely **enqueue** and **dequeue**.

**Enqueue:** put element in the back of the queue
**Dequeue:** remove the element of the front of the queue

 ### Complexity

 | --- | --- |
 | Enqueue | O(1) |
 | Dequeue | O(1) |
 | Peeking | O(1) |
 | Contains | O(n) |
 | Removal | O(n) |
 | Is Empty | O(1) |
