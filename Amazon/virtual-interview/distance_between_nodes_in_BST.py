class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def distance_between_nodes_in_BST(root, val1, val2):
    # find LCA
    level_LCA = 0
    val_min = min(val1, val2)
    val_max = max(val1, val2)
    p_LCA = root
    while p_LCA:
        if p_LCA.val < val_min:
            p_LCA = p_LCA.right
            level_LCA += 1
        elif p_LCA.val > val_max:
            p_LCA = p_LCA.left
            level_LCA += 1
        elif val_min <= p_LCA.val <= val_max:
            break

    # find val_min
    level_valMin = level_LCA
    p_valMin = p_LCA
    while p_valMin:
        if p_valMin.val == val_min:
            break
        elif p_valMin.val < val_min:
            p_valMin = p_valMin.right
            level_valMin += 1
        else:
            p_valMin = p_valMin.left
            level_valMin += 1

    # find val_max:
    level_valMax = level_LCA
    p_valMax = p_LCA
    while p_valMax:
        if p_valMax.val == val_max:
            break
        elif p_valMax.val < val_max:
            p_valMax = p_valMax.right
            level_valMax += 1
        else:
            p_valMax = p_valMax.left
            level_valMax += 1

    return level_valMin + level_valMax - 2 * level_LCA


r1 = Node(8)
r2 = Node(4)
r3 = Node(12)
r4 = Node(2)
r5 = Node(6)
r6 = Node(10)
r7 = Node(14)
r8 = Node(1)
r9 = Node(3)
r1.left = r2
r1.right = r3
r2.left = r4
r2.right = r5
r3.left = r6
r3.right = r7
r4.left = r8
r4.right = r9
print(distance_between_nodes_in_BST(r1, 1, 14))