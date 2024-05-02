import hashlib
import time
import random
import string
import matplotlib.pyplot as plt

def solve_puzzle(B):
    P = ''.join(random.choice('01') for _ in range(B))  
    start_time = time.time()
    while True:
        M = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        hash_object = hashlib.sha256(M.encode())
        hash_end = bin(int(hash_object.hexdigest(), 16))[-B:]  
        if hash_end == P:
            end_time = time.time()
            print(f"Found a solution for B={B}: M={M}, h(M)={hash_end}, P={P}")
            return (end_time - start_time) * 1000

B_values = [4, 8, 12, 16]
times = []
trials = 10

for B in B_values:
    total_time = 0
    avg_time = 0
    for _ in range(trials):
        solve_time = solve_puzzle(B)
        print(f"Found in {solve_time} milliseconds")
        total_time += solve_time
    avg_time = total_time / trials   
    times.append(avg_time)

for i in range(len(B_values)):
    print(f"Average solve time for {B_values[i]} bits was {times[i]} milliseconds") 

plt.plot(B_values, times)
plt.xlabel('B value')
plt.ylabel('Average time (milliseconds)')
plt.title('Time to solve crypto puzzle for different B values')
plt.show()
