#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import math
import numpy as np


# In[32]:





# In[47]:


#Potential barrier
V = float(input('Enter the amount of potential for the well (This will be in electorn volt) \n'))
L = float(input('Enter the width of the potential well (This will be in angstrom) \n'))
m = 9.1093837 * (10**-31)
h = 1.054571817 * (10**-34)
E = np.linspace(0, 1.6e-19, 500)

b =  np.sqrt(2*m*(V*1.6*(10**-19)-i))/h
g = 2*np.sqrt(0.25*(((1-E/V)/(E/V)) + ((E/V)/(1-E/V)) - 2 ))
T = 1/((np.cosh(b*L*(10**-10)))**2 + (g/2)**2 * (np.sinh(b*L*(10**-10)))**2)
plt.plot(T, E)
plt.show()


# In[59]:


#E<V
E = np.linspace(0.1,6,1000)
V = 6

e = E/V
alpha = 0.5
def T(e):
    return 1/(1 + 1/(4*e*(1-e)) * np.sinh(alpha * np.sqrt(1-e))**2)

# plot the function
plt.plot(e ,T(e), 'b')
plt.xlabel("e")
plt.ylabel("T")


# In[ ]:





# In[ ]:




