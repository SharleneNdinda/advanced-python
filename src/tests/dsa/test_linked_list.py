from unittest import TestCase

from dsa.linked_list import SinglyLinkedList
from dsa.linked_list import traverse_and_print


class TestSinglyLinkedList(TestCase):
    """Test singly linked list functionality."""

    def setUp(self):
        """Setup test environment."""
        self.node1 = SinglyLinkedList(12)
        self.node2 = SinglyLinkedList(31)

    def test_traverse_and_print(self):
        """Test traversing and printing data."""
        self.node1.next = self.node2
        traverse = traverse_and_print(self.node1)
        assert traverse == []
