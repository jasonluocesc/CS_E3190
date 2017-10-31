# coding: utf-8
def get_nth_smallest_value(array1, array2):
    """Find nth smallest value from union of 2 * n integers in time O(log n).

    To run doctests:
        python -m doctest -v solution.py
    >>> get_nth_smallest_value([1, 2, 3], [4, 5, 6])
    3
    >>> get_nth_smallest_value([1, 2, 4, 6], [3, 5, 7, 8])
    4
    >>> get_nth_smallest_value([-84, -79, -77, -65, -54, -53, -31, -11, -10, -7, -4, 10, 24, 25, 35, 69, 90], 
    ... [-100, -93, -78, -56, -55, -45, 1, 3, 16, 27, 50, 56, 64, 65, 70, 74, 100])
    -4
    >>> get_nth_smallest_value([-498, -489, -480, -465, -442, -429, -381, -372, -350, -297, -289, 
    ... -203, -199, -170, -139, -121, -106, -95, -89, -80, 24, 26, 66, 164, 175, 180, 
    ... 198, 220, 225, 243, 269, 271, 288, 311, 328, 335, 343, 392, 425, 439, 459],
    ... [-451, -433, -336, -247, -240, -215, -194, -172, -146, -142, -79, -65, 
    ... -41, -13, -4, 44, 57, 69, 92, 145, 148, 170, 191, 194, 195, 213, 241, 255, 259, 
    ... 261, 286, 291, 362, 377, 382, 424, 432, 461, 482, 490, 491])
    69

    Parameters
    ----------
    array1 : sorted list of int
    array2 : sorted list of int, same length as array1

    Returns
    -------
    val : int
        The nth smallest value in the union of the two lists, when both
        lists have length n.
    """
    # Write your code here.
    l1=len(array1)
    l2=len(array2)

    if l1>l2:
        array1, array2, l1, l2 = array2, array1, l2, l1
    if l1==0:
        return array2[l2//2]

    iMin=0
    iMax=l1
    half=(l1+l2)//2

    while iMin<=iMax:
        i=int((iMin+iMax)/2)
        j=half-i

        if  i<l1 and array2[j-1]>array1[i]:
            iMin=i+1

        elif i>0 and array1[i-1]>array2[j]:
            iMax=i-1

        else:
            if i==0:
                maxLeft=array2[j-1]
            elif j==0:
                maxLeft=array1[i-1]
            else:
                maxLeft=max(array1[i-1],array2[j-1])

            return maxLeft



