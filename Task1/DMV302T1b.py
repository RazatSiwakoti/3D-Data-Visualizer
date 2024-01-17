#!/usr/bin/env python
# coding: utf-8
#Razat Siwakoti (A00046635)
#DMV302- Assessment 3 
#DMV302Ta.ipynb

#SourceCode:
#(VanderPlas, 2023)
#VanderPlas, J. (2023). Three-Dimensional Plotting in Matplotlib | Python Data Science Handbook. Github.io. https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

#(Matplotlib. 2023)
#Matplotlib (2023). Visualization with Python. Matplotlib.org. https://matplotlib.org/


# In[1]:


#import neccessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#read dataset
df = pd.read_csv('Dataset1.csv', header=None)
df.head()


# In[2]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

# Apply KMeans clustering with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42) #k=3 from brief
df['cluster'] = kmeans.fit_predict(df)

# Define different markers and increased marker sizes for each cluster
markers = ['o', '^', '*']
marker_sizes = [30, 30, 40]  # Adjust the sizes as needed

# Larger 3D Scatter Plot with increased marker sizes
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot each cluster with different markers, colors, and sizes
for cluster_num, marker, size in zip(range(3), markers, marker_sizes):
    cluster_data = df[df['cluster'] == cluster_num]
    ax.scatter(cluster_data[0], cluster_data[1], cluster_data[2], label=f'Cluster {cluster_num + 1}', marker=marker, s=size)

# Labeling and Title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Larger 3D Scatter Plot with KMeans Clustering')

# Display legend
ax.legend()

# Show the plot
plt.show()

