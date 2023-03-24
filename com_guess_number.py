import random

player = " "
l = 0;h = 0

print("Welcome to com think number game.")
print("select your mode")

while True:
  mode = input("1.manual 2.auto: ")
  if mode == "1" or mode == "2":
    break
  else:
    print("input only 1 and 2")
    print()



while l >= h:
  print()
  l = int(input("input min value: "))
  h = int(input("input max value: "))
  if l > h:
    print("l must lower than h")
if mode == "2":
    destination = int(input("input your destination number: "))
 
think = 0
already = set()
alll = set()

for i in range(l,h+1):
    alll.add(i)

while player != "c":
  
  think += 1 
  c = random.randint(l,h)
   
  if c in alll - already:
    already.add(c)
    error = 0
      
    print()
    print("your number is",l,"-",h,"right?")
    print("Then. Is",c,"correct?")
    if mode == "1":
      player = input("too low(l),too high(h), correct(c): ")
      print("already =",already)
    elif mode == "2":
      if c < destination:
        print("you told it too low from (",destination,")")
        print("already =",already)
        player = "l"
      elif c > destination:
        print("you told it too high from (",destination,")")
        print("already =",already)
        player = "h"
      elif c == destination:
        player = "c"
    if player == "l":
      if c == h:
        print()
        print("is",c,"too low?")
        if mode == "1":
          h = int(input("input your max number again: "))
        elif mode == "2":
          h = destination + 10
          print("The max upper to",h)
        for i in range(l,h+1):
          alll.add(i)
        
      else:
        l = c+1
    elif player == "h":
      if c == l:
        print()
        print("is",c,"too high?")
        if mode == "1":
          l = int(input("input your min number again: "))
        elif mode == "2":
          l = destination - 10
          print("The min lower to",l)
        for i in range(l,h+1):
          alll.add(i)
        
      else:
        h = c-1
    if l == h:
      if mode == "2" and l < destination:
        h = destination + 10
        print()
        print("seems max is too low,max up to",h)
        for i in range(l,h+1):
          alll.add(i)
        
      elif mode == "2" and l > destination:
        l = destination - 10
        print()
        print("seems min is too high,min low to",l)
        for i in range(l,h+1):
          alll.add(i)
        
      elif mode == "2" and l == destination:
        c = l
        print("there is only one number left and that number is ",c)
        break
  elif c in already:
    error += 1
    #print(c,"is an already number",error)
    if error == 20:
      print("already guess all number that can guess ,program quit")
      break
    
  
print()
if error != 20:
  print("com think in",think,"rounds")
  print("Correct number is",c)
else:
  print("cannot find your number.")
