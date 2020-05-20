prob1="";
prob2="";

sw=-1;

print("enter number:", end="");
a = int(input());

for i in range(1,a+1):
  # print(sw, end="")
  print(prob1, end="")
  # print(" ", end="")
  print(i, end="");
  if sw>0:
    prob1+="+"
  else:
    prob1+="-"
  sw=sw*-1;



  print();
