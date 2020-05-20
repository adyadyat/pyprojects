for i in range(1,8):
  for j in range(1,8):
    if ( (i==j) | (i==(8-j) ) ):
      print("x", end="");
    else:
      print(" ", end="");
  print();