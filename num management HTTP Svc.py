from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

#wait for 5 seconds
def return_after_5_secs(message):
    sleep(5)
    return message

 #wait for 7 seconds
def return_after_7_secs(message):
    sleep(8)
    return message
 
pool = ThreadPoolExecutor(3)
future_list = list()
#submitting the 5 seconds wait method
future_list.append(pool.submit(return_after_5_secs, ("hello5")))
#submitting the 7 seconds wait method
future_list.append(pool.submit(return_after_7_secs, ("hello3")))
#check immediately if any of the process completes
print(future_list[0].done())
print(future_list[1].done())
# no one completes
print("no one completes.. waiting for 6 sec..")
#wait for 6 seconds
sleep(6)
print("waiting completes for 6 secs..")
print(future_list[0].done())
print(future_list[1].done())
print("Result: " + future_list[0].result())
# first job has completed
print("again gonna wait for 3 secs..")
sleep(3)
print("wait completes for 3 secs..")
#second job will also complete now
print(future_list[0].done())
print(future_list[1].done())
print("Result: " + future_list[0].result()+" "+future_list[1].result())
#shutting down the pool executor
pool.shutdown()
 
