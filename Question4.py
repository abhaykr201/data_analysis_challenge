import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import ast


df=pd.read_csv("data.csv")

df_sweden1 = df[df['Country']=='Sweden']
df_sweden1 = df_sweden1[df_sweden1['Year'] ==1990]
df_sweden1.reset_index(inplace=True)
df_sweden1['average'] = pd.DataFrame(df_sweden1['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'].str.split(" ").tolist(), columns="average rest".split()).average.apply(ast.literal_eval)

df_sweden2 = df[df['Country']=='Sweden']
df_sweden2 = df_sweden2[df_sweden2['Year'] ==2015]
df_sweden2.reset_index(inplace=True)
df_sweden2['average'] = pd.DataFrame(df_sweden2['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'].str.split(" ").tolist(), columns="average rest".split()).average.apply(ast.literal_eval)
plt.bar('Sweden',df_sweden1['average']/df_sweden2['average'] )



df_japan1 = df[df['Country']=='Japan']
df_japan1 = df_japan1[df_japan1['Year'] ==1990]
df_japan1.reset_index(inplace=True)
df_japan1['average'] = pd.DataFrame(df_japan1['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'].str.split(" ").tolist(), columns="average rest".split()).average.apply(ast.literal_eval)

df_japan2 = df[df['Country']=='Japan']
df_japan2 = df_japan2[df_japan2['Year'] ==2015]
df_japan2.reset_index(inplace=True)
df_japan2['average'] = pd.DataFrame(df_japan2['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'].str.split(" ").tolist(), columns="average rest".split()).average.apply(ast.literal_eval)
plt.bar('Japan',df_japan1['average']/df_japan2['average'] )



df_norway1 = df[df['Country']=='Norway']
df_norway1 = df_norway1[df_norway1['Year'] ==1990]
df_norway1.reset_index(inplace=True)
df_norway1['average'] = pd.DataFrame(df_norway1['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'].str.split(" ").tolist(), columns="average rest".split()).average.apply(ast.literal_eval)

df_norway2 = df[df['Country']=='Norway']
df_norway2 = df_norway2[df_norway2['Year'] ==2015]
df_norway2.reset_index(inplace=True)
df_norway2['average'] = pd.DataFrame(df_norway2['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'].str.split(" ").tolist(), columns="average rest".split()).average.apply(ast.literal_eval)

plt.bar('Norway',df_norway1['average']/df_norway2['average'] )
plt.savefig("Question4_")
plt.show()

