from tree import Tree


class TreeImplementation(Tree):
    def insert(self, value: int) -> None:
        """
        Insert a value into the tree. Does nothing if the value is already in
        the tree.
        """
        if value < self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)

    def contains(self, value: int) -> bool:
        """
        Check if the tree contains a value.
        """
        if value == self.value:
            return True
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.contains(value)
        else:
            if self.left is None:
                return False
            return self.right.contains(value)  

    def remove(self, value: int) -> None:
        """
        Remove a value from the tree. Raises a KeyError if the value is not
        in the tree, or a ValueError if the removal would result in an empty
        tree.
        """
        if value == self.value:
            if self.left is None and self.right is None:
                raise ValueError("Cannot remove root from tree with no children")
            elif self.left is None:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
            elif self.right is None:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
            else:
                self.value = self.left.max_value()
                self.left.remove(self.value)
        elif value > self.value:
            if self.right is None:
                raise KeyError("Value not in tree")
            self.right.remove(value)
        else:
            if self.left is None:
                raise KeyError("Value not in tree")
            self.left.remove(value)

    def min_value(self) -> int:
        """
        Return the minimum value in the tree.
        """
        if self.left is None:
            return self.value
        return self.left.min_value()
    
    def max_value(self) -> int:
        """
        Return the maximum value in the tree.
        """
        if self.right is None:
            return self.value
        return self.right.max_value()

    def inorder_traversal(self) -> list[int]:
        """
        Return the inorder traversal (left, root, right) of the tree as a list.
        """

        left = []
        mid = [self.value]
        right = []
        
        if self.left is not None:
            left = self.left.inorder_traversal()
        if right is not None:
            right = self.right.inorder_traversal()


        return left + mid + right 
