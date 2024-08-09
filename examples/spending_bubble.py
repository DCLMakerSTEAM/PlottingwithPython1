import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('department_spending.csv')

# Ensure the Spending column is numeric
df['Spending'] = pd.to_numeric(df['Spending'], errors='coerce')

# Drop rows with missing values in Spending
df = df.dropna(subset=['Spending'])

# Create the bubble chart
plt.figure(figsize=(10, 8))
plt.scatter(df['Department'], df['Spending'],
            s=df['Spending'],  # Bubble size proportional to spending
            alpha=0.5)

# Add labels and title
plt.title('Departmental Spending Bubble Chart')
plt.xlabel('Department')
plt.ylabel('Spending')

# Show the plot
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
