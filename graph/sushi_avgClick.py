import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np
import string
import csv

inputName = sys.argv[1]
outputName = "avg"+inputName

sheet = pd.read_csv(inputName).groupby(["Ping", "Type"]) \
    .agg({'Counts':'mean'}) \
    .rename(columns={'Counts' : 'Clicks'}) \
    .reset_index()

print(sheet)

sns.set(style="darkgrid")
ax = sns.barplot(x="Ping", y="Clicks", data=sheet, alpha=0.8)

plt.title('Sushi Shooter: Ping vs Average_Click_Counts')
plt.show()

#sheet.to_csv(outputName, index=False)