import time
import heapq as hq
  
# jobs to be executed
jobs = [(2, 'task_1'), (5, 'task_2'), (1, 'task_4'),
        (4, 'task_5'), (3, 'task_3'), (1, 'task_8')]
  
# interrupts
interrupts = [(1, 'intr_1'), (2, 'intr_2'), (13, 'intr_3')]
  
i, j = 0, 0
  
# Arranging jobs in heap
hq.heapify(jobs)
  
print(jobs, "\n\n")
print(hq.heappop(jobs))
print(hq.heappop(jobs))
print(hq.heappop(jobs))