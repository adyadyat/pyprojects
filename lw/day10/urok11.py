for i in range(1,9):
  for j in range(1,9):
    if ( (i==1) | (i==8) | (j==1) | (j==8)):
      print("x", end="");
    else:
      print(" ", end="");
  print();