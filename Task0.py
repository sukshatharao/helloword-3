#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
#print("calls last row", calls[-1]);

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

#print("texts first row",texts[0]);

txt = []
call = []

txt = list(texts[0])
call = list(calls[-1])
print("First record of texts, {} texts {} at time {}".format(txt[0], txt[1], txt[2]))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(call[0], call[1], call[2], call[3]))


# In[ ]:




