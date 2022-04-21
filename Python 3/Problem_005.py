max_number = 20
smallest_combo = 20*19*17*13*11*7*3
i = smallest_combo
count = 0
seq = []

while count < max_number:
    for x in range(1,max_number+1):
        if (i % x) == 0:
            # print("{} is divisible by {}".format(i, x))
            count += 1
            pass
        else:
            count = 0
            break
    i += smallest_combo
    
print("Therefore, the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {}.".format(i))
