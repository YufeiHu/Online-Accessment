def helper_other(cards, i, memo):

    if i == len(cards) - 1: return cards[i]
    if i == len(cards) - 2: return max(cards[i] - cards[i + 1], cards[i] + cards[i + 1])
    if i == len(cards) - 3:
        ans1 = cards[i] - max(cards[i + 1] - cards[i + 2], cards[i + 1] + cards[i + 2])
        ans2 = cards[i] + cards[i + 1] - cards[i + 2]
        ans3 = cards[i] + cards[i + 1] + cards[i + 2]
        return max(ans1, ans2, ans3)
    if memo[i] > 0: return memo[i]

    ans1 = cards[i] - helper_other(cards, i + 1, memo)
    ans2 = cards[i] + cards[i + 1] + helper_other(cards, i + 2, memo)
    ans3 = cards[i] + cards[i + 1] + cards[i + 2] - helper_other(cards, i + 3, memo)
    memo[i] = max(ans1, ans2, ans3)
    return memo[i]


def cardGame_other(cards):
    """
    :type piles: List[int]
    :rtype: bool
    """
    memo = [0] * len(cards)
    sumCur = sum(cards)
    return (sumCur + helper_other(cards, 0, memo)) // 2


def helper(memo, cards, i):

    if i >= len(cards): return 0
    if i == len(cards) - 1: return cards[i]
    if i == len(cards) - 2: return max(cards[i], cards[i] + cards[i + 1])
    if i == len(cards) - 3:
        ans1 = cards[i] + min(cards[i+2], 0)
        ans2 = cards[i] + cards[i+1]
        ans3 = cards[i] + cards[i+1] + cards[i+2]
        memo[i] = max(ans1, ans2, ans3)
        return memo[i]
    if i in memo: return memo[i]

    ans1 = cards[i] + min(helper(memo, cards, i + 2), helper(memo, cards, i + 3), helper(memo, cards, i + 4))
    ans2 = cards[i] + cards[i+1] + min(helper(memo, cards, i + 3), helper(memo, cards, i + 4), helper(memo, cards, i + 5))
    ans3 = cards[i] + cards[i + 1] + cards[i + 2] + min(helper(memo, cards, i + 4), helper(memo, cards, i + 5), helper(memo, cards, i + 6))
    memo[i] = max(ans1, ans2, ans3)
    return memo[i]


def cardGame(cards):
    """
    :type piles: List[int]
    :rtype: bool
    """
    memo = dict()
    ans1 = helper(memo, cards, 0)
    ans2 = sum(cards) - ans1
    return ans1, ans2


cards = [59, 48, 36, 70, 59, 93, 60, 98, 15, 32, 31, 13, 27, 14, 8, 17, 4, 76, 24, 47, 39, 81, 26, 6, 70, 73, 8, 36, 71, 19,
     66, 61, 86, 63, 97, 32, 15, 36, 68, 69, 32, 53, 83, 35, 100, 41, 44, 8, 28, 76, 39, 90, 37, 35, 11, 99, 48, 49, 64,
     74, 6, 54, 12, 99, 34, 47, 78, 36, 51, 26, 43, 83, 10, 68, 32, 48, 72, 54, 64, 64, 44, 62, 77, 60, 100, 84, 15, 24,
     95, 6, 6, 8, 24, 21, 84, 61, 75, 26, 63, 54]
print(cardGame(cards))
print(cardGame_other(cards))