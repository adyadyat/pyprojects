wd = 1
d = 1
week = 1
sw = 0
for i in range(1,91):
  if sw == 0:
  	print(week, end=" ")
  	week += 1
  	sw = 1
  if (d<10):
    print(" " ,end="")
  if (wd == 1):
    print("{", end="")
  if (wd==6): 
    print("[", end="")
  if (d%7==0):
    print("(", end="")

  print(d ,end="")
  
  if (wd == 1):
    print("}", end="")
  if (wd==6): 
    print("]", end="")
  if (d%7==0):
    print(")", end="")
    sw = 0
  
  print(" " , end="")
  
  if (d%7==0):
    print()
    wd=0

  d=d+1
  wd=wd+1

  if (d%31==0):
    print()
    d=1
    wd=1
    sw = 0
    week = 1
"""
1 {1}  2  3  4  5  [6]  (7) 
2 {8}  9 10 11 12 [13] (14) 
3{15} 16 17 18 19 [20] (21) 
4{22} 23 24 25 26 [27] (28) 
5{29} 30 
 
"""