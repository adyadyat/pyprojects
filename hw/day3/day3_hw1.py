sw = 0
sw1 = 0
for i in range(1,32):
  if (i<10):
    if (i<5):
      print(" " ,end="")
    if (i>6):
      print(" " ,end="")
  if (i == 5):
      print(" " ,end="")
      print("{", end="")
  if (i == 6):
      print(" " ,end="")
      print("[", end="")
  if (i > 5):
    sw += 1
    if (sw % 7 == 0):
      print("{", end="")
  if (i > 6):  
    sw1 += 1
    if (sw1 % 7 == 0):
      print("[", end="")
  if (i%7==0):
    print("(", end="");

  print(i ,end="");

  if (i > 5):
    if (sw % 7 == 0):
      print("}", end="")
      sw = 0
  if (i == 5):
      print("}", end="")
  if (i == 6):
      print("]", end="")
  if (i > 6):  
    if (sw1 % 7 == 0):
      print("]", end="")
      sw1 = 0
  if (i%7==0):
    print(")", end="");
    
  print(" " , end="")
  
  if (i%7==0):
    print();
'''
 1  2  3  4  {5}  [6]  (7) 
 8  9 10 11 {12} [13] (14) 
15 16 17 18 {19} [20] (21) 
22 23 24 25 {26} [27] (28) 
29 30 31
'''
