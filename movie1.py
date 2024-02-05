# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:15:18 2024

@author: 20090187
"""

import pandas as pd

df = pd.read_csv("movie_dataset.csv")


df = pd.read_csv("movie_dataset.csv",index_col=0)


avg_met = df["Metascore"].mean()
df["Metascore"].fillna(avg_met, inplace = True)



avg_rev = df["Revenue (Millions)"].mean()
df["Revenue (Millions)"].fillna(avg_rev, inplace = True)

print(df.info())

print(df['Rating'].max())

print(df["Revenue (Millions)"].sum())

#df = df[df['Year'] == 2006]


#df = df[df['Year'] > 2015]

#df = df[df['Director'] == "Christopher_Nolan"]

# #df = df[df['Rating'] > 7.9]

#df = df[df['Title'] == 2016]


print(df.info())

df.to_csv("cleanedmovie_dataset.csv")

"""

# df.dropna(inplace = True)


df = df[df['Rating'] > 7.9]

print(df.info())


df = pd.read_csv("movie_dataset.csv",index_col=0)

print(df.info())





print(df)

print(df.info())


print(df.describe())



df = pd.read_csv("movie_dataset.csv",index_col=0)
         
df.dropna(inplace = True)

df = df.reset_index(drop=True)


print(df)


print(df.info())

print(df)

print(df["Rating"])

print(df['Rating'].max())


print(df.info())

# print(df.columns)

col_names = df.columns.tolist()

print(col_names)

# print(df["Revenue (Millions)"].sum())

# df = df[df['Year'] > 2015]

# print(df.info())

#df = df[df['Director'] == "Christopher_Nolan"]

#print(df.info())

# print(df.describe())


#df = df[df['Rating'] > 7.9]

#print(df.info())


df.to_csv("output/pulsar_dataset.csv")

"""














































