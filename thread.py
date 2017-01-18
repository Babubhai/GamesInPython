import sys
import threading

class clientListener(threading.Thread):
    def __init__(self,a,threadID):
        threading.Thread.__init__(self)
        self.a = a
        self.threadID = threadID
    def run(self):
        while (self.a > 0):
            threadlock.acquire()
            print_msg(self.a,self.threadID)
            threadlock.release()
            self.a -= 1


def print_msg(number,tid):
    print "message from thread "+str(tid)+" "+str(number)

threadlock = threading.Lock()
threads = []

thread1 = clientListener(5,2)
thread2 = clientListener(3,3)

thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)
for t in threads:
    t.join()
