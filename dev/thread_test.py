#!/usr/bin/python

import threading 
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print "Starting" + self.name
      print_time(self.name, 5, self.counter)
      print "Exiting" + self.name

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print "%s: %s" % (threadName, time.ctime(time.time()))
   counter -= 1

thread1 = myThread(1, "Thread-1", 1)

thread1.start() 

print "Exiting main thread"
