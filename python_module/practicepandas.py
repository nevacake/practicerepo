import pandas as pd
# dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
#        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
#        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
#        "population": [200.4, 143.5, 1252, 1357, 52.98] }


# brics = pd.DataFrame(dict)
# print(brics)

# # Set the index for brics
# brics.index = ["BR", "RU", "IN", "CH", "SA"]

# # Print out brics with new index values
# print(brics)

periodictable = pd.read_csv("test.csv")
# find stuff liek this --> print(periodictable["AtomicNumber"]) or print(periodictable[["AtomicNumber"]])
# print(periodictable)
# print(periodictable[0:12])
# print(periodictable.iloc[2])
# print(periodictable.loc[[20]])
