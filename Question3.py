import csv
import ast
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv")

df_sweden = df[df['Country']=='Sweden']
df_sweden = df_sweden[df_sweden['Year'] <= 2015]
df_sweden = df_sweden[df_sweden['Year'] >= 1990]


df_japan = df[df['Country']=='Japan']
df_japan = df_japan[df_japan['Year'] <= 2015]
df_japan = df_japan[df_japan['Year'] >= 1990]

df_norway = df[df['Country']=='Norway']
df_norway = df_norway[df_norway['Year'] <= 2015]
df_norway = df_norway[df_norway['Year'] >= 1990]

df_norway.reset_index(inplace=True)
df_japan.reset_index(inplace=True)
df_sweden.reset_index(inplace=True)

df_sweden['average'] = pd.DataFrame(df_sweden['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'].str.split(" ").tolist(), columns="average rest".split()).average.apply(ast.literal_eval)

df_japan['average'] = pd.DataFrame(df_japan['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'].str.split(" ").tolist(), columns="average rest".split()).average.apply(ast.literal_eval)

df_norway['average'] = pd.DataFrame(df_norway['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'].str.split(" ").tolist(), columns="average rest".split()).average.apply(ast.literal_eval)

plt.plot(df_sweden['Year'], df_sweden['average'] , label = "Sweden")
plt.plot(df_japan['Year'], df_japan['average'] , label = "Japan")
plt.plot(df_norway['Year'], df_norway['average'] , label = "Norway")
plt.title("trends in infant mortality")
plt.ylabel("mortality rate")
plt.xlabel("Year")
plt.legend()
plt.savefig('Question3_')
plt.show()
print(df_sweden)
print(df_japan)
print(df_norway)
