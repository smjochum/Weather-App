# Module 4 - processes

import multiprocessing as mp
import os
import time
import random
random.seed()

# The following parts 1-10 can be commented out as individual blocks to run.

# 1. The following code shows how to creaate and run processes.
# a. How many processes run in the following code?
# b. predict the answer to the questions, then run the code to check your answer

# def add1(n):
#     newN = n + 1
#     print("n:", n, "newN:", newN, "PID:", os.getpid(), "name:", mp.current_process().name)
#                                    # getting PID and name of process
#
# if __name__ == '__main__':   # is this needed?
#     numbers = [10, 20, 30]
#     procs = []
#
#     for n in numbers:
#         p = mp.Process(target=add1, args=(n,))   # what is args?
#         procs.append(p)
#         p.start()
#
#     namedP = mp.Process(target=add1, args=(-1,), name='named process')
#     namedP.start()
#
#     print("done1")    # is this printed before or after the child processes are done?
#     for p in procs:
#         p.join()
#     namedP.join()
#     print("done2")     # is this printed before or after the child processes are done?
#

# 2. Check process status
# predict the status that's printed in the code below, then run the code to check your answer
#
# def slowFunction():
#     print("Start slow function")
#     time.sleep(1)
#     print("End slow function")
#
# if __name__ == '__main__':
#     p = mp.Process(target=slowFunction)
#     print("main start: p alive status", p.is_alive())
#
#     p.start()
#     print("p start: p alive status", p.is_alive())
#
#     p.join()
#     print("main join: p alive status", p.is_alive(), ", p exit status", p.exitcode)



# 3. Processes and shared resources
# Recall that we used a lock to prevent a race condition when 4 threads update a Counter object.
# Now we do the same with 3 processes, predict the count value at the end of the code.
#
# class Counter() :
#     def __init__(self) :
#         self.counter = 0
#         self.lock = mp.Lock()
#     def inc(self) :
#         with self.lock :
#             for x in range(200000):    # 200,000 iterations
#                 self.counter += 1
#     def printCount(self) :
#         print(self.counter)
#
# if __name__ == '__main__':
#     procs = []
#     c = Counter()
#     for i in range(3):
#         p = mp.Process(target=c.inc, args=())
#         procs.append(p)
#         p.start()
#     for p in procs:
#         p.join()
#     c.printCount()
#
#
#
# # 4. What count value should be printed at the end?
# What count value is printed? Why?
'''
def printFile():     
    with open("counter.txt","r") as fh :
        num = fh.readline()
    for i in range(50000) :      # 50,000 iterations
        num = int(num) + 1
    with open("counter.txt","w") as fh :
        fh.write(" {:d}".format(num))
        
if __name__ == '__main__':
    procs = []
    with open("counter.txt", "w") as fh :
        fh.write("0")               
    for i in range(4) :
        p = mp.Process(target=printFile)
        procs.append(p)
        p.start()
    for p in procs :
        p.join()
    with open("counter.txt") as fh :
        print(fh.readline())
'''


# 5. use Event to signal conditions
# What will be printed to screen?

def waitToPrint(e):
    e.wait()
    print(mp.current_process().name + ": printing...")

def waitWithTimeout(e, t):
    e.wait(t)
    if e.is_set() :
        print(mp.current_process().name + ": printing...")
    else :
        print(mp.current_process().name + ": no printing")

if __name__ == '__main__':
    e = mp.Event() #happens when p1 starts
    p1 = mp.Process(name='wait_until_set', target=waitToPrint, args=(e,))  # will wait
    p1.start()

    p2 = mp.Process(name='wait_with_timeout', target=waitWithTimeout, args=(e, 1))  # will time out
    p2.start()

    print("main: before setting Event")
    time.sleep(2)
    e.set()
    print("main: event is set")

    p1.join()
    p2.join()
    print("main: done")

#### KNOW HOW TO NUMBER ORDER OF PROCESSES.


# 6. Add to the code below to use a queue as the data buffer for producer / consumer,
# then print all the numbers that are produced.
'''
def randNum(length) :    
    num = 0
    for i in range(length) :
        num += (10 ** i) * random.randint(0,9)

if __name__ == '__main__' :
    pList = []
    for i in range(3) :
        p = mp.Process(target=randNum, args=(5,))
        pList.append(p)
        p.start()     # each process produces a random number
    
    for p in pList:
        p.join()
    
    for i in range(3) :
        print()       # print the random numbers that are produced
'''


# 7. Use a Pool to get multiple processes to run in parallel
# various tasks to be run:
def square(x):
    time.sleep(4)       
    return x * x

def add(args) :         
    time.sleep(1)
    return args[0] + args[1]

def printResult(result) :
    print("result:", result)

def double(x) :
    return x + x

"""
if __name__ == '__main__' :
    pool = mp.Pool(processes=4)

    nums1 = [10,11,12,13,14]
    nums2 = [1, 2, 3, 4, 5]
    args = [(10,1), (11,2), (12,3), (13,4), (14,5)]   
    
    '''
    # a. what does this code print?
    results = pool.map(square, nums1)          
    print("square results", results)
    '''
    
    '''
    # b. Add code below to run the add function in parallel.
    # which of the lists above can be used as input arguments to add?

    print("add results", results)
    print("main done")       # is this printed before or after the results? Why?
    '''    
 
    '''
    # c. Add to the code to print the results
    results = [pool.apply_async(square, args=(x,)) for x in range(1,10)]
 
    '''
    
    '''
    # d. What does this print?
    for x in range(10,15) :
        pool.apply_async(square, args=(x,), callback=printResult)    
    '''
    
    pool.close()
    pool.join()

"""