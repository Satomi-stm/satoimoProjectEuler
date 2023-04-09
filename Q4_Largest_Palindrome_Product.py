# for i in range(1000):
#     for j in range(1000):
#         num = i * j 

#         halfLengthNum = len(num) // 2

#         for k in range(halfLengthNum)

max_ans = 0
for i in range(100, 1000):
    for j in range(i,1000):
        num = i * j
        num_str = str(num)
        if num_str == num_str[::-1] and num > max_ans:
            max_ans = num

print(max_ans)



