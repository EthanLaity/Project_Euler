x = vector(length = 10001)
number = 1
primes = 0
x[1] = 2

while (x[10001] == 0) {
  number = number + 1
  if (all(number%%x[c(1:primes)], vector(length=sum(x != 0))+number) || number == 2) {
    primes = primes + 1
    x[primes] <- number
    if (primes < 10 || primes%%500 == 0) {
      cat("Currently found", primes, "prime numbers. The last prime found was", number, "\n")
    }
  }
}

cat("DING DING DING!!! \nThe 10,001st prime number is", x[10001])
