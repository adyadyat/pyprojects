import time;

pool = 600;
pump1=3;
pumph=9;
pumph_v=0;
pump1_time=0;
cycle=1
holod =0;
while pool >=200:
  print(pool, end="");
  print(" - ", end="");
  print(pump1_time, end="");
  print(" - ", end="");
  print(holod, end="");
  pool=pool-pump1;
  pump1_time = pump1_time+1;

  if ( (pool < 250) & (cycle==1) ):
    holod=1;


  if (holod==1):
    pool=pool+pumph;
    pumph_v=pumph_v+pumph;

  # if (pool > 500):
  #   holod=0;
  #   cycle=cycle+1;

  print(" - ", end="");
  print(pumph_v, end="");

  time.sleep(0.2);
  print();