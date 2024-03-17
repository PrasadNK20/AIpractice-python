#!/usr/bin/env python
# coding: utf-8

# ### TASKS - Titanic data

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
sns.set_theme()
import matplotlib.pyplot as plt

# Load the titanic dataset into a DataFrame
df = pd.read_csv('titanic.csv')
df


# 
# 1. Line Plot:
#    * Task 1: Create a line plot showing the trend of average age of passengers based on their travel class (1st, 2nd, and 3rd).
# 
#    * Task 2: Create a line plot showing the trend of survival rate of passengers based on their age group (child, adult, elderly).
# 
# 2. Scatter Plot:
#    * Task 1: Visualize the relationship between age and fare paid by passengers. Additionally, differentiate the points by their survival status (survived vs. not survived).
# 
#    * Task 2: Create a scatter plot showing the relationship between age and fare paid by passengers, differentiated by their gender (male vs. female).
#   
# 3. Bar Plot:
#    * Task 1: Plot a bar plot showing the count of passengers who survived and who did not survive based on their gender (male vs. female).
#    
#    * Task 2: Plot a bar plot showing the count of passengers who survived and who did not survive based on their travel class (1st, 2nd, and 3rd).
# 
# 4. Box Plot:
#    * Task 1: Visualize the distribution of fares paid by passengers based on their embarkation port (Cherbourg, Queenstown, Southampton).
#   
#    * Task 2: Visualize the distribution of ages of passengers based on their survival status (survived vs. not survived).

# In[27]:


plt.figure(figsize=(10, 6))   #Figure size (width, height)
plt.plot(df['Pclass'], df['Age'], marker = '*', color ='green', linestyle = '--')
plt.title('Travel class v/s Age') #Title of graph
plt.xlabel('Class')  #X axis label
plt.ylabel('Age')   #Y axis label
plt.grid(True)  #Adding grids to the plot  
plt.xticks(rotation = 30)   #Rotating the x axis labels
plt.show()   #Printing the graph


# In[28]:


sns.lineplot(x = df['Pclass'], y = df['Age'])
plt.show()


# In[9]:


sns.lineplot(x = df['Age'], y = df['Survived'])
plt.show()
#sns.lineplot(x='day', y='total_bill', data=tips, hue='sex')
#plt.title('Line plot: Total bill by day (Differentiated by gender)')
#plt.show()


# In[11]:


#Plot of Age vs Fare
sns.scatterplot(x = df['Age'], y = df['Fare'], data=df, hue='Survived')


# In[ ]:





# In[17]:


#Survival based on the sex
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Bar plot: Surival based on the Gender')
plt.show()


# In[ ]:





# In[21]:


#plot of survival based on the passenger class
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Bar plot: Surival based on the Gender')
plt.show()


# In[22]:


#Visualize the distribution of fares paid by passengers based on their embarkation port (Cherbourg, Queenstown, Southampton).
sns.boxplot(x='Embarked', y='Fare', data=df) 
plt.title('Box plot: Embark vs Fare')
plt.show()


# In[25]:


#Visualize the distribution of ages of passengers based on their survival status (survived vs. not survived).
sns.boxplot(x='Survived', y='Age', data=df) 
plt.title('Box plot: Survial based on the age')
plt.show()


# In[ ]:




