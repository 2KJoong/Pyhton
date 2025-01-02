#아나콘다에서 실행

# List 안에 Tuple
a = [1,2,3,4]
b = [11,22,33,44]
[(i,j) for i,j in zip(a,b)]

# List 안에 List
a = [1,2,3,4]
b = [11,22,33,44]
[[i,j] for i,j in zip(a,b)]

# List 안에 Dictionary
a = [1,2,3,4]
b = [11,22,33,44]
[{i:j} for i,j in zip(a,b)]

a = [1,2,3,4]
b = [11,22,33,44]
x=[{i:j} for i,j in zip(a,b)]
for i in x :
    try :
        print(i[1])
    except :
        print('key 가 없어요')

list(map(lambda x: x*2 , [1,2,3,4]))

list(map(lambda x: {'홍길동'+str(x):x} , [1,2,3,4]))

def f(u,k):
    assert(callable(k))
    return k(u)

def rr(x) : return x+4
def kk(x) : return x*4

f(4,rr)

x_23 = f(23, lambda x : x+4)
x_23

list(map(lambda x:x(3), [lambda i:i+1, rr,kk]))