# Problem 3

num = 600851475143
max_it = num

begin = 1

new_factor = 0
old_factor = 0

while True:
    for i in range(begin,max_it+1):
        # print('Current divisor is {}'.format(i))
        # print("Flag1")
        if i == 1:
            print('As current divisor is {}, no division was attempted\n'.format(i))
            # print("Flag2")
            pass
        elif begin > max_it+1:
            print('Current divisor is {}, exiting operation as this is not a possible divisor\n'.format(i))
            # print("Flag3")
            break
        elif (num % i) == 0:
            print('Current divisor is {}, which is a successful factor!'.format(i))
            # print("Flag4")
            print(i)
            new_factor = i
            for j in range(2,int(new_factor)-1):
                if (new_factor % j) == 0:
                    print("{} is NOT a prime! Divisible by {}. Try again :)\n".format(int(new_factor), j))
                    break
            else:
                if new_factor > old_factor:
                    old_factor = new_factor
                    print("{} IS a prime! Keep searching! :)\n".format(old_factor))
        else:
            # print('Confirmation that current divisor is {}'.format(i))
            # print("Flag5")
            max_it = num / i
            max_it = round(max_it)
            begin = i+1
            # print('Since 600851475143 is not divisible by {}, then we will reduce the search ceiling to {} and restart our search at {} \n'.format(i, max_it, begin))
            # print(num)
            # print(begin)
    break
    
print("The largest prime factor of the number {} is {}.\n\n".format(num, old_factor))
