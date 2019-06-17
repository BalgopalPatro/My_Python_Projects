#!/usr/bin/env python
# coding: utf-8

# In[7]:


f=open(input())
d = [line for line in f ]
n = int(d[0])
ans = []
for i in range(1,n+1):
    st = d[i]
    b = st.count('B')
    e = st.count('.')
    if (b == 0 and e != 0 ) or (e > b) or (e == 0 and b!=0) : 
        ans.append('N')#print("Case #%i: N"%(i))
    else:
        ans.append('Y')#print("Case #%i: Y"%(i))
p = open('output1.txt','w')
for i in range(1,n+1):
    p.write("Case #%i: %c\n"%(i,ans[i-1]))


# In[ ]:




