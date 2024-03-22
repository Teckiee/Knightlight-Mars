import _thread
import time
# Define a function for the thread
def thread_task( threadName, delay):
   for count in range(1, 6):
      time.sleep(delay)
      print ("Thread name: {} Count: {}".format ( threadName, count ))

# Create two threads as follows
try:
   _thread.start_new_thread( thread_task, ("Thread-1", 2, ) )
   _thread.start_new_thread( thread_task, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while True:
   pass