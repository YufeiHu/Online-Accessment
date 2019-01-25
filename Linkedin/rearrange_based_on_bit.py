def numOnes(n):
    
    ans = 0
    while n:
        if n % 2 == 1:
            ans += 1
        n = n >> 1
    return ans


def rearrange(elements):
    
    memo = list()
    for val in elements:
        memo.append(numOnes(val))

    elements = [x for _, x in sorted(zip(memo, elements))]
    memo = sorted(memo)

    i = 0
    while i < len(memo) - 1:
        if memo[i] == memo[i + 1]:
            j = i + 1
            while j < len(memo) and memo[i] == memo[j]:
                j += 1
            elements[i:j] = sorted(elements[i:j])
            i = j
        else:
            i += 1

    return elements


print(rearrange([7, 8, 18, 6, 14, 36, 18]))