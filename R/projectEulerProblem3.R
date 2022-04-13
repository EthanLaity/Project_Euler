start.time <- Sys.time()

num = 600851475143  
factorCounter = 0
x = c()
primeFactorCounter = 0
y = c()
solnCount = 0
primeFactors = c()

for (i in 1:floor(num/2)) {
  if (num%%i == 0) {
    factorCounter = factorCounter + 1
    x[factorCounter] = i
    print(i)
    ### The below loops were necessary to prevent the solution from taking ~11 
    ### hours to compute. Computation time reduced from ~11 hours (unfinished)
    ### to 0.063869 secs!!! The loops simply cut short the factor searching
    ### once a non-prime factor is found.
    if (length(x)>2){
      for (j in 2:(length(x)-1)) {
        if (x[factorCounter]%%x[j] == 0) {
          return()
        }
      }
    }
  }
}

for (i in 1:length(x)) {
  for (j in 2:length(x)) {
    if (x[i]%%x[j] == 0) {
      primeFactorCounter = primeFactorCounter + 1
      y[primeFactorCounter] = x[i]
    }
  }
}

for (i in 1:length(plyr::count(y)$freq)) {
  if (plyr::count(y)$freq[i] == 1) {
    solnCount = solnCount + 1
    primeFactors[solnCount] = plyr::count(y)$x[i]
  }
}

max(primeFactors)

end.time <- Sys.time()
time.taken <- end.time - start.time
time.taken
