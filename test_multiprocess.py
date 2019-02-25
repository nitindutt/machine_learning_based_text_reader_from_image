from threading import Thread
import time

def func1(sleep_time):
    print 'func1: starting'
    print ("sleeping for %d time" %(sleep_time))
    time.sleep(sleep_time)
    print ("func1 done")
    return True

def func2():
    print 'func2: starting'
    time.sleep(3)
    print ("func2 done")
    return True


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None
    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)
    def join(self):
        Thread.join(self)
        return self._return

func1Exe = ThreadWithReturnValue(target=func1, args=(2,))

twrv.start()
func2()
func1_return_value = func1Exe.join()
print (func1_return_value)



