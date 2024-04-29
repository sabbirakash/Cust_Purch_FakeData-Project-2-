#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"G:\Data Science Project\Assignments\Assignment-10(17.11.23)\Cust_Purch_FakeData.csv")
df


# 1.	How many entries your data have? Can you tell the no. of columns in your data?

# In[4]:


df.info()


# 2.	What are the max and min ages of your customer? Can you find mean of your customer?

# In[7]:


print("The Max of age is :",df.age.max())
print("The Min of age is :",df.age.min())
print("The Avg of age is :",df.age.mean())


# 3.	What are the three most common customer's names?

# In[9]:


df["first"].value_counts().head(3)


# 4.	Two customers have the same phone number, can you find those customers?

# In[23]:


df[df.phone.duplicated(keep = False)]


# In[22]:


df[df.duplicated(subset='phone', keep = False)]


# 5.	How many customers have profession "Structural Engineer"?

# In[26]:


df[df["profession"] == "Structural Engineer"].count()[0]


# 6.	How many male customers are 'Structural Engineer'?

# In[28]:


df[(df["profession"] == "Structural Engineer") & (df["gender"] == "Male")].count()[0]


# In[ ]:





# 7.	Find out the female Structural Engineers from province Alberta (AB)?

# In[31]:


df[(df["profession"] == "Structural Engineer") & (df["gender"] == "Female") & (df["province"] == "AB")]


# 8.	What is the max, min and average spending?

# In[32]:


print("The Max speding is :", df["price(CAD)"].max())
print("The Min speding is :", df["price(CAD)"].min())
print("The Avg speding is :", df["price(CAD)"].mean())


# 9.	Who did not spend anything? Company wants to send a deal to encourage the customer to buy stuff!

# In[34]:


df[df["price(CAD)"] == df["price(CAD)"].min()]


# 10.	As a loyalty reward, company wants to send thanks coupon to those who spent 100CAD or more, please find out the customers?

# In[36]:


df[df["price(CAD)"] >= 100.0]


# 11.	How many emails are associated with this credit card number '5020000000000230'?

# In[43]:


df[df["cc_no"] == 5020000000000230]["email"]


# 12.	We need to send new cards to the customers well before the expire, how many cards are expiring in 2019?

# In[62]:


df["cc_exp"] = pd.to_datetime(df["cc_exp"])


# In[71]:


df[df["cc_exp"] <= "12/31/2019"].count()[0]


# In[57]:


df[df["cc_exp"].apply(lambda x: x[5:])== "19"].count()[0]


# 13.	How many people use Visa as their Credit Card Provider?

# In[50]:


df[df["cc_type"] == "Visa"].count()[0]


# 14.	Can you find the customer who spent 100 CAD using Visa?

# In[51]:


df[(df["price(CAD)"] == 100) & (df["cc_type"] == "Visa")]


# 15.	What are two most common professions?

# In[53]:


df["profession"].value_counts().head(2)


# 16.	Can you tell the top 5 most popular email providers? (e.g. gmail.com, yahoo.com, etc...)

# In[88]:


df['email_provider'] = df['email'].apply(lambda x: x.split('@')[1])
email_provider_counts = df['email_provider'].value_counts()
top_5_email_providers = email_provider_counts.nlargest(5)
print(top_5_email_providers)


# 17.	Is there any customer who is using email with "am.edu"?

# In[72]:


has_am_edu_email = df['email'].apply(lambda x: 'am.edu' in x)

customers_with_am_edu_email = df[has_am_edu_email]

print(customers_with_am_edu_email)


# In[77]:


def find_email(x):
    if "am.edu" in x:
        return True
    else:
        return False


# In[81]:


df[df["email"].apply(find_email)]


# 18.	Which day of the week, the store gets more customers?

# In[87]:


df["weekday"].value_counts().head(1)

