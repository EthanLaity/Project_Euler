# Problem 6

# Consider first "x" natural numbers
x = 100

# Calculate square of sum
sq_of_sum = (sum(range(1,x+1)))**2

# Calculate sum of squares
sum_of_sq = 0
for i in range(1,x+1):
    sum_of_sq += i**2
    
# Find difference
soln = sq_of_sum - sum_of_sq

print("Therefore, the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is {}".format(soln))
