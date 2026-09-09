# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 08:12:56 2026

@author: user
"""

College = ["JAIN","CHRIST","JSS","RV","RRMC"]

print("original list:", College)

#LENGTH
print("Length of the list:",len(College))

#append
College.append("PES")
print(College)

#insert
College.insert(2, "BMS")
print(College)

#count
print("Count of CHRIST:", College.count("CHRIST"))

#copy
College2 = College.copy()
print(College2)

#reverse
College.reverse()
print(College)

#remove
College.remove("JSS")
print(College)

#pop
College.pop()
print(College)

#index
print(College.index("CHRIST"))

#extend
College.extend(["PES", "BMS"])
print(College)

#max
print("Maximum:", max(College))

#min
print("Minimum:", min(College))

#sort
College.sort()
print("Sorted list:", College)

#clear
College.clear()
print("Cleared list:", College)
     







