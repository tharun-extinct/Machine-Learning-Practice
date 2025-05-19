import pandas as pd
from statistics import mode

data = [12, 23, 34, 45, 56, 67, 78, 89, 90]

# Calculate mean using Brute Force
def mean(data):
    #return round(sum(data) / len(data), 3)
    return sum(data) / len(data)


# Calculate median using Brute Force
def median(data):
    if not data:
        raise ValueError("The data list is empty.")
    if len(data) == 1:
        return data[0]
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    return median


# Calculate mode using Brute Force
def mode(data):
    frequency = {}
    for number in data:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    max_count = max(frequency.values())
    modes = [number for number, count in frequency.items() if count == max_count]
    return modes


def standard_deviation(data):
    if len(data) < 2:
        raise ValueError("Standard deviation requires at least two data points.")
    meanValue = mean(data)
    variance = sum((x - meanValue) ** 2 for x in data) / (len(data) - 1)
    return variance ** 0.5


def percentile(data, percentile):
    if not 0 <= percentile <= 100:
        raise ValueError("Percentile must be between 0 and 100.")
    sorted_data = sorted(data)
    index = (percentile / 100) * (len(sorted_data) - 1)
    lower_index = int(index)
    upper_index = lower_index + 1
    if upper_index >= len(sorted_data):
        return sorted_data[lower_index]
    return sorted_data[lower_index] + (sorted_data[upper_index] - sorted_data[lower_index]) * (index - lower_index)


# Data Distribution
''' 
    -> Normal Distribution
    -> Skewed Distribution
    -> Uniform Distribution
'''
def data_distribution(data):
    frequency = {}
    for number in data:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    return frequency


if __name__ == "__main__":
    #print("Mean:", mean(data))
    #print("Median:", median(data))
    #print("Mode:", mode(data))
    print("Standard Deviation:", standard_deviation(data[0:1]))

'''
df = pd.DataFrame(data, columns=['Numbers'])
df['Square'] = df['Numbers'] ** 2
df['Cube'] = df['Numbers'] ** 3

mean = df['Numbers'].mean()


# Calculate median using pandas
median = df['Numbers'].median()
'''


