for i in range(1,9):
  for j in range(1,9):
    if (i%2!=0):
      if (j%2!=0 ):
        print("x", end="");
      else:
        print(" ", end="");
    else:
      if (j%2==0 ):
        print("x", end="");
      else:
        print(" ", end="");

  print();


