#!/usr/bin/env python
# coding: utf-8
''' Razat Siwakoti (A00046635)
DMV302- Assessment 3 
DMV302Tb.ipynb

SourceCode:
(seaborn , 2023)
seaborn.heatmap (2023). seaborn 0.13.0 documentation. Pydata.org. https://seaborn.pydata.org/generated/seaborn.heatmap.html

(Matplotlib. 2023)
Matplotlib (2023). Visualization with Python. Matplotlib.org. https://matplotlib.org/

(Ravikiran, 2023)
Ravikiran. (May 18, 2023). A Complete Guide to Data Visualization in Python With Libraries & More. Simplilearn. https://www.simplilearn.com/tutorials/python-tutorial/data-visualization-in-python
# In[36]:
'''

#import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# In[37]:


# read csv file and display few first rows
df = pd.read_csv("Dataset2.csv")
df.head()


#                                             
#                      -
#                      
#                      
#                      
#                      ##--------------Fig 1 : Correlation heatmap --------------##

# In[38]:


#show correlation between multiple variables as a color-coded matrix
# Select relevant columns for the heatmap (temperature variables and rainfall)
selected_columns = df.iloc[:, 1:12] # Adjust column indices based on your dataset


# Calculate correlation matrix
correlation_matrix =selected_columns.corr()

# Set up the matplotlib figure
plt.figure(figsize=(12, 10))

# Create a heatmap using Seaborn
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)

# Customize the plot
plt.title("Correlation Heatmap for Weather History Dataset") ##title
plt.xticks(rotation=90) 
plt.yticks(rotation=0)
# Display the heatmap
plt.show()


#                                            
#                      -
#                      
#                      
#                      
#                       ##--------------Fig 2: Box and Whisker Plot --------------## 

# In[39]:


#to visualize the distribution of different variables in the dataset
# Generate a horizontal boxplot using Seaborn
sns.boxplot(data=df, orient="h", palette="Set1")

# Customize the plot
plt.title('Box and Whisker Plot for Different Variables in the Dataset')
plt.xlabel('Value Distribution')
plt.ylabel('Variable Categories')

# Display the boxplot
plt.show()


#                                            
#                      -
#                      
#                      
#                      
#                       ##--------------Fig 3 : Bubble Chart --------------## 

# In[40]:


##For average temperature of that day, average temperature f that day since 1901 and raibnfall
# Normalize the rainfall values for better bubble size visualization
df['normalized_rainfall'] = df['rain'] * 1000

# Create a Bubble Chart
plt.figure(figsize=(12, 8))
plt.scatter(df['avg temp'], df['avg max temp since 1901'], s=df['normalized_rainfall'], alpha=0.7, c='blue', edgecolors='grey', linewidth=2)

# Customize the chart
plt.title('Bubble Chart for Temperature and Rainfall')
plt.xlabel('avg temp')
plt.ylabel('avg max temp since 1901')
plt.grid(True)
plt.tight_layout()

# Add a color bar legend indicating rainfall intensity
color_bar = plt.colorbar()
color_bar.set_label('Rainfall Intensity')

# Show the chart
plt.show()


#                                            
#                      -
#                      
#                      
#                      
#                       ##--------------Fig 4 : Combo chart for Temperature and rainfall overtime --------------## 

# In[41]:


#observe temperature trends and rainfall occurrences simultaneously.
# Set the figure size
plt.figure(figsize=(60, 20))

# Plotting temperature (line chart)
sns.lineplot(x='Date', y='avg temp', data=df, label='avg temp', color='blue')
sns.lineplot(x='Date', y='min temp', data=df, label='min temp', color='green')
sns.lineplot(x='Date', y='max temp', data=df, label='max temp', color='red')

# Creating a secondary y-axis for rainfall (bar chart)
ax2 = plt.twinx()
sns.barplot(x='Date', y='rain', data=df, alpha=0.5, color='gray', ax=ax2)

# Set labels and title
plt.title('Combo Chart for Temperature and Rainfall')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
ax2.set_ylabel('Rainfall (inches)')

# Display the legend
plt.legend(loc='upper left')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.show()


#                      
#                      -
#                      
#                      
#                      
#                      ##--------------Fig 5 : Scatter Plot Matrix --------------## 

# In[42]:


#to visualize the pairwise correlations between different columns, providing a comprehensive view of the data
# Assuming your dataset is stored in a variable named 'weather_data'
selected_columns = ['avg temp', 'min temp', 'max temp', 
                     'rain', 'avg rain since 1901']

# Selecting the relevant columns for the scatter plot matrix
selected_data = df[selected_columns]

# Creating the Scatter Plot Matrix
scatter_plot_matrix = sns.pairplot(selected_data, diag_kind='hist', markers='o')

# Adding a title
scatter_plot_matrix.fig.suptitle('Scatter Plot Matrix for Weather Variables', y=1.02)

# Displaying the plot
plt.show()

