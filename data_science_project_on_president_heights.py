# -*- coding: utf-8 -*-
"""Data Science Project on President Heights.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_GlwqpVASI7Q1IzFpTmwL6HkYz93u3Au
"""

data = pd.read_csv("/content/president_heights.csv")
print(data.head())

We’ll use the Pandas package to read the file and extract this information (note that the heights are measured in centimeters):

height = np.array(data["height(cm)"])
print(height)

Now that we have this data array, we can compute a variety of summary statistics:

print("Mean of heights =", height.mean())
print("Standard Deviation of height =", height.std())
print("Minimum height =", height.min())
print("Maximum height =", height.max())

Note that in each case, the aggregation operation reduced the entire array to a single summarizing value, which gives us information about the distribution of values. We may also wish to compute quantiles:

print("25th percentile =", np.percentile(height, 25))
print("Median =", np.median(height))
print("75th percentile =", np.percentile(height, 75))

We see that the median height of US presidents is 182 cm, or just shy of six feet. Of course, sometimes it’s more useful to see a visual representation of this data, which we can accomplish using tools in Matplotlib:

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

plt.hist(height)
plt.title("Height Distribution of Presidents of USA")
plt.xlabel("height(cm)")
plt.ylabel("Number")
plt.show()