#!/usr/bin/env python
# coding: utf-8

# 1) Download the data from the file data source and provide possible data insights.

# In[4]:


import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize']=(8,4)


# In[5]:


import warnings
warnings.filterwarnings('ignore')


# In[6]:


df=pd.read_csv(r"C:\Users\jm88\Music\New folder\DataScience\Adapt Ready\complaints.csv")
df.head()


# In[7]:


df.isnull().sum()


# In[49]:


df.shape


# # EDA & Visualazation

# In[9]:


df["Sub-product"].fillna('Others', inplace = True) 
df["Sub-issue"].fillna('Others', inplace = True) 
df["Issue"].fillna('Others', inplace = True) 
df["State"].fillna('Others', inplace = True) 
df["Consumer complaint narrative"].fillna('None', inplace = True) 
df["Company public response"].fillna('None', inplace = True) 
df["Consumer consent provided?"].fillna('None', inplace = True) 
df["Company response to consumer"].fillna('None', inplace = True) 
df["Consumer disputed?"].fillna('None', inplace = True)
#df['Sub-issue'].unique()


# In[10]:


df['Tags'].unique()


# In[11]:


df["Tags"].fillna('Others', inplace = True) 


# In[12]:


df["Tags"].unique()


# In[13]:


df['Tags'].replace("Older American, Servicemember","Older American & Servicemember", inplace = True)


# In[14]:


df["Tags"].unique()


# In[15]:


df1=df.drop(['ZIP code'],axis=1)


# In[16]:


df1.isnull().sum()


# # Data Insights

# # Tags

# In[17]:


df1["Tags"].value_counts()


# In[18]:


import matplotlib
matplotlib.rcParams["figure.figsize"] = (10,4)

Responce = (df1["Tags"].value_counts())[:10]
lab = "Others", "Servicemember","Older American", "Older American & Servicemember"
explode = (0,0,0,0)  
#create bar chart of top 10 teams
Responce.plot(kind='pie', explode=explode , labels = lab,autopct='%1.1f%%', shadow=True, startangle=140)
plt.ylabel("")


# > Analyse compliants using "Tags". 
# 1) Service member is 5.5%.
# 2) Older American is 3.1%.
# 3) Older American & Servicemember is only 0.8%
# 4) Other is 90.6%. So most of the compliants from other Tags.

# # Submitted via

# In[19]:


df1["Submitted via"].value_counts()


# In[20]:


import matplotlib
matplotlib.rcParams["figure.figsize"] = (10,4)

top_10_teams = (df1["Submitted via"].value_counts())

#create bar chart of top 10 teams
top_10_teams.plot(kind='bar',color = "green")


# > Analyse compliants using "Submitted Via". 
# * Most of the compliants Submitted Via "Web". Web submitted counts "4584816".

# # Sub-product

# In[21]:


df1["Sub-product"].value_counts()


# In[22]:


import matplotlib
matplotlib.rcParams["figure.figsize"] = (10,4)

top_10_teams = (df1["Sub-product"].value_counts())[:10]

#create bar chart of top 10 teams
top_10_teams.plot(kind='bar',color = "yellow")


# In[23]:


Total=df1["Sub-product"].count()
value = (3069348/Total)*100
value


# > Analyse compliants using "Sub-Product". 
# * Most of the compliants about "Credit reporting". Credit reporting compliants counts "3069348".
# * Credit reporting compliant is almost 60% in Sub-Product.

# # Product

# In[39]:


df1["Product"].unique()
df1["Product"].value_counts()[:10]


# In[40]:


import matplotlib
matplotlib.rcParams["figure.figsize"] = (10,4)

Responce = (df1["Product"].value_counts())[:10]
lab = "Credit reporting, credit repair services, or other personal consumer reports","Credit reporting or other personal consumer reports","Debt collection","Mortgage","Checking or savings account","Credit card or prepaid card","Credit reporting","Credit card","Student loan","Bank account or service"
explode = (0.1, 0.1, 0.1, 0.1, 0.1,0,0,0,0,0)  
#create bar chart of top 10 teams
Responce.plot(kind='pie', explode=explode , labels = lab,autopct='%1.1f%%', shadow=True, startangle=140)
plt.ylabel("")


# > Analyse compliants using "Product". 
# * Most of the compliants about "Credit reporting, credit repair services, or other personal consumer reports".
# * "Credit reporting and Debt collection" are most of the compliants Products.

# # State

# In[23]:


df1["State"].value_counts()


# In[24]:


import matplotlib
matplotlib.rcParams["figure.figsize"] = (10,4)

State = (df1["State"].value_counts())[:15]

#create bar chart of top 10 teams
State.plot(kind='bar',color = "darkgreen")


# > Analyse compliants using "States". 
# * Most of the compliants raised from FL, CA, TX, GA, NY, PA, IL States.

# # Issue

# In[41]:


df1["Issue"].value_counts()


# In[42]:


Total=df1["Issue"].count()


# In[43]:


#-> Total persentage of "Incorrect information on your report"
value = (1492050/Total)*100


# In[44]:


value


# > Analyse compliants using "Issue". 
# * Incorrect information on your report is 29% in Total Issues.
# # Top 5 issues
# 1) Incorrect information on your report                                                
# 2) Improper use of your report                                                          
# 3) Problem with a credit reporting company's investigation into an existing problem     
# 4) Attempts to collect debt not owed                                                   
# 5) Problem with a company's investigation into an existing problem

# In[29]:


df1["Sub-issue"].value_counts()


# # Timely response?

# In[30]:


df1["Timely response?"].value_counts()


# In[31]:


import matplotlib
matplotlib.rcParams["figure.figsize"] = (8,4)
def autopct_format(values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return '{:.1f}%\n({v:d})'.format(pct, v=val)
        return my_format

s = df1['Timely response?'].value_counts()
plt.pie(s,labels = s.index, autopct=autopct_format(s))


# > Analyse compliants using "Timely Response?".
# * 98.9 % percentage responsed immediatly.

# # Consumer disputed?

# In[32]:


df1["Consumer disputed?"].value_counts()


# In[33]:


import matplotlib
matplotlib.rcParams["figure.figsize"] = (6,2)

disputed = (df1["Consumer disputed?"].value_counts())

#create bar chart of top 10 teams
disputed.plot(kind='barh',color = "black")


# # Company public responce?

# In[34]:


df1["Company public response"].value_counts()


# In[35]:


import matplotlib
matplotlib.rcParams["figure.figsize"] = (10,4)

Responce = (df1["Company public response"].value_counts())[:10]

#create bar chart of top 10 teams
Responce.plot(kind='barh',color = "navy")


# > Analyse compliants using "Company Public Response?".
# * "Company has responded to the consumer and the CFPB and chooses not to provide a public response" is a most of the public responce about company.

# # Company

# In[36]:


df1["Company"].value_counts()


# In[37]:


import matplotlib
matplotlib.rcParams["figure.figsize"] = (10,4)

Responce = (df1["Company"].value_counts())[:10]

#create bar chart of top 10 teams
Responce.plot(kind='bar',color = "cyan")


# > Analyse compliants using "Company".
# # Top 5 Company get most compliants.
# 1) EQUIFAX, INC.                                     
# 2) TRANSUNION INTERMEDIATE HOLDINGS, INC.             
# 3) Experian Information Solutions Inc.                
# 4) BANK OF AMERICA, NATIONAL ASSOCIATION              
# 5) WELLS FARGO & COMPANY

# # Date sent to company

# In[61]:


df["Date sent to company"].value_counts()


# In[65]:


import matplotlib
matplotlib.rcParams["figure.figsize"] = (10,4)

Responce = (df1["Date sent to company"].value_counts())

#create bar chart of top 10 teams
Responce.plot(kind='line',color = "cyan")


# > Analyse compliants using "Date sent to company".
# * Between 30-05-2017 to 02-04-2024 most of the compliants sent to the companies.

# # Consumer consent provided?

# In[66]:


df1["Consumer consent provided?"].value_counts()


# In[39]:


import matplotlib
matplotlib.rcParams["figure.figsize"] = (10,4)

Responce = (df1["Consumer consent provided?"].value_counts())[:10]
lab = "Consent not provided", "Consent provided", "None","Other", "Consent withdrawn" 
explode = (0.1, 0, 0, 0, 0)  
#create bar chart of top 10 teams
Responce.plot(kind='pie', explode=explode , labels = lab,autopct='%1.1f%%', shadow=True, startangle=140)
plt.ylabel("")


# # Company response to consumer

# In[47]:


df1["Company response to consumer"].value_counts()


# In[41]:


import matplotlib
matplotlib.rcParams["figure.figsize"] = (10,4)

Responce = (df1["Company response to consumer"].value_counts())
Responce= Responce.sort_values(ascending=True)

Responce.plot(kind='barh',y= Responce, color = "crimson" )


# In[48]:


Total=df1["Company response to consumer"].count()
value = (3432407/Total)*100
value


# > Analyse compliants using "Company response to consumer".
# # 66.8 % Companies are Closed the compliants with explanation.

# ================================================================================

# In[52]:


df2=df1.sample(n=1048576)
df2.to_csv("complaints_EDA.csv")


# 2. Given an unsorted array of integers, find the length of the longest continuous
# increasing subsequence (subarray).

# In[54]:


def find_len_sub(nums):
    if not nums:
        return 0
    
    max_length = 1
    current_length = 1
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    
    return max_length

# get the input
input1 = list(map(int,input().split())) #[1, 3, 5, 4, 7],[2, 2, 2, 2, 2]

print("Output:", find_len_sub(input1))


# =================================================================================

# 3. Given a list of non negative integers, arrange them such that they form the largest
# number.

# In[57]:


from functools import cmp_to_key

def largest_number(nums):
    def compare(a, b):
        # Concatenate and compare as strings
        return int(b + a) - int(a + b)
    # Convert integers to strings
    nums_str = [str(num) for num in nums]
    nums_str.sort(key=cmp_to_key(compare))  
    # Handle case when the input list contains only zeros
    if nums_str[0] == '0':
        return '0'
    return ''.join(nums_str)

# Get the input
input1 = list(map(int,input().split())) #[10,2], [3, 30, 34, 5, 9]

print("Output:", largest_number(input1))


# =================================================================================

# 4. Store all the &quot;servlet-name&quot;, and &quot;servlet-class&quot; to a csv file from the attached
# sample_json.json file using Python.

# In[58]:


import json
import csv

with open(r"C:\Users\jm88\Music\New folder\DataScience\Adapt Ready\DT A1 sample_json.json", 'r') as json_file:
    data = json.load(json_file)

# get "servlet-name" and "servlet-class" from each entry
servlet_data = []
for servlet in data['web-app']['servlet']:
    servlet_name = servlet['servlet-name']
    servlet_class = servlet['servlet-class']
    servlet_data.append((servlet_name, servlet_class))

with open('servlet_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header
    writer.writerow(['servlet-name', 'servlet-class'])
    # Write the data
    writer.writerows(servlet_data)

print("CSV file created successfully.")


# In[ ]:




