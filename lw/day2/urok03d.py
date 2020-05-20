prob1="";
prob2="";

sw=0;

print("enter number:", end="");
a = int(input());

for i in range(1,a+1):
  print(i, end="");
  print("-", end="");
  print(sw, end="");

  if sw==0:
    sw=1;
  else:
    sw=0;




  print();
