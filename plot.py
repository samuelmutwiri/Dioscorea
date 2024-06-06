import matplotlib.pyplot as plt
import pandas as pd

#comment out one of the two lines below to switch between nutritional content and phytochemical content datasets
#data = pd.read_csv('data.csv') #nutritional content dataset
data = pd.read_csv('data1.csv') #phytochemical content dataset

categories = data.iloc[:, 0]

# Get the values for the bars from columns
values = data.iloc[:, 1:]

# Get the column names for the legend
column_names = values.columns

# Create a figure and axis
fig, ax = plt.subplots()

# Set the width of each bar
bar_width = 0.75 / values.shape[1]

# Set the position of the bars on the x-axis
bar_positions = range(len(categories))

# Plot the bars
bars = []
for i, column in enumerate(values.columns):
    bar = ax.bar(
        [x + i * bar_width for x in bar_positions],
        values[column],
        bar_width,
        label=column_names[i]
    )
    bars.append(bar)

# Set the x-axis ticks and labels
ax.set_xticks([x + (bar_width * (values.shape[1] - 1)) / 2 for x in bar_positions])
ax.set_xticklabels(categories)

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=45)

# Add a legend
ax.legend()

# Add labels and title
ax.set_xlabel('Species')
ax.set_ylabel('Concentration')
#ax.set_title('Nutritional Content Comparison')
ax.set_title('Phytochemical Content Comparison')

# Show the plot
plt.show()