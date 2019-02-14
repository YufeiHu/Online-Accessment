class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_sum_from_root_to_leaves(root):
    if not root: return 0
    left = max_sum_from_root_to_leaves(root.left)
    right = max_sum_from_root_to_leaves(root.right)
    return max(left, right) + root.val


r1 = Node(1)
r2 = Node(2)
r3 = Node(3)
r4 = Node(4)
r5 = Node(5)
r1.left = r2
r1.right = r3
r2.left = r4
r2.right = r5
print(max_sum_from_root_to_leaves(r1))