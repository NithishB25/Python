'''def palindrome(x):
    if x<0:
     return False
    a = x
    rev =0
    while x>0:
       a = x%10
       rev = rev*10+a 
       x//=10
    return a==rev
num= int(input("Enter a number :"))
if palindrome(num):
   print("The given num is palindrome")
else:
   print("The given number is not a palindrome ")
'''

def isPalindrome(x):
    if x < 0:
        return False

    a = x
    rev = 0

    while x > 0:
        d = x % 10
        rev = rev * 10 + d
        x = x // 10

    return a == rev


num = int(input("Enter a number: "))

if isPalindrome(num):
    print(num,"Palindrome",)
else:
    print(num,"Not a Palindrome")