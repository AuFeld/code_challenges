 def hasCycle(self, head: ListNode) -> bool:
        # loop through the linked list 
        # look for the tail
            # if there is a tail, it's `next` is None 
            # how do we know when we've found the tail?
        
        # Idea 1: add a 'visited' property to each node as 
        # we traverse 
        # check to see if a node we're visiting has that 
        # property 
#         current = head 
        
#         while current is not None:
#             # check if the current node has the `visited` property
#             if hasattr(current, 'visited'):
#                 return True
            
#             current.visited = True
#             current = current.next 
#             # if we ever encounter a node with the 'visited', then
#             # we've been there before 
#             # or alternatively, set the `value` to None 
        
#         # we reached the end of the linked list 
#         return False
        
        # if we want to check the length of the list
        # how do we figure out the length? 
        # usually we'd figure out the length by traversing
        # until we got a node whose `next` is None
        # but if the linked list contains, we'd never get there 
        
        # What if we aren't allowed to mutate the linked list? 
        # Idea 2: Add the nodes to a set/hash table that keeps 
        # track of  nodes in the linked list we've visited 
        # as we traverse, we'll check if the current node 
        # is one we've visited before 
        # if it is, there must be a cycle, return True 
        
        # Idea 3: Traverse the linked list with two pointers,
        # one that moves at twice the speed of the other 
        # if there is a cycle in the list, then the faster 
        # runner will reach the end of the linked list 
        # otherwise, if there is a cycle, then the faster 
        # runner will lap the slower runner 
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            # increment the two pointers 
            fast = fast.next.next
            slow = slow.next 
            
            # check to see if they ever land on the same node 
            if fast is slow:
                return True
        
        # fast reached the end of the linked list 
		return False