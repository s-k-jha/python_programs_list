#Python program to swap two elements in a list

def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
List = [20,11,21,32]
pos1, pos2  = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))