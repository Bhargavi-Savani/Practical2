# S_ID: 20CS075 S_NAME: BHARGAVI SAVANI
# Practical2 Study and Learn List, Tuple, Set and Dictionary
# Repository link: https://github.com/Bhargavi-Savani/Practical2.git

# Write a Python script to check whether a given key already exists in a dictionary.

S_Dict = {0:10,1:20}
C_Key = int(input("Enter the key:" ))                       #Inputs the key to be checked
if(C_Key in S_Dict):                                        # To check whether a given key exists in S_Dict
    print("The given key already exists in dictionary")
else:
    print("The given key doesn't exists in dictionary")