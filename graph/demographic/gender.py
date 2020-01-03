import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np
import string
import csv

inputName = sys.argv[1]
outputName = "demog2.csv"

sheet = pd.read_csv(inputName)
sheet2 = sheet.groupby("Q10")\
    .agg({"Q13":'size'}) \
    .rename(columns={'Q13': 'Counts'}) \
    .reset_index()

print(sheet)


sns.set(style="darkgrid")
ax = sns.barplot(x="Counts", y="Q10", data = sheet2, palette ="husl")
ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax.set(xlabel='Counts', ylabel='Gender')
plt.title('Participants Gender')
plt.show()