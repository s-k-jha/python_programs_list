def dictionary():
  
    key_value = {}
 
    key_value[1] = 2
    key_value[2] = 4
    key_value[5] = 6
    key_value[3] = 8
    key_value[6] = 10
    key_value[4] = 12
    print("Task 1")
 
    print("key_value", key_value)
 

    for i in sorted(key_value.keys()):
        print(i , end=" ")
 
def main():
    dictionary()
if __name__ == "__main__":
    main()