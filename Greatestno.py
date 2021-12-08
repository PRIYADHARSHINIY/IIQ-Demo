#!/usr/bin/env python
# coding: utf-8

# In[7]:


A=[]
n=int(input('n='))
for i in range (n):
    num=int(input())
    A.append(num)
print("Greatest among",n ,"numbers is", max(A))

