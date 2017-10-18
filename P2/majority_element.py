#Write a program that finds if an element array A contains a majority element, i.e. an element that appears more than n/2 times in A,
# where n is the length of the array A. In case a majority element cannot be found, return None.
# Suppose that the elements of A do not necessarily come from an ordered domain, and so they can only be tested for equality ("is A[i]=A[j]?"),
# but not compared ("is A[i]>A[j]?"). Use a divide-and-conquer algorithm that runs in time O(nlog⁡n).

def majority_element(A):
    length = len(A)

    if length==2:
        if(A[0]==A[1]):
            return A[0]
        else:
            return -1

    elif length==1:
        return A[0]

    elementL = majority_element(A[:length//2])
    elementR = majority_element(A[length//2:])

    if (elementL == -1 and elementR >= 0):
        return elementR;
    elif (elementR == -1 and elementL >= 0):
        return elementL;

    if (elementL == elementR):
        return elementL;
    else:
        return -1;



A=[1,2,2,3,3,2,2,2]
print(majority_element(A))