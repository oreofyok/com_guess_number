import random
import time

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
    
    time.sleep(1)
    
    print()
    print("your number is",l,"-",h,"right?"); time.sleep(.5)
    print("Then. Is",c,"correct?") ; time.sleep(.5)
    if mode == "1":
      player = input("too low(l),too high(h), correct(c): ") ; time.sleep(.5)
      print("already =",already)
    elif mode == "2":
      if c < destination:
        print("you told it too low from (",destination,")") ; time.sleep(.5)
        print("already =",already) ; time.sleep(.5)
        player = "l"
      elif c > destination:
        print("you told it too high from (",destination,")") ; time.sleep(.5)
        print("already =",already) ; time.sleep(.5)
        player = "h"
      elif c == destination:
        player = "c"
    if player == "l":
      if c == h:
        print()
        print("is",c,"too low?") ; time.sleep(.5)
        if mode == "1":
          h = int(input("input your max number again: ")) ; time.sleep(.5)
        elif mode == "2":
          h = destination + 10
          print("The max upper to",h) ; time.sleep(.5)
        for i in range(l,h+1):
          alll.add(i)
        
      else:
        l = c+1
    elif player == "h":
      if c == l:
        print()
        print("is",c,"too high?") ; time.sleep(.5)
        if mode == "1":
          l = int(input("input your min number again: ")) ; time.sleep(.5)
        elif mode == "2":
          l = destination - 10
          print("The min lower to",l) ; time.sleep(.5)
        for i in range(l,h+1):
          alll.add(i)
        
      else:
        h = c-1
    if l == h:
      if mode == "2" and l < destination:
        h = destination + 10
        print()
        print("seems max is too low,max up to",h) ; time.sleep(.5)
        for i in range(l,h+1):
          alll.add(i)
        
      elif mode == "2" and l > destination:
        l = destination - 10
        print()
        print("seems min is too high,min low to",l) ; time.sleep(.5)
        for i in range(l,h+1):
          alll.add(i)
        
      elif mode == "2" and l == destination:
        c = l
        print("there is only one number left and that number is ",c) ; time.sleep(.5)
        break
  elif c in already:
    error += 1
    #print(c,"is an already number",error)
    if error == 20:
      print("already guess all number that can guess ,program quit") ; time.sleep(.5)
      break
    
  
print()
if error != 20:
  print("com think in",think,"rounds") ; time.sleep(.5)
  print("Correct number is",c)
else:
  print("cannot find your number.")
