wd =1
d = 1;
for i in range(1,91):
  if (d<10):
    print(" " ,end="");
  
  if (wd==6): 
    print("[", end="");
  if (d%7==0):
    print("(", end="");
  
  print(d ,end="");
  

  if (wd==6): 
    print("]", end="");
  if (d%7==0):
    print(")", end="");
  
  print(" " , end="")
  
  if (d%7==0):
    print();
    wd=0;

  d=d+1;
  wd=wd+1;
  
  if (d%31==0):
    print();
    d=1;


