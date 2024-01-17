#!/usr/bin/env python
# coding: utf-8
'''
Razat Siwakoti (A00046635)
DMV302- Assessment 3 
DMV302Ta.ipynb

SourceCode:
(VanderPlas, 2023)
VanderPlas, J. (2023). Three-Dimensional Plotting in Matplotlib | Python Data Science Handbook. Github.io. https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

(Matplotlib. 2023)
Matplotlib (2023). Visualization with Python. Matplotlib.org. https://matplotlib.org/

'''
# In[20]:


#import neccessary libraries
import pandas as pd
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#read dataset
df = pd.read_csv("Dataset1.csv", header=None)
df.head()


# 
# 
# 
# 
# ##-------------------3D scatter plot with two histograms---------------

# In[21]:


import matplotlib.gridspec as gridspec

# Extract columns for scatter plot
x_data = df.iloc[:, 0]  # first column for X-axis
y_data = df.iloc[:, 1]  # second column  for y-axis
z_data = df.iloc[:, 2]  # third columnfor the z-axis

# Create scatter plot and histograms
fig = plt.figure(figsize=(16, 12))
gs = gridspec.GridSpec(2, 2, width_ratios=[4, 1], height_ratios=[1, 4])

# Scatter plot
ax_scatter = plt.subplot(gs[1, 0], projection = '3d') #for 3D projection
ax_scatter.scatter(x_data, y_data, z_data, alpha=0.7) #plot the values from the dataset
#labels for axis
ax_scatter.set_xlabel('X-axis')
ax_scatter.set_ylabel('Y-axis')
ax_scatter.set_zlabel('Z-axis')

# Histogram for Y-axis on top
ax_hist_x = plt.subplot(gs[0, 0], sharex=ax_scatter)
ax_hist_x.hist(y_data, bins=20, alpha=0.5, color='red', density=True , edgecolor='black')
ax_hist_x.set_ylabel('Frequency')
ax_hist_x.set_title('Histogram for Y-axis')

# Histogram for Z-axis on the right
ax_hist_y = plt.subplot (gs[1, 1], sharey=ax_scatter)
ax_hist_y.hist(z_data, bins=20, alpha=0.5, color='blue', density=True, orientation='horizontal', edgecolor='black')
ax_hist_y.set_xlabel('Frequency')
ax_hist_y.set_title('Histogram for Z-axis')

#add title, layout and show
plt.suptitle('3D Scatter Plot with Histograms', fontsize=20)
plt.tight_layout()
plt.show()


# #-----------------Project 2D data onto a 3D plane (Y-Z)---------------------
# 

# #--------as my student number ends with 5, Y-Z plane had to be selected according to the brief-------

# In[22]:


# Project the 3D data onto a 2D plane (Y-Z)
y_z_plane = df[[1, 2]]

# Scatter plot of the 3D data with only Y-Z values
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot settings
ax.scatter(df[1], df[2], zs=0, zdir='z', depthshade=False, c='skyblue', edgecolor='black', alpha=0.7, s=50)

# Axes labels and title
ax.set_xlabel('Y-axis')
ax.set_ylabel('Z-axis')

'''In the case of the 2D projection onto the Y-Z plane, we are essentially representing a 2D space, 
and the third dimension (X-axis) is not being visualized directly in the plot. 
Therefore, setting for the X-axis is not necessary in this context.'''

ax.set_zlabel('X-axis')
ax.set_title('3D Scatter Plot with 2D Projection onto Y-Z Plane')

# Gridlines for better visualization
ax.grid(True, linestyle='--', alpha=0.5)

# Remove box around the plot for cleaner appearance
ax.set_box_aspect([1, 1, 0.2])  # Adjust the third value for the depth

# Show the plot
plt.show()


# #-------------------------Projecting  2D data onto a 2D plane (Y-Z) with histogram for each dimension---------------------
# 

# In[16]:


# Project the 3D data onto a 2D plane (Y-Z)
y_z_plane = df[[1, 2]]


# Scatter plot of the 2D data (Y-Z)
plt.figure(figsize=(12, 6))
plt.scatter(y_z_plane[1], y_z_plane[2])
plt.axhline(0, color='black', linestyle='--', linewidth=1)  # Add a horizontal line at y=0
plt.xlabel('Y-axis')
plt.ylabel('Z-axis')
plt.title('Projection of Scatter Plot of 2D Data (Y-Z plane)')
plt.show()

# Project the 2D data onto each dimension and create histograms
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Project onto X-axis
sns.histplot(df[0], bins=20, kde=True, color='red', label='X-axis', orientation='horizontal',ax=axes[0], edgecolor='black')
axes[0].set_xlabel('X-axis')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Histogram in X-dimension')
axes[0].legend()

# Project onto Y-axis
sns.histplot(y_z_plane[1], bins=20, kde=True, color='blue', label='Y-axis', ax=axes[1], edgecolor='black')
axes[1].set_xlabel('Y-axis')
axes[1].set_ylabel('Frequency')
axes[1].set_title('Histogram in Y-dimension')
axes[1].legend()

# Project onto Z-axis
sns.histplot(y_z_plane[2], bins=20, kde=True, color='green', label='Z-axis',orientation='horizontal', ax=axes[2], edgecolor='black')
axes[2].set_xlabel('Z-axis')
axes[2].set_ylabel('Frequency')
axes[2].set_title('Histogram in Z-dimension')
axes[2].legend()

# Adjust layout
plt.tight_layout()
plt.show()


# ##------- 2d scattter plot with histogram

# In[23]:


import matplotlib.gridspec as gridspec

# Extract columns for scatter plot
y_data = y_z_plane[1]
z_data = y_z_plane[2]

# Create a 2D scatter plot with histograms
fig = plt.figure(figsize=(16, 12))
gs = gridspec.GridSpec(2, 2, width_ratios=[4, 1], height_ratios=[1, 4])

# Scatter plot in the center
ax_scatter = plt.subplot(gs[1, 0])
ax_scatter.scatter(y_data, z_data)
ax_scatter.axhline(0, color='black', linestyle='--', linewidth=1)  # Add a horizontal line at y=0
ax_scatter.set_xlabel('Y-axis')
ax_scatter.set_ylabel('Z-axis')

# Histogram for Y-axis above the scatter plot
ax_hist_y = plt.subplot(gs[0, 0], sharex=ax_scatter)
ax_hist_y.hist(y_data, bins=20, alpha=0.5, color='blue', density=True, edgecolor='black')
ax_hist_y.set_ylabel('Frequency')
ax_hist_y.set_title('Histogram in Y-dimension')

# Histogram for Z-axis to the right of the scatter plot
ax_hist_z = plt.subplot(gs[1, 1], sharey=ax_scatter)
ax_hist_z.hist(z_data, bins=20, alpha=0.5, color='green', density=True, orientation='horizontal', edgecolor='black')
ax_hist_z.set_xlabel('Frequency')
ax_hist_z.set_title('Histogram in Z-dimension')

# Add a title with a larger font size
plt.suptitle('2D Scatter Plot with Histograms (Y-Z plane)', fontsize=16)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

