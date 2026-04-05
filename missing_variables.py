import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#Create or load a dataset
# Example dataset with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, np.nan, 30, 22, 28],
    'Salary': [50000, 60000, None, 45000, 52000],
    'Department': ['HR', 'IT', 'Finance', None, 'IT']
}

df = pd.DataFrame(data)


#Summary of missing values
missing_count = df.isnull().sum()
missing_percent = (missing_count / len(df)) * 100

missing_summary = pd.DataFrame({
    'Missing Count': missing_count,
    'Missing %': missing_percent
}).sort_values(by='Missing %', ascending=False)

print("=== Missing Value Summary ===")
print(missing_summary)


#Visualize missing values
plt.figure(figsize=(8, 4))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Bar plot of missing percentages
missing_summary[missing_summary['Missing Count'] > 0]['Missing %'].plot(
    kind='bar', color='orange', figsize=(6, 4)
)
plt.ylabel("Percentage Missing")
plt.title("Missing Data Percentage by Column")
plt.show()

