#Write a program that gives the nth smallest element in the union of two sorted arrays of size n, A[1,…,n] and B[1,…,n].
# Use a divide-and-conquer algorithm that runs in time O(logn).
# (Modification of Exercise 2.22 in Dasgupta et al. "Algorithms")

def nth_smallest(A,B,n):
    if len(A)==0:
        return B[n]
    elif len(B)==0:
        return A[n]

    midA=len(A)//2
    midB=len(B)//2
    if midA+midB<n:
        if A[midA]>B[midB]:
            return nth_smallest(A,B[midB+1:],n-midB-1)
        else:
            return nth_smallest(A[midA+1:],B,n-midA-1)
    else:
        if A[midA]>B[midB]:
            return nth_smallest(A[:midA],B,n)
        else:
            return nth_smallest(A,B[:midB],n)

A=[1,2,3]
B=[6,7,8,11]
n=6
print(nth_smallest(A,B,n))