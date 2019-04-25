def fib(n):
    j = 1
    k = 0
    
    for i in range(n):
        t = j + k
        k = j
        j = t
    
    print('fib({}) {}'.format(n, k))


n = int(input('Forneça um número: '))

for i in range(n):
    fib(i)

