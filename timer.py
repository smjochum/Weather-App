import time
import os

def timeit(method):
    """given a class times prints its proformance"""
    def timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)
        end_time= time.time()
        print("This is how long it took!  " + str(end_time-start_time))
        return result
    return timed

