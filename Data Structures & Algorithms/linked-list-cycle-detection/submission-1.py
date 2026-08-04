# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}

        curr = head
        while curr:
            if visited.get(curr, 0) > 0:
                return True
            visited[curr] = 1
            curr = curr.next
        return False