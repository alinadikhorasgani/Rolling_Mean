import pandas as pd
import matplotlib.pyplot as plt

# Sample data (monthly sales)
data = {
    'Month': pd.date_range(start='2022-01-01', periods=12, freq='M'),
    'Sales': [10, 15, 8, 12, 18, 14, 20, 22, 26, 24, 30, 28]
}

df = pd.DataFrame(data)

# Calculate a 3-month rolling mean
window_size = 3
df['Rolling Mean'] = df['Sales'].rolling(window=window_size).mean()

# Plot the original data and the rolling mean
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], label='Original Data', marker='o')
plt.plot(df['Month'], df['Rolling Mean'], label=f'{window_size}-Month Rolling Mean', linestyle='--', color='red')

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Data with Rolling Mean')
plt.legend()
plt.grid(True)

plt.show()
