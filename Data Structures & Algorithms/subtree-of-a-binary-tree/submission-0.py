class Solution:
    def isSubtree(self, root, subRoot):
        if not root:                      # ran out of places to look
            return False
        if self.sameTree(root, subRoot):  # does the match start here?
            return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def sameTree(self, a, b):
        if not a and not b:               # both ended together
            return True
        if not a or not b:                # one ended early, shapes differ
            return False
        if a.val != b.val:
            return False
        return (self.sameTree(a.left, b.left) and
                self.sameTree(a.right, b.right))