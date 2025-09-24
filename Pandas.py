import pandas as pd
students_data = [["alice" , 20 ,"A" , 85 ] , ["Bob" , 22 , "B" ,78] ,["Charlie" , 19 ,"A" , 92],[ "David" , 21 , "C" , 65] ,["Eva" , 20 ,"B" , 74]]
df = pd.DataFrame(students_data , columns=["Name" , "Age" , "Grade" , "Marks"])
print(df)
print(df.head(3))
new_DF = df[(df["Name"]) & (df["Marks"])]
print(new_DF)