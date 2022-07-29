#Remove multiple elements from a list in Python

#Let’s say we want to delete each element in the list which is divisible by 2 or all the even numbers. 
 
list1 = [12, 5, 17, 18, 19, 50]
 
for ele in list1:
    if ele % 2 == 0:
        list1.remove(ele)
print("New list after removing all even numbers: ", list1)