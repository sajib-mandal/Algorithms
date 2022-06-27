# sourch: https://github.com/harishvc/challenges/blob/master/longest-common-subsequence.py

# Find length of the LCS
def LCS_Length(X, Y):
    m = len(X)
    n = len(Y)
    C = [[0 for j in range(n + 1)] for i in range(m + 1)]
    longest = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                tmp = C[i - 1][j - 1] + 1
                C[i][j] = tmp
                if (tmp > longest):
                    longest = tmp
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])
    return longest


# Print two dimensional matrix
def PrintMatrix(Table):
    for row in range(0, len(Table)):
        for col in range(0, len(Table[row])):
            print("%d" % (Table[row][col]), end=" ")
        print("")


# Time Complexity: O(mn), Space Complexity: O(mn)
def LCS(X, Y):
    m = len(X)
    n = len(Y)
    # An (m+1) times (n+1) matrix
    C = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])
    return C


# Traverse the two dimensional matrix to find one LCS
def backTrack(C, X, Y, i, j):
    if i == 0 or j == 0:
        return ""
    elif X[i - 1] == Y[j - 1]:
        return backTrack(C, X, Y, i - 1, j - 1) + X[i - 1]
    else:
        if C[i][j - 1] > C[i - 1][j]:
            return backTrack(C, X, Y, i, j - 1)
        else:
            return backTrack(C, X, Y, i - 1, j)


# Traverse the two dimensional matrix to find all LCS
def backTrackAll(C, X, Y, i, j):
    if i == 0 or j == 0:
        return set([""])
    elif X[i - 1] == Y[j - 1]:
        return set([Z + X[i - 1] for Z in backTrackAll(C, X, Y, i - 1, j - 1)])
    else:
        R = set()
        if C[i][j - 1] >= C[i - 1][j]:
            R.update(backTrackAll(C, X, Y, i, j - 1))
        if C[i - 1][j] >= C[i][j - 1]:
            R.update(backTrackAll(C, X, Y, i - 1, j))
        return R


X = "ABCBDAB"
Y = "BDCABA"

m = len(X)
n = len(Y)
C = LCS(X, Y)
print("Input strings => %s  %s" % (X, Y))
print("Max LCS: %d" % LCS_Length(X, Y))
print("Some LCS: %s" % backTrack(C, X, Y, m, n))
print("All LCSs: %s" % backTrackAll(C, X, Y, m, n))
