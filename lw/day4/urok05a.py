pool = 600;
pump1=3;
pump1_time=0;
while pool >=200:
  print(pool, end="");
  print(" - ", end="");
  print(pump1_time, end="");
  pool=pool-pump1;
  pump1_time = pump1_time+1;
  print();