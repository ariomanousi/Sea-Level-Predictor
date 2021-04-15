import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


# Read data from file
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
x = df['Year']
y = df['CSIRO Adjusted Sea Level']
fig, ax = plt.subplots(figsize=(20, 10))
plt.scatter(x, y, label='original data', color='blue')

# Create first line of best fit
years_extended = list(range(1800, 2075, 25))
slope, intercept, r_value, p_value, std_err = linregress(x, y)
line1 = [slope * xi + intercept for xi in years_extended]
plt.plot(years_extended, line1, color='orange', label="fitted line 1800-2050")

# Create second line of best fit
recent_years = list(range(2000, 2075, 25))
x1 = df.loc[df["Year"] >= 2000]['Year']
y1 = df.loc[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"]
slope, intercept, r_value, p_value, std_err = linregress(x1, y1)
line2 = [slope * x1i + intercept for x1i in recent_years]
plt.plot(recent_years, line2, color='green', label="fitted line 2000-2050")

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.show()

# Save plot and return data for testing (DO NOT MODIFY)
plt.savefig('sea_level_plot.png')




