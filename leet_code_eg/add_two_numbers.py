### Description ###

'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single 
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

### Intuition ###

'''
Keep track of the carry using a variable and simulate digits-by-digits sum 
starting from the head of list, which contains the least-significant digit.
'''

### Algo + Psuedo Code ###

'''
Just like how you would sum two numbers on a piece of paper, we begin by summing 
the least-significant digits, which is the head of l1 and l2. Since each 
digit is in the range of 0…90 \ldots 90…9, summing two digits may "overflow". 
For example 5+7=12. In this case, we set the current digit to 2 and bring over 
the carry=1 to the next iteration. carry must be either 0 or 1 because the 
largest possible sum of two digits (including the carry) is 
9+9+1=19.

The pseudocode is as following:

    Initialize current node to dummy head of the returning list.
    Initialize carry to 0.
    Initialize p and q to head of l1 and l2 respectively.
    Loop through lists l1 and l2 until you reach both ends.
        Set x to node p's value. If p has reached the end of l1, set to 0.
        Set y to node q's value. If q has reached the end of l2, set to 0.
        Set sum=x+y+carry
        Update carry=sum/10.
        Create a new node with the digit value of (sum mod 10) and set it to 
        current node's next, then advance current node to next.
        Advance both p and q.
    Check if carry=1, if so append a new node with digit 1 to the returning list.
    Return dummy head's next node.

Note: that we use a dummy head to simplify the code. Without a dummy head, you 
would have to write extra conditional statements to initialize the head's value.

'''

### Complexity Analysis ### 

'''
Time Complexity: O(max(m,n)). Assume that m and n represents the length of l1 
and l2 respectively, the algo below iterates at most max(m, n) times.

Space Complexity: O(max(m,n)). The length of the new list is at most max(m,n) +1
'''

### Solution ### 

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        result = ListNode(0)
        result_tail = result
        carry = 0
        
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)
            
            result_tail.next = ListNode(out)
            result_tail = result_tail.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        
        return result.next
