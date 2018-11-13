import time
def timeit(method):
    def timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)
        end_time= time.time()
        print(end_time-start_time)
        return result
    return timed

