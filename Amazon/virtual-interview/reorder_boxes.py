def reorder_boxes(boxes):
    boxes.sort()
    ans = list()
    for i in range(len(boxes) - 1, -1, -2):
        if i - 1 >= 0:
            ans.append(boxes[i] + boxes[i - 1])
        else:
            ans.append(boxes[i])
    return ans

print(reorder_boxes([1, 2, 3, 4, 5, 6, 7]))
