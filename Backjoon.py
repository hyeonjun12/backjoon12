#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input())
for i in range(1,10):
    print(n,"*",i,"=",n*i)


# In[19]:


t=int(input())
a=[]
b=[]
for i in range(t):
    A,B=map(int, input().split())
    a.append(A)
    b.append(B)
for i in range(t):
    print(a[i]+b[i])


# In[16]:


n=int(input())
sum=0
for i in range(n+1):
    sum=sum+i
print(sum)


# In[3]:


import sys
inp=int(input())
for i in range(inp):
    a,b=map(int, sys.stdin.readline().split())
    print(a+b)


# In[6]:


import sys
inp=int(sys.stdin.readline())
for i in range(1,inp+1):
    print(i)


# In[7]:


import sys
inp=int(sys.stdin.readline())
for i in range(1,inp+1):
    print(inp-i+1)


# In[ ]:


t=int(input())
a=[]
b=[]
for i in range(t):
    A,B=map(int, input().split())
    a.append(A)
    b.append(B)
for i in range(t):
    print("Case #{}:".format(i+1),a[i]+b[i])


# In[ ]:


t=int(input())
a=[]
b=[]
for i in range(t):
    A,B=map(int, input().split())
    a.append(A)
    b.append(B)
for i in range(t):
    print("Case #{}:".format(i+1),a[i],"+",b[i],"=",a[i]+b[i])


# In[ ]:


t=int(input())
for i in range(1,t+1):
    print("*"*i)


# In[ ]:


t=int(input())
for i in range(1,t+1):
    print(" "*(t-i)+"*"*i)


# In[ ]:




