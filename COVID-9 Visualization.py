#!/usr/bin/env python
# coding: utf-8
"""
Created on Wed Oct 27 09:44:29 2021

@author: Jospin Amisi
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#Gathering data and plotting Total World Cases

get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('fivethirtyeight')

#Loading the CSV file
df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv', parse_dates = ['Date'])

#Sum of the total cases (Confirmed, Recovered, Deaths)
df['Total Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)

#Worldwide Cases
worldwide_df = df.groupby(['Date']).sum()
w = worldwide_df.plot(figsize=(16,10))
w.set_xlabel('Date')
w.set_ylabel('# of Cases worldwide')
w.title.set_text('Worldwide COVID Insights')

plt.show()


# Malawi vs. Worldwide Total Cases
mw_df = df[df['Country']=='Malawi'].groupby(['Date']).sum()

fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(111)

ax.plot(worldwide_df[['Total Cases']], label='Worldwide')
ax.plot(mw_df[['Total Cases']], label='Malawi')
ax.set_xlabel('Date')
ax.set_ylabel('# of Total Cases')
ax.title.set_text('Worldwide vs. Malawi Total Cases')

plt.legend(loc='upper left')
plt.show()


# Malawi Daily Cases and Deaths
w_df = mw_df.reset_index()
mw_df['Daily Confirmed'] = mw_df['Confirmed'].sub(mw_df['Confirmed'].shift())
mw_df['Daily Deaths'] = mw_df['Deaths'].sub(mw_df['Deaths'].shift())

fig = plt.figure(figsize=(20,8))
ax = fig.add_subplot(111)

ax.bar(mw_df['Date'], mw_df['Daily Confirmed'], color='b', label='Malawi Daily Confirmed Cases')
ax.bar(mw_df['Date'], mw_df['Daily Deaths'], color='r', label='Malawi Daily Deaths')
ax.set_xlabel('Date')
ax.set_ylabel('# of People Affected')
ax.title.set_text('Malawi Daily Cases and Deaths')

plt.legend(loc='upper left')
plt.show()


# Worst Hit Countries by COVID-19

from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
yesterday.strftime('%Y-%m-%d')

today_df = df[df['Date'] == yesterday]
top_10 = today_df.sort_values(['Confirmed'], ascending=False)[:10]
top_10.loc['rest-of-world'] = today_df.sort_values(['Confirmed'], ascending=False)[10:].sum()
top_10.loc['rest-of-world', 'Country'] = 'Rest of World'

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

ax.pie(top_10['Confirmed'], labels=top_10['Country'], autopct = '%1.1f%%')
ax.title.set_text('Hardest Hit Countries Worldwide')

# This code shows the legend of the graph and plot everything

plt.legend(loc='upper left')
plt.show()




