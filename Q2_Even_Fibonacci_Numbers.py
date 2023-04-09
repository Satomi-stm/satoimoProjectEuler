
num1 = 1 #数列の第一項目
num2 = 2 #数列の第二項目

#結果として出す合計を入れる変数
s = 0

#項の値の上限
t = 4000000
while s <= t:
    if num2 % 2 == 0: #第一項目以外のどの値もnum2になる
        s += num2

    copy = num1 #num1の値を保存
    num1 = num2 #num1にnum2を代入　num1を指す項が一つ右にずれた
    num2 += copy #num2の値を更新

print(s)





