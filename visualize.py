import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

def histogram(data):
    exam_scores = np.random.normal(70, 10, 100)
    plt.hist(exam_scores, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    plt.title('Normal Distribution') 
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()


def compare_hist_dist():
    # Generate sample data
    data = np.random.normal(70, 10, 1000)
    
    # Create histogram
    plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Histogram')
    
    # Add theoretical normal distribution curve
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, 70, 10)
    plt.plot(x, p, 'k', linewidth=2, label='Normal Distribution')
    
    plt.title('Histogram vs Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    plt.show()


def sample():
    df = sns.load_dataset("diamonds")

    sns.scatterplot(x="carat", y="price", data=df)
    plt.title('Scatter Plot of Carat vs Price')
    plt.xlabel('Carat')
    plt.ylabel('Price')
    plt.show()
    

if __name__ == "__main__":
    data = np.random.normal(0, 1, 100)
    #compare_hist_dist()
    sample()
