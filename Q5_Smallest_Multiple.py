# 2520 は 1 から 10 の数字の全ての整数で割り切れる数字であり, そのような数字の中では最小の値である.

# では, 1 から 20 までの整数全てで割り切れる数字の中で最小の正の数はいくらになるか.

#gcdとは最大公約数
#lcmとは最小公倍数

import math

#lcm(最小公倍数)をもとめる関数を作る
# a*b / aとbの最大公約数 = aとbの最小公倍数
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def find_lcm_of_range(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result


smallest_number = find_lcm_of_range(20)
print(smallest_number)

def isDivisible1to20(num):
    for i in range(1,21):
        if number % i != 0:
            return False
    return True

#１から２０までの数字である数字が割り切れるかをみる
number = 1
while True:
    if isDivisible1to20(number):
        break
    number += 1 #インクリメント

#答えをみつけたらストップする
print(number)