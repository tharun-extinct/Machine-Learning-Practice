import matplotlib.pyplot as plt
import numpy as np

def histogram(data):
    plt.hist(data, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    plt.title('Histogram of Data Distribution') 
    plt.xlabel('Value') 
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    data = np.random.normal(0, 1, 100)

    