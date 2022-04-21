# ! pip install python-math

import math

def sumPrimes(maxPrime):
    try:
        sumPrime = 0
        for x in range(2,maxPrime):
            for y in range(2,int(math.sqrt(x))+1):
                if (x % y == 0):
                    break
            else:
                # print(x)
                sumPrime += x
        
    except Exception as e:
        print(type(e))
        
    return sumPrime
        
def main():
    maxPrime = 2* 10**6
    sumPrime = sumPrimes(maxPrime)
    print("The sum of all the primes below {} is {}".format(maxPrime, sumPrime))
        
if __name__ == "__main__":
    main()
