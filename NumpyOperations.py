#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Notesfornumpy

import numpy as np
import numpy.linalg as LA


# In[2]:


A = np.array([[1,0,2,5, -6],[1,2,1,0,2],[4,0,3,2,1], [3,-1,5,1,2],[0,5,0,0,2]])
A


# In[4]:


#finding_the_sum_of_all_elements_in_arrays

ans_1 = np.sum(A)


# In[5]:


print(ans_1)


# In[6]:


#matrix_operations

B_1= np.array([[-7, 0,  3, 0],
       [ 7,  0,  4,  0],
       [ 0, 12,  0,  1]])
B_2 = np.array([[  6,  -3,  0,  10],
       [ 8,   0,  2,   2],
       [-1,  11,  4,  8]])


# In[7]:


C=B_1-B_2


# In[8]:


print(C)


# In[10]:


B_3=np.array([[  6,  -3, 10],
       [ 8,   0,  2],
       [-1,  11,  4]])


# In[14]:


B_4=np.identity(3)
B_5 =B_3-B_4 


# In[15]:


print(B_5)


# In[16]:


#Finding_systems_of_linear_equations

A= np.array([[-7, 0,  3, 0],
       [ 7,  0,  4,  0],
       [ 0, 12,  0,  1],
       [ 3, 1, 2,  1]])


# In[17]:


b=np.array([0,  1,  4,  5])


# In[18]:


invA=np.linalg.inv(A)
x =np.dot(invA,b)


# In[19]:


print(x)


# In[20]:


#Matrix_Decompositions

from scipy.linalg import lu


# In[21]:


C = np.array([[ 12, 3,   2,   2, -11],
       [  1,   4,  1,  11,  -5],
       [ 13,  -5,   9,  12,  -2],
       [  5, -13,  2,   3,   5],
       [ -9,  10,  -1,  6,  7]])
C


# In[25]:


P, L, U = lu(C)


# In[28]:


#assigning_elements_in_array

a = np.array([20, 1, 2, 3, 4])
a


# In[29]:


a[0]=100
#assigning_third_element
a[2]=12


# In[30]:


a


# In[32]:


a.size


# In[33]:


a.ndim


# In[36]:


# Get the standard deviation of numpy array

standard_deviation=a.std()


# In[37]:


print(standard_deviation)


# In[ ]:




