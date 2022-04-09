#!/usr/bin/env python
# coding: utf-8

# In[12]:


a, b = map(int,input().split(' '))
if a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("==")


# In[14]:


score=int(input())
if 90<=score<=100:
    print("A")
elif 80<=score<=89:
    print("B")
elif 70<=score<=79:
    print("C")
elif 60<=score<=69:
    print("D")
else:
    print("F")


# In[17]:


year=int(input())
if year%4==0:
    if year%100!=0 or year%400==0:
        print("1")
else:
    print("0")
    


# In[20]:


x=int(input())
y=int(input())
if x>0 and y>0:
    print("1")
elif x<0 and y>0:
    print("2")
elif x<0 and y<0:
    print("3")
elif x>0 and y<0:
    print("4")


# In[21]:


h,m = input().split()
h = int(h)
m=int(m)
if m>=45:
    print(h, m-45)
else:
    if h==0:
        print(23, 15+m)
    else:
        print(h-1, 15+m)


# In[25]:


h, m =map(int,input().split())
t=int(input())
if t>=60:
    h=h+t//60
    m=m+(t-(60*(t//60)))
    if m>=60:
        h=h+1
        m=60-m
elif m+t>=60:
    h=h+1
    m=m+t-60
else:
    m=m+t
if h>=24:
    h=h-24
print(h,m)
    
    


# In[28]:


a,b,c=map(int, input().split())
if a==b!=c:
    print(1000+a*100)
elif b==c!=a:
    print(1000+b*100)
elif a==c!=b:
    print(1000+a*100)
elif a<b<c or b<a<c:
    print(c*100)
elif c<b<a or b<c<a:
     print(a*100)
elif a<c<b or c<a<b:
     print(b*100)
else:
    print(10000+a*1000)


# In[ ]:




