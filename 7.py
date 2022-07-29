# Python program to remove Nth occurrence of the given word

def RemoveIthWord(lst, word, N):
    newList = []
    count = 0

    for i in lst:
        if(i == word):
            count = count + 1
            if(count != N):
                newList.append(i)
        else:
            newList.append(i)

    lst = newList

    if count == 0:
        print("Item not found")
    else:
        print("Updated list is: ", lst)

    return newList

list = ["shivam", "kumar", "jha"]
word = "kumar"
N = 1

RemoveIthWord(list, word, N)
