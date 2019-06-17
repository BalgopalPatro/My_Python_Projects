#!/usr/bin/env python
# coding: utf-8

# In[5]:


f=open(input())
d = [line for line in f ]
n = int(d[0])
ans = []
for i in range(1,n+1):
    st = d[i]
    b = st.count('B')
    e = st.count('.')
    if (e != 0 and b >= 2):
        ans.append('Y')
    elif (b == 0 and e != 0 ) or (e == 0 and b!=0) or ( e > b and b < 2): 
        ans.append('N')
    else:
        ans.append('Y')
p = open('output2.txt','w')
for i in range(1,n+1):
    p.write("Case #%i: %c\n"%(i,ans[i-1]))


# In[ ]:




