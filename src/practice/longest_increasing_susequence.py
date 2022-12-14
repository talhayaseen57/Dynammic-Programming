def lis(A):
    """
    It returns the length of longest increasing subsequence in the array.
    """
    L = [1] * len(A)
    for i in range (1, len(L)):
        subproblems = [L[k] for k in range(i) if A[k]<A[i]]
        L[i] = 1 + max(subproblems, default=0)

    return max(L, default=0)

if __name__ == "__main__":
    array = [5,2,8,6,3,6,9,5]
    result = lis(array)
    print(result)
    