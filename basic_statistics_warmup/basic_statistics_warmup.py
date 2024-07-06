import math
import statistics
import scipy.stats as st

n = int(input())
numbers = sorted(list(map(int, input().split())))

# calculate mean, median, mode
mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)

# calculate standard deviation
stdev = statistics.pstdev(numbers)

# calculate confidence interval
confidence_interval = 1.96 * (stdev / math.sqrt(n))
confidence_interval_lower = mean - confidence_interval
confidence_interval_upper = mean + confidence_interval

print(round(mean, 1))
print(round(median, 1))
print(round(mode, 1))
print(round(stdev, 1))
print(f"{round(confidence_interval_lower, 1)} {round(confidence_interval_upper, 1)}")