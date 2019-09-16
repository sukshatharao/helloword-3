#!/usr/bin/env python
# coding: utf-8

# In[94]:



import re
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

code_dict = dict()
bng_calls_recieved = 0

for row in calls:
    calling_no= re.search('\(\d[0-9]*\)',row[0])
    recieving_no = re.search("^140|\d[0-9]*\)|^7\d{3}|^8\d{3}|^9\d{3}",row[1])
    if calling_no is not None and calling_no.group() == '(080)' :
        bng_calls_recieved += 1
        if recieving_no is not None:
            r= recieving_no.group().split(')')[0]
            if r not in code_dict:
                code_dict[r] = 1
            else:
                code_dict[r] = code_dict[r]+1

print("The numbers called by people in Bangalore have codes:")
for val in sorted(code_dict):
    print(val)

#print("The telephone codes being called to, by the Banaglore '080' fixed line are following:", sorted(code_dict))
#print("\nCalls recieved by Bangalore fixed line number:", bng_calls_recieved)
#print("\n\n% calls from fixed line in BNG to fixed line in BNG :",code_dict['(080)']/bng_calls_recieved *100)
print("\n{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(code_dict['080']/bng_calls_recieved *100))


# In[ ]:





# In[ ]:




