#Let A[1,…,n] be a sorted array of distinct integers. Write a program that finds out whether there is an index i for
# which A[i]=i. If there is more than one such index i, it suffices to return only one
# of them. Use a divide-and-conquer algorithm that runs in time O(logn).
# (Exercise 2.17 in Dasgupta et al. "Algorithms")

def find_pair(A):
    length = len(A) // 2
    print("length=",length)
    if length==0:
        print("No index")
        return 0
    elif A[length]==length:
        print(length)
        return length
    elif A[length] > length:
        return find_pair(A[0:length])
    elif A[length]< length:
        return find_pair(A[length:])


A=[-1,0,2,3]
find_pair(A)



