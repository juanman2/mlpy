#!/usr/bin/env python
# coding: utf-8

# This exercise will require you to pull some data from the Qunadl API. Qaundl is currently the most widely used aggregator of financial market data.

# As a first step, you will need to register a free account on the http://www.quandl.com website.

# After you register, you will be provided with a unique API key, that you should store:

# In[ ]:



# In[51]:


# First, import the relevant modules
import requests
import json
import time
import sys
import matplotlib.pyplot as plt


# In[52]:


# Now, call the Quandl API and pull out a small sample of the data (only one day) to get a glimpse
# into the JSON structure that will be returned



URL="https://www.quandl.com/api/v3/datasets/CFTC/0233CV_FO_L_ALL_CR.json?api_key={:s}&".format(key)
parameters = {'start_date': '2020-01-01', 'end_date':'2020-12-31'}
response = requests.get(URL, params=parameters)
if response.status_code != 200:
   raise Exception("Response was code " + str(response.status_code))
responseStr = response.text
data = json.loads(response.text)

print(data['dataset'].keys())
type(data['dataset']['data'])
print(len(data['dataset']['data']))
print(len(data['dataset']))


# In[53]:


# Inspect the JSON structure of the object you created, and take note of how nested it is,
# as well as the overall structure


# These are your tasks for this mini project:
# 
# 1. Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD).
# 2. Convert the returned JSON object into a Python dictionary.
# 3. Calculate what the highest and lowest opening prices were for the stock in this period.
# 4. What was the largest change in any one day (based on High and Low price)?
# 5. What was the largest change between any two days (based on Closing Price)?
# 6. What was the average daily trading volume during this year?
# 7. (Optional) What was the median trading volume during this year. (Note: you may need to implement your own function for calculating the median.)

# In[54]:



smin = sys.float_info.max
lmin = sys.float_info.max
dmin = sys.float_info.max

smax = 0.0
lmax = 0.0
dmax = 0.0

dsum = 0.0
dlist = []

for d in data['dataset']['data']:
    smin = min(smin, d[2])
    smax = max(smax, d[2])
    lmin = min(lmin, d[1])
    lmax = max(lmax, d[1])
    
    dif = abs(d[1]-d[2])
    dmax = max(dmax, dif)
    dmin = min(dmin, dif)
    dsum += dif
    dlist.append(dif)
    
    print(d[0], d[1], d[2]) 

ave_dif = dsum / len(data['dataset']['data'])
print("Max long in 2020 was: {:.2f}".format(lmax))
print("Min long in 2020 was: {:.2f}".format(lmin))
print("Max short in 2020 was: {:.2f}".format(smax))
print("Min short in 2020 was: {:.2f}".format(smin))
print("Max differential in 2020 was: {:.2f}".format(dmax))
print("Min differential in 2020 was: {:.2f}".format(dmin))
print("Ave differential in 2020 was: {:.2f}".format(ave_dif))

print(len(dlist))


# In[67]:


def median(dlist):
    for i in dlist:
        print("{:.2f}".format(i))
        
    if len(dlist)%2 == 0: # even
        h = int(len(dlist)/2)
        return (dlist[h-1]+dlist[h])/2
    else:
        return (dlist[int(len(dlist)/2) + 1])

median_d = median(sorted(dlist))
median_d


# In[68]:


print("Median differential is {:.2f}".format(median_d))


# In[58]:


plt.plot(dlist)
plt.xlabel("2020 (months)")
plt.ylabel("differential")
plt.show()


# In[ ]:




