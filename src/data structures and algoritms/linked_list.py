class SinglyLinkedList:
    """Implement a singly linked list node."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def traverse(self, head):
        """Traverse through a linked list.

        Args:
            head: The beginning node of traversal.

        """
        current = head
        data = []
        while current:
            data.append(current.data)
            current = head.next
        return data
