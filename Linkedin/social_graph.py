from collections import defaultdict


def socialGraphs(counts):

    memo = defaultdict(list)
    for i, count in enumerate(counts):
        memo[count].append(i)

    results = list()
    for key, value in memo.items():
        ansCur = list()
        cnt = 0
        for val in value:
            ansCur.append(val)
            cnt += 1
            if cnt == key:
                cnt = 0
                results.append(ansCur)
                ansCur = list()
        if ansCur:
            results.append(ansCur)

    for result in sorted(results):
        result = map(str, result)
        print(' '.join(result))


socialGraphs([2, 10, 2, 2, 10])