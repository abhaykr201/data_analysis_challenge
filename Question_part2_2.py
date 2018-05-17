import csv
import ast
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_data = pd.read_csv("data.csv")

df_xmart = pd.read_csv("xmart.csv")
df_xmart1=df_xmart[['DimensionMemberCode','DisplayString','WORLD_BANK_INCOME_GROUP']]
df_xmart1['Country'] = df_xmart1[['DisplayString']]
df_xmart1.drop(['DisplayString'], axis=1, inplace=True)
result = pd.merge(df_data, df_xmart1, how='left', on='Country')


result_merge = result[['WORLD_BANK_INCOME_GROUP','Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)']]
df_dm = pd.DataFrame(result_merge['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'].str.split(" ").tolist(), columns="average rest".split())
df_dm['WORLD_BANK_INCOME_GROUP'] = result_merge[['WORLD_BANK_INCOME_GROUP']]
df_dm.drop(['rest'], axis=1, inplace=True)
graph = df_dm.groupby(["WORLD_BANK_INCOME_GROUP"], as_index=False).count()


plt.bar(graph['WORLD_BANK_INCOME_GROUP'], graph['average'])
plt.title("Infant mortality rate by WORLD_BANK_INCOME_GROUP")
plt.ylabel("mortality rate")
plt.xlabel("WORLD_BANK_INCOME_GROUP")
plt.savefig("Question_part2_2_1")
plt.show()

total_avg = graph['average'].sum()
graph['relative_avg'] = graph['average']/total_avg

plt.bar(graph['WORLD_BANK_INCOME_GROUP'], graph['relative_avg'])
plt.title("relative Infant mortality rate by WORLD_BANK_INCOME_GROUP")
plt.ylabel("relative mortality rate")
plt.xlabel("WORLD_BANK_INCOME_GROUP")
plt.savefig("Question_part2_2_2")
plt.show()
