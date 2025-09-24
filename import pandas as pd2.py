import pandas as pd
S_data = [["Ahmed" , "A" , "Pass"], ["Mona" , "D" , "Fail"], ["Asser" , "A+" , "Pass"]]
df2 = pd.DataFrame(S_data , columns=['Student', 'Grade', 'Pass/Fail'])
print(df2)
print(df2.loc[1])
print(df2.loc[df2["Pass/Fail"] == "Pass"])
