# Amirthavarshini V (21105)
# Question - 4
# Convert the first character of each element in a series to uppercase

import pandas as pd
l = input("Enter your series of words in a list format : ")
s = pd.Series(l)
print("Result after capitalising each element of the series: ")
print(s.str.title())
