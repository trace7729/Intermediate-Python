from threading import Semaphore, Thread, Lock
from queue import Queue, Empty
from random import randint
from time import sleep
from os import system, name
# Python II - Lab 6 - Annie Yen

max_customers_in_bank = 10 # maximum number of customers that can be in the bank at one time
max_customers = 30  # number of customers that will go to the bank today
max_tellers = 3 # number of tellers working today
teller_timeout = 10 # longest time that a teller will wait for new customers


class Customer():
    ''' Customer objects that each has name attribute'''
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


class Teller():
    ''' Teller objects that each has name attribute''' 
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

def bankprint(lock, msg):
    '''
    Print commands
    Args:
        lock: Lock()
        msg: string
    Returns:
        None
    '''
    lock.acquire()
    try:
        print(msg)
    finally:
        lock.release()

def wait_outside_bank(customer, guard, teller_line, printlock):
    '''
    Thread function for Customer object
    Args:
        customer: Customer object
        guard: Semaphore
        teller_line: Queue
        printlock: Lock()
    Returns:
        None
    '''
    bankprint(printlock,f"{customer} is waiting outside the bank")
    try:
        bankprint(printlock,f"<G> Security guard letting {customer} into the bank")
        guard.acquire()
        bankprint(printlock, f"(C) {customer} is trying to get into line")
        teller_line.put(customer)
        #guard.release()
    except Exception as Error:
        print("Cannot put {customer} into line " +str(Error))

def teller_job(teller, guard, teller_line, printlock):
    '''
    Thread method for Teller object
    Args:
        teller: Teller object
        guard: Semaphore
        teller_line: Queue
        printlock: Lock()
    Returns:
        None
    '''
    bankprint(printlock, f"[T] {teller} has started working")
    while True:
        try:
            #guard.acquire()
            customer = teller_line.get(timeout=teller_timeout)
            bankprint(printlock, f"[T] {teller} is now helping {customer}")
            sleep(randint(1,4))
            bankprint(printlock, f"[T] {teller} is done helping {customer}")
            bankprint(printlock, f"<G> Security is letting {customer} out of the bank")
            guard.release()
        except Empty:
            bankprint(printlock, f"[T] No one is in line, {teller} is going on a break")
            break


if __name__ == '__main__':
    printlock = Lock()
    teller_line = Queue(maxsize=max_customers_in_bank)
    guard = Semaphore(max_customers_in_bank)

    bankprint(printlock, "<G> Security guard starting their shift")
    bankprint(printlock, "*B* Bank open")

    # create list of Customer objects and pass to thread method
    customers = [Customer("Customer " +str(i)) for i in range(1, max_customers+1)]
    for i in range(0, len(customers)):
        customer_thread = Thread(name=f"customers[i]", target = wait_outside_bank, args =(customers[i],guard, teller_line, printlock))
        customer_thread.start()

    sleep(5)
    bankprint(printlock, "*B* Tellers started working")

    # create a list of Teller objects and pass to thread method in another list
    tellers = [Teller("Teller "+str(i)) for i in range(1,max_tellers+1)]
    tellers_list = [Thread(name=f"tellers[i]", target = teller_job, args = (tellers[i], guard, teller_line, printlock)) for i in range(0,len(tellers))]
    for teller in tellers_list:
        teller.start()
    for teller in tellers_list:
        teller.join()

    bankprint(printlock, "*B* Bank closed")		
