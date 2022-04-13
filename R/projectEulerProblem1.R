n = 1000
sum = 0

for (i in 1:(n-1))
{
  if (i%%3==0){
    sum <- sum + i
  } else if (i%%5==0) {
    sum <- sum + i
  }
}

sum

