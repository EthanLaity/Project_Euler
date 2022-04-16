# Problem 4

pal = 0

for i in range(999,99,-1):
    for j in range(999,99,-1):
        num = i * j
        digits = len(str(num))
        if (digits % 2) != 0:
            # compare digit 1 to digit len(str(num)), 2 to digit len(str(num))-1
            array = [None] * digits
            k = digits - 1
            while k >= 0:
                array[k] = str(num)[k]
                k -= 1
            if digits == 1:
                pass            
            elif array[digits-1] == array[0]:
                if digits == 3:
                    pass
                elif digits == 5:
                    if array[digits-2] == array[1]:
                        if num > pal:
                            pal = num
                            # print("New largest palindrome! {} is the largest palindrome found so far!".format(pal))
                        # print("Palindrome found! {} is a palindrome!\n".format(num))
        else:
            # compare digit 1 to digit len(str(num)), 2 to digit len(str(num))-1, 3 to digit len(str(num))-2
            array = [None] * digits
            k = digits - 1
            while k >= 0:
                array[k] = str(num)[k]
                k -= 1
            if digits == 2:
                pass
            elif array[digits-1] == array[0]:
                if digits == 4:
                    pass
                elif digits == 6:
                    if array[digits-2] == array[1]:
                        if array[digits-3] == array[2]:
                            if num > pal:
                                pal = num
                                # print("New largest palindrome! {} is the largest palindrome found so far!".format(pal))
                            # print("Palindrome found! {} is a palindrome!\n".format(num))
                            
print("The largest palindrome found is {}.".format(pal))