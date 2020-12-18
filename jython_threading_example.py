from rough import print_time
from datetime import datetime

"""
This is actually using python threading package.
One thing I came to know is that if we use the python threading module also, 
internally Jython chnages it to Java thread and work.
"""
# from threading import Thread, InterruptedException

"""
This is the java threading module.
"""
from java.lang import Thread, InterruptedException


"""
Here you can call your module from the run method.
For passing arguments, you can use the constructor of the Cycle class.
"""
class Cycle(Thread):

    def __init__(self,time1=1):
        Thread.__init__(self)
        # arguments for the run method
        self.time1 = time1

    def run(self):
        try:
            # Calling the required module with given arguments
            print_time(self.time1)
        except InterruptedException:
            print("Exception")

if __name__ == '__main__':
    print("start time:",datetime.now())
  
    for i in range(100):
        Cycle(i).start()
        
    print("end time:",datetime.now())

