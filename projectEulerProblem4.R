palindromes = c()
counter = 0

for (i in 999:100) {
  for (j in 999:100) {
    num = i * j
    
    step1 <- num%%100000
    step2 <- num%%10000
    step3 <- num%%1000
    step4 <- num%%100
    step5 <- num%%10
    
    h.thou <- num - step1
    t.thou <- step1 - step2
    thou <- step2 - step3
    huns <- step3 - step4
    tens <- step4 - step5
    ones <- step5
    
    rev = ones*100000 + tens*1000 + huns*10 + thou*0.1 + t.thou*0.001 + 
      h.thou*0.00001
    
    if (num == rev) {
      counter = counter + 1
      palindromes[counter] <- num
    }
  }
}

max(palindromes)




