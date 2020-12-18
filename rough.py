from datetime import datetime

def print_time(delay):
   count = 0
   while count < 10000000:
      count += 1
      
   if delay==99:
      print("Last but not the least:",datetime.now())
