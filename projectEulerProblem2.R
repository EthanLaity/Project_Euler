maxVal = 4000000
x = c()
x[1] = 1
x[2] = 2
sum = 0
count = 3

for (i in length(x)) {
  if (x[i]%%2 == 0) {
    sum <- sum + x[i]
  }
}


repeat {
  x[count] <- x[count-1] + x[count-2]
  if (x[count] > maxVal) {
    break
  }
  if (x[count]%%2 == 0) {
    sum <- sum + x[count]
  }
  count <- count + 1
}

sum
