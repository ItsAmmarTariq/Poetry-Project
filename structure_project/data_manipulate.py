import pandas as pd

# Load the CSV 
file_path = "file.csv"
df = pd.read_csv(file_path)

# Display 
print("Original DataFrame:")
print(df)


filtered_df = df[df['Age'] >= 30]


print("\nFiltered DataFrame (Age >= 30):")
print(filtered_df)

# Calculate 
average_salary = filtered_df['Salary'].mean()
print(f"\nAverage Salary of Individuals with Age >= 30: ${average_salary:.2f}")
