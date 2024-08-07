def dna_match_topdown(DNA1, DNA2):

    memo = {} # to store values

    def dp (a, b):

        if (a,b) in memo:

            return memo[(a,b)]
        
        if a == len(DNA1) or b == len(DNA2):
            return 0
        
        if(DNA1[a] == DNA2[b]):
            memo[(a,b)] = 1 + dp(a+1, b+1)

        else:
            memo[(a,b)] = max(dp(a+1, b), dp(a, b+1))
        
        return memo[(a,b)]
    return dp(0,0)


def dna_match_bottomup(DNA1, DNA2):
    
    m, n = len(DNA1), len(DNA2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    max_len = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if DNA1[i-1] == DNA2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            max_len = max(max_len, dp[i][j])

    return max_len