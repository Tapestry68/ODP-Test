import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('netflix_titles.csv', encoding='utf-8')
data_p = data.groupby(data['release_year'])['release_year'].count()

print(data_p)
fig, ax = plt.subplots()

ax.boxplot(data.groupby('release_year').count())
ax.set_ylim(0.0, 1100.0)
ax.set_xlabel('Release_year')
ax.set_ylabel('count')
plt.show
