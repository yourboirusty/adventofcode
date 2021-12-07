from statistics import median

data = [int(x) for x in open('7/input').read().split(',')]
print(sum(map(lambda x: abs(x-median(data)), data)))
crab_mean = sum(data) // len(data)
print(sum(map(lambda x: sum(range(abs(x-crab_mean)+1)), data)))
