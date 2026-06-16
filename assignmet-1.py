#Create a new list containing the names of 5 different cities
l1=["hyderabad","bengaluru","mumbai","chennai","delhi"]
middle=len(l1)//2
#Use indexing to access and print the name of the city at the middle index of the list
print(l1[middle])
# Use slicing to extract a subset of cities from the list (e.g., the first 3 cities) and print the result
print(l1[:3])
#Sort the list of cities in ascending order and print the result
l1.sort()
print(l1)
# Append a new city to the end of the list and print the updated list
l1.append("tirupati")
print(l1)
# Remove the first city from the list and print the updated list
l1.pop(0)
print(l1)
#Write a function that takes a list of cities as input and returns the length of the list
count=0
for i in l1:
    count+=1
print("length of the list is ",count)
#or
def count_citys(citys):
    return len(citys)
print(count_citys(l1))
# Test the function with the list of cities created in the first task and print the result
# for i in l1:
#     print(i)
# or
def city(citys):
    return citys
print(city(l1))