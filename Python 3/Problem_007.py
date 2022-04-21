# Problem 7

target = 10001
count = 1

try:
    for prime in range(2,1000000):
        # print(prime)
        # print("Flag 1")
        prime_test = 0
        for num in range(1,prime):
            # print("Flag 2")
            if num == 1:
                # print("Flag 3")
                pass
            elif (prime % num) == 0:
                # print("Flag 4")
                break
            else:
                # print("Flag 5")
                prime_test += 1
                if prime_test == (prime - 2):
                    # print("Flag 6")
                    print("Prime: {}, # of primes: {}.".format(prime, count))
                    count += 1
                    if count == target:
                        # print("Flag 7")
                        print("The {}th prime number is {}.".format(target, prime))
                        raise StopIteration
except StopIteration:
    pass
