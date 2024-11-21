"""
Stack dataclass
"""

from typing import Any


class Stack:
    """Stack dataclass (including methods)"""
    _items: list

    def __init__(self) -> None:
        """Initialize a new empty stack."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items."""
        return self._items == []

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack"""
        assert not self.is_empty()
        return self._items.pop()

    def top(self) -> Any:
        """Return the top-most element in stack (other name: peek())"""
        assert not self.is_empty()
        return self._items[len(self._items) - 1]
