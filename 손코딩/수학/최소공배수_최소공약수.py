n, m = map(int,input().split())

# 최대 공약수
def gcd(x,y):
    while (y):
        x, y = y, x%y
    return x 

# 최소 공배수
def lcm(x,y):
    return (x*y)// gcd(x,y)