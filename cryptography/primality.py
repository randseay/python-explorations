"""
Runs a primality test against passed-in values
"""
from sys import argv

def isPrime(n):
    return not (int(n) < 2 or any(int(n) % x == 0 for x in range(2, int(int(n) ** 0.5) + 1)))

def main():
    print([isPrime(argv[i]) for i in range(1, len(argv))])

if __name__ == '__main__' and len(argv) > 1:
    main()
else:
    print('No number given, please try again.')
