#!/usr/bin/env python
# coding: utf-8

# In[5]:


def fibo(term):
    print("the fibonacci series is : ")
    n1,n2=0,1
    count=0
    
    while count<term:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1


# In[ ]:




