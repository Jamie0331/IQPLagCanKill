import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np
import string
import csv

inputName = sys.argv[1]
outputName = inputName

sheet = pd.read_csv(inputName)
sheet = sheet[sheet.Counts <= 25]


print(sheet)

sns.set(style="darkgrid")
ax = sns.boxplot(x="Ping", y="Counts", data=sheet)

ax.text(x=0.5, y=1.1, s='Sushi Shooter: Added Lag vs Lag (space bar)', fontsize=14, weight='bold', ha='center', va='bottom', transform=ax.transAxes)
ax.text(x=0.5, y=1.02, s='Boxplot: distribution of all participants', fontsize=11, alpha=0.75, ha='center', va='bottom', transform=ax.transAxes)
ax.set(xlabel='Added Lag (milliseconds)', ylabel='Number of Lag (space bar)')
plt.show()

#sheet.to_csv(outputName, index=False)