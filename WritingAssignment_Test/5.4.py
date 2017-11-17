

def subset_sum(input, sum):
    input_size = len(input)
    result = [[False for x in range(sum+1)] for y in range(input_size)]

    for i in range(0, sum+1):
        if input[0] == i:
            result[0][i] = True
        else:
            result[0][i] = False
    for j in range(0, input_size):
        result[j][0] = True
    for i in range(1, input_size):
        for j in range(1, sum+1):
            if j < input[i]:
                result[i][j] = result[i-1][j]
            else:
                result[i][j] = result[i-1][j] or result[i-1][j - input[i]]
    return result[-1][-1]


set1 = [1, 2, 3, 4]
sum1 = 10
print(subset_sum(set1, sum1))