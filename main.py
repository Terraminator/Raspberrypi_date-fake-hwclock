# Sync system date with fake-hwclock
#!/usr/bin/python3
import time
from datetime import datetime

def get_date():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    return(date)

def set_date(date):
   with open("/etc/fake-hwclock.data", 'w') as f:
       f.write(date)
       f.close()
   return(0)

def main():
   while True:
      date = get_date()
      r = set_date(date)
      print(date)
      time.sleep(120)

if __name__ == "__main__":
   main()
