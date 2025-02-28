class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        # Step 1: Find the LCS using DP
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
    
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
        # Step 2: Reconstruct the shortest supersequence
        i, j = m, n
        result = []
    
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])  # Add the common character once
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                result.append(str1[i - 1])  # Add the character from str1
                i -= 1
            else:
                result.append(str2[j - 1])  # Add the character from str2
                j -= 1
    
        # Add remaining characters from str1 or str2
        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        while j > 0:
            result.append(str2[j - 1])
            j -= 1
    
        # Reverse the result to get the correct order
        return ''.join(reversed(result))
        