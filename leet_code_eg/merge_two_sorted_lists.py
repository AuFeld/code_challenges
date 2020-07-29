    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # should we copy the lists before doing anything
        # to them, or just mutate them directly? 
        
        # don't forget to check that the inputs are not None 
        
        # attach one of the lists to the end of the other list 
        # sort them 
        # Sorting incurs a runtime of O(n log n)
        # We wouldn't be able to use any built-in sorting methods 
        # So we'd have to implement it ourself 
​
        # What is the best possible we can achieve for this problem?
        # We traversed each list once? Can we do less work than that? 
        # O(n + m) is probably the best we can do as far as runtime is concerned 
        # Added each node to a new list 
        
        # Space complexity: We're creating an entirely new linked list to hold 
        # all of the values from our inputs lists
        # O(n + m) since we're copying each input ListNode 
        # Do we need to do this? 
        # Let's instead mutate one of the input lists 
        
        # init a new linked list 
        new_list = ListNode(None)
        # variable to keep track of where we are in the new list 
        current_new = new_list
        # keep track of the two current nodes, l1 and l2
        
        # traverse along both linked lists 
        while l1 is not None and l2 is not None:
            # compare the two values that l1 and l2 are referring to 
            # if l1.val == l2.val:
                # add both to our new list and increment both pointers 
            if l1.val <= l2.val:
                # take the smaller one and add it on to the end of a new linked list
                current_new.next = ListNode(l1.val)
                # update the new_list reference 
                l1 = l1.next
            else:
                current_new.next = ListNode(l2.val)
                l2 = l2.next
            current_new = current_new.next
                
        # once all of the nodes from one of the linked lists is added,
        # add all of the remaining nodes from the other list to the end of
        # the new linked list 
        # check l1 to see if it still has nodes 
        if l1 is not None:
            # add the rest of l1 to the end of our new list 
            current_new.next = l1
        # check l2 to see if it still has nodes 
        if l2 is not None:
            current_new.next = l2
            
        # return our new list - our initial dummy node 
        return new_list.next
    
        # Runtime for this strategy is O(n + m) where n and m are the lengths
        # of both linked lists 