# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=444460&highlight=%B9%B7%2B%C3%E6


from math import ceil


def check(target, original):
    t = 0
    for o in range(len(original)):
        if target[t] == original[o]:
            t += 1
        if t == len(target):
            return True
    return False


def solve(target, original):
    target_set = set(list(target))
    original_set = set(list(original))
    if not original_set.issuperset(target_set):
        return -1

    # preprocess original to speed up
    original_new = ""
    for char in original:
        if char in target_set:
            original_new += char

    minRepeat = int(ceil(len(target) * 1.0 / len(original_new)))
    maxRepeat = len(target)
    reconstruct = original_new * minRepeat
    for k in range(minRepeat, maxRepeat + 1):
        if check(target, reconstruct):
            return k
        reconstruct += original_new

    return -1


ans = solve("ZAZZZAAAAZZAZ", "BAZ")
print(ans)