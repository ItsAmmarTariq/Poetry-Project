import numpy as np

def calculate_statistics(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    return mean, std_dev

def main():
    
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    
    mean, std_dev = calculate_statistics(data)

    print(f"Data: {data}")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {std_dev}")

if __name__ == "__main__":
    main()
