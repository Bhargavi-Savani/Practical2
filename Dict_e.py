# S_ID: 20CS075 S_NAME: BHARGAVI SAVANI
# Practical2 Study and Learn List, Tuple, Set and Dictionary

# Write a Python script to concatenate following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
N_Dic={}
for i in (dic1,dic2,dic3):
    N_Dic.update(i)
print(N_Dic)