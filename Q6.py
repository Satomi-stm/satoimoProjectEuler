#sum square differences
 
def sum_square_differences(n):

    #nの二乗を1~nまで足す
    sum_A = 0
    for i in range(1, n+1):
        sum_A += i**2

    #1~nを足し合わせた数の合計を二乗
    s = 0
    for i in range(1, n+1):
        s += i
    sum_B = s**2

    result = sum_B - sum_A

    return result

print(sum_square_differences(100))


