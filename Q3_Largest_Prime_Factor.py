N = 600851475143
n = 1
while N > 1: #Nが１以上のときwhileを回す　
    n += 2 #Nは奇数なのでNの素因数は奇数であることが分かる
    while N % n == 0:  #Nがnで割り切れなくなるまでwhileを回す
        N /= n  # N = N / n
print(n) #最終的なnが最大の素因数となる