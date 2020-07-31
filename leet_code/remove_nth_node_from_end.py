### Description ###

'''
Given a linked list, remove the n-th node from the end of the list and return
its head.
'''

### Intuition ###

'''
1 ~> 2 ~> 3 ~> 4 ~> 5

and n = 2

When n = 2, it's asking to removed the the second to last node from the end.

Resulting in 1 ~> 2 ~> 3 ~> 5

Can you do this in one pass?
'''

### Algo & Psuedo Code ###

'''
Can not traverse backwards beacuse there is no pointer pointing backwards. 

What we need to do is find the complement of n.

Complement = 'k' = the # from the beginning of the list. 

We need to count how many nodes exist in the linked list (5) and subtract
n from this value, which will give us our 'k'

5 - 2 = 3. 

3 represents the number from the beginning. Remember that index starts at 0, so
technically we are trying to remove the 4th node.

k = 3(4)

We can't lose the reference to the head of this linked list, so we do instead
is have a pointer that points to this list and iterates in a while loop until
k = 0. 

While K != 0, we can decrement k and increment ptr (our pointer)
k -- 
ptr = ptr.next

How can we remove the node from a linked list?
- Only WAY: have a  pointer pointing to that node to be removed and have it not 
    pointing at that node anymore.
- in this case we are going to need two pointers
- prev pointer is always going to be one step behind ptr
- this way when we have a reference to the previous pointer, we can easily
    change the value that the next node after Node3 is Node5
- technically, Node4 is still pointing to Node5, which can be removed
- 

prev.next = ptr.next
ptr.next = None
return head
'''

### Complexity ###

'''
Time: O(n + n) = O(n)

Space: O(1)
'''

### Code ### 

class Solution(object):
    def remove_nth_from_end(self, head, n):
        # Find the proper index 'k'
        temp = head
        num_nodes = 0
        while temp is not None:
            temp = temp.next 
            num_nodes += 1
        k = num_nodes - n 

        # Find the proper node to remove
        prev = None
        pointer = head 
        while k != 0:
            prev = pointer
            pointer = pointer.next 
            k -= 1
        
        # Remove Node
        if prev is None:
            return head.next
        else:
            prev.next = pointer.next 
            pointer.next = None 
            return head
