import threading
import time
def worker(num):
  print(f"Thread{num}: starting")
  time.sleep(2)
  print(f"Thread{num}: finishing")

threads = []
for i in range(5):
  thread = threading.Thread(target=worker, args=(i,))
  threads.append(thread)
  thread.start()
  
for thread in threads:
  thread.join()
  
print("All threads completed.")  