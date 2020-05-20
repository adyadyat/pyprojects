prob1="";
prob2="";



print("enter number:", end="");
a = int(input());

for i in range(1,a+1):
  if (i%2!=0):
    print(prob1, end="");
  if (i%2==0):
    print(prob2, end="");

  print(i, end="");
  prob1+="-";
  prob2+="+";


  print();
