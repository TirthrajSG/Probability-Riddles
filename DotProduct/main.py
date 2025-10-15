import random
import matplotlib.pyplot as plt

def running_mean(arr):
    new_arr = []
    total = 0
    for i, x in enumerate(arr, 1):
        total += x
        new_arr.append(total / i)
    return new_arr

def find_prob(total_outcomes=1000, n=10):
    favorable = 0
    for _ in range(total_outcomes):
        dot = sum(random.randint(0,1) * random.randint(0,1) for _ in range(n))
        if dot % 2:
            favorable += 1
    return favorable / total_outcomes

n = 10
probs = [find_prob(n=n) for _ in range(1000)]
cum_probs = running_mean(probs)
actual_prob = 1/2 - 1/2**(2*n+1)

plt.plot(cum_probs, label="Simulated running mean")
plt.axhline(y=actual_prob, color='red', linestyle='--', label="Theoretical value")
plt.legend()
plt.show()
