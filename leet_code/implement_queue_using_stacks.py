### Description ### 

'''
Problem

Implement the following operations of a queue using stacks.

    push(x) — Push element x to the back of queue.
    pop() — Removes the element from in front of queue.
    peek() — Get the front element.
    empty() — Return whether the queue is empty.

Example:

MyQueue queue = new MyQueue();queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:

1. You must use only standard operations of a stack — which means only push to 
    top, peek/pop from top, size, and is empty operations are valid.

2. Depending on your language, stack may not be supported natively. You may 
    simulate a stack by using a list or deque (double-ended queue), as long as 
    you use only standard operations of a stack.

3. You may assume that all operations are valid (for example, no pop or peek 
    operations will be called on an empty queue).
'''

### Approach ###

'''
Use another stack to reverse data for pop and top manipulations. 

And use a pointer to save the bottom data of stack so it may be used in peek 
manipulation.
'''

### Complexity ###

'''
For push/peak/empty methods, it’s trivial that these manipulations only take O(1) time.

However, for pop method, we have two aspects of it.

General Analysis:

If we only look at pop manipulation, it may costs O(n) time in worst case. Hence 
    time complexity is O(n) if n denotes to all elements to handle with.

Amortised Analysis:

If we look entire processing of all elements, we will find that each element 
will be move from stack to reverse_stack only once. It means the while loop in 
line 51 will only execute O(n) time totally. 

Therefore, it only takes O(n/n) = O(1) time for pop manipulation.
'''

### Code ###

# implement stack manipulations
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    
# restrict manipulations that can only be implemented by above methods
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = Stack()
        self.stack_front = None
        self.reverse_stack = Stack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.stack.isEmpty():
            self.stack_front = x
        self.stack.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.reverse_stack.isEmpty():
            while self.stack.size():
                self.reverse_stack.push(self.stack.pop())
        return self.reverse_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.reverse_stack.size():
            return self.reverse_stack.peek()
        return self.stack_front

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack.isEmpty() and self.reverse_stack.isEmpty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()