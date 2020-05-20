for i in range(1,32):
  if (i<10):
    print(" " ,end="");
  
  if (i%7==0):
    print("(", end="");
  
  print(i ,end="");
  
  if (i%7==0):
    print(")", end="");
  
  print(" " , end="")
  
  if (i%7==0):
    print();