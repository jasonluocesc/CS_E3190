def find_max_subsequence(a):
    length = len(a)
    start,end, temp = 0, 0, 0
    max_sum = a[0]
    max_now = a[0]
    for j in range(1,length):
        if max_now <= 0:
            max_now = a[j]
            temp = j
        else:
            max_now = max_now + a[j]
            if max_now > max_sum:
                max_sum = max_now
                end = j
                start = temp
    print(max_sum)
    return a[start: end+1]


A = [20,40,-70,3,5]
result = find_max_subsequence(A)
print(result)