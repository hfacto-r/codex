#Find gcd of two numbers
#Euclid algorithm

def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a



