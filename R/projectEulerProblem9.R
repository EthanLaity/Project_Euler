for (a in 1:1000){
  for (b in 1:(1000-a)){
    for (c in 1:(1000-a-b)){
      if (a^2 + b^2 == c^2 && a + b + c == 1000){
        cat("The values are a =", a, ", b =", b, ", c =", c, ".")
        cat("\nThe product abc is, therefore,", a*b*c)
        return()
      }
    }
  }
}
