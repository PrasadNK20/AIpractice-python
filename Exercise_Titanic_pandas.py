#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv('titanic.csv')
df


# 1. Load the Titanic dataset into a DataFrame.
#     * Check the shape of dataframe
#     * Check the size of dataframe
#     * Check the columns of dataframe
# 2. Perform the following querying operations:
#     * Filter passengers who survived the Titanic disaster.
#     * Filter passengers who did not survive the Titanic disaster.
#     * Filter passengers based on their age, such as passengers younger than 18 years old.
#     * Filter passengers based on their fare, such as passengers who paid more than a certain fare amount.
#     * Filter passengers based on their class (1st, 2nd, or 3rd).
#     * Filter passengers based on their embarkation port (C = Cherbourg, Q = Queenstown, S = Southampton).
# 3. Access values in the DataFrame:
#     * Access the value of a specific cell in the DataFrame, such as the name of the passenger in the 5th row and 3rd column.
#     * Access values in a specific row or column of the DataFrame.
# 4. Check counts in categorical columns:
#     * Calculate the number of passengers in each class (1st, 2nd, and 3rd).
#     * Calculate the number of male and female passengers.
#     * Calculate the number of passengers embarked from each port (Cherbourg, Queenstown, Southampton).
# 5. Identify unique values:
#     * Find unique values in the 'Sex' column (male, female).
#     * Find unique values in the 'Embarked' column (C, Q, S).
# 6. Describe numeric columns:
#     * Calculate descriptive statistics for the 'Age' column (mean, median, min, max, etc.).
#     * Calculate descriptive statistics for the 'Fare' column (mean, median, min, max, etc.).

# In[7]:


df.shape #shape


# In[6]:


df.size #size rows * columns


# In[8]:


df.columns #columns in the dataset


# In[19]:


df[(df['Survived'] == 1)] #data survived


# In[22]:


df[df['Survived'] == 0] #data not survived


# In[21]:


df[df['Age'] < 18] #passengers age < 18


# In[25]:


df[df['Fare'] > 30.0] #passengers paid more than $30


# In[26]:


df[df['Pclass'] == 1] #Pclass 1


# In[27]:


df[df['Pclass'] == 2] #Pclass 2


# In[29]:


df[df['Pclass'] == 3] #Pclass 3


# In[33]:


df[df['Embarked'] == 'S'] #embardked point S passengers


# In[36]:


df


# In[40]:


df.loc[4][2] #5th row and 3rd col


# In[38]:


df.head(10)


# In[41]:


df['Name']


# In[48]:


df[df.columns[2]]


# In[50]:


value_count = df['Pclass'].value_counts() #number of passengers in each class


# In[51]:


print(value_count) 


# In[52]:


value_count = df['Sex'].value_counts() #Number of males and Females
print(value_count)


# In[53]:


print(df['Embarked'].unique()) #unique values


# In[54]:


print(df['Sex'].unique()) #unique values


# In[55]:


df['Age'].describe() #stats of Age


# In[56]:


df['Fare'].describe() #stats of Age


# In[57]:


df['Age'].median()


# In[58]:


df['Fare'].median()


# In[ ]:




