def amount(A, S):

    A.sort()

    def backtrack(remain, comb, start):
        if remain == 0:
            result.append(list(comb))
            return
        elif remain < 0:
            return

        for i in range(start, len(A)):
            if i > start and A[i] == A[i - 1]:
                continue
            comb.append(A[i])
            backtrack(remain - A[i], comb, i + 1)
            comb.pop()

    result = []
    backtrack(S, [], 0)
    return result
