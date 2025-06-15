def pal(s):
    return s == s[::-1]
s=input("Enter a string: ")

if pal(s):
    print("Palindrome")
else:
    print("Not Palindrome") 