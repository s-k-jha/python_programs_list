#string is palindrone or not
def isPalindrome(s):
    return s == s[::-1]
 
s = "radar"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")