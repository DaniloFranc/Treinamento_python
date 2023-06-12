import random

def monte_carlo(num_samples):
    count_in_circle = 0
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:
            count_in_circle += 1
    return 4 * count_in_circle / num_samples

print(monte_carlo(100000))