# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=444568&highlight=%B9%B7%2B%C3%E6


from heapq import heappop, heappush


# class MaxHeapObj(object):
#   def __init__(self,val): self.val = val
#   def __lt__(self,other): return self.val > other.val
#   def __eq__(self,other): return self.val == other.val
#   def __str__(self): return str(self.val)
#
# class MinHeap(object):
#   def __init__(self): self.h = []
#   def heappush(self,x): heappush(self.h,x)
#   def heappop(self): return heappop(self.h)
#   def __getitem__(self,i): return self.h[i]
#   def __len__(self): return len(self.h)
#
# class MaxHeap(MinHeap):
#   def heappush(self,x): heappush(self.h,MaxHeapObj(x))
#   def heappop(self): return heappop(self.h).val
#   def __getitem__(self,i): return self.h[i].val


def solve(seats):

    l = -1
    memo = list()
    while l < len(seats):
        if l == -1 or seats[l] == 1:
            r = l + 1
            while r < len(seats) and seats[r] == 0:
                r += 1
            length = r - l - 1
            if length > 0:
                heappush(memo, (-length, l, r))
            l = r
        else:
            l += 1

    ans = list()
    while memo:
        length, l, r = heappop(memo)
        length *= -1
        if l < 0:
            mid = 0
        elif r >= len(seats):
            mid = len(seats) - 1
        else:
            mid = (l + r) // 2
        ans.append(mid)
        length_left = mid - l - 1
        if length_left > 0:
            heappush(memo, (-length_left, l, mid))
        length_right = r - mid - 1
        if length_right > 0:
            heappush(memo, (-length_right, mid, r))

    return ans


ans = solve([0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0])
print(ans)