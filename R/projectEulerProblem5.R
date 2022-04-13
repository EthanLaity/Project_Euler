iteration = 0
stop = FALSE

while (stop == FALSE) {
  iteration = iteration + 2*3*5*7*11*13*17*19
  if (iteration%%1000000 == 0) {
    print(iteration)
  }
  if (all(iteration%%(1:20) == integer(20))) {
    print(iteration)
    stop = TRUE
  }
}










