#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1=["apple","orange","mango"]
for i in list1:
    r=0
    m=0 
    n=0
    l=0
    p=0
    for j in i:
        match j:
            case 'a':r+=1
            case 'e':m+=1
            case 'i':n+=1
            case 'o':l+=1
            case 'u':p+=1
            case default:continue
    print("for:",i)
    print("a:",r,end=" ")
    print("e:",m,end=" ")
    print("i:",n,end=" ")
    print("O:",l,end=" ")
    print("u:",p,end=" ")
    print("total vowel in",i,"is:",r+m+n+l+p)
    print("")


# In[ ]:




