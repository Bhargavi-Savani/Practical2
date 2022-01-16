# S_ID: 20CS075 S_NAME: BHARGAVI SAVANI
# Practical2 Study and Learn List, Tuple, Set and Dictionary

#  Write a Python program to add member(s) in a set and clear a set

numbers = set()
# To add single member we can use add()/update()
numbers.add("One")
numbers.update({"Two"})
# To add multiple members
numbers.update({"Three","Four","Five"})
print(numbers)
numbers.clear()             # clear() removes all the elements from the list
print(numbers)