
def powerset(inputSet):
    res = []
    n = len(inputSet)

    def backtrack(start, subset):
        res.append(subset)
        for i in range(start, n):
            backtrack(i + 1, subset + [inputSet[i]])

    backtrack(0, [])
    return res
