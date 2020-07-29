### Description ###

'''
Given a linked list, return the node where the cycle begins. If there is no 
cycle, return null.

To represent a cycle in the given linked list, we use an integer 'pos' which
represents the position (0-indexed) in the linked list where tail connects to.
If 'pos' is -1, then there is no cycle in the linked list. 

Note: Do not modify the linked list

Example 1:

Input: head = [3, 2, 0, -4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the
second node. 

Example 2: 

Input: head = [1, 2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the 
first node.

Example 3: 

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list
'''

### Algo ###

'''
Node3 ~> Node2 ~> Node0 ~> Node4
            ^                |
            |      <~~     <~~

There are going to be 2 pointers, pointing at Node3: pointer1 & pointer2

designate pointer1 as the slow moving pointer that goes from node to node at a time
designate pointer2 as the fast moving pointer that jumps from node to node to node at a time

we have to check either:
- fast pointer has reached the end of the list
OR
- fast pointer == slow pointer
    - the only time they'll be equal is the first run when we initialize them &
    if they are ever equal again then we know we have a cycle
'''

### Complexity ###

'''
Let n denotes to count of all nodes in this linked list, x denotes to the x-th 
node is the node that runner meets walker and y denotes to the node that cycle 
starts.

1. If there is no cycle in this linked list, it takes O(n/2) time for runner to 
    go through entire list.

2. If there exists a cycle in linked list, runner needs to take O(x) time to 
    meet walker. And after they meet each other, it takes O(y) time to let 
    seeker meet walker. So it will take O(x+y) = O(n+n) = O(n) time because x 
    and y are both less than n.

By 1 and 2, it’s clear that it takes O(n/2 + n) = O(n) time for detecting node 
    of cycle start.

For space complexity, it only uses O(1) extra space.
'''

### Code ###

class Solution:
    def detectCycle(self, head):
        '''
        :type head: ListNode
        :rtype: ListNode
        '''

        # approach
        # 1. use two pointer with different speed and meet each other
        # 2. put another pointer start from head
        # 3. the third pointer will finally meet walker at cycle start

        runner = walker = head

        while runner and runner.next:
            runner = runner.next.next
            walker = walker.next
            if runner == walker:
                seeker = head
                while seeker != walker: 
                    walker = walker.next
                    seeker = seeker.next

                return walker