s=input("enter a string: ")

reverse=""
for i in s:
    reverse=i+reverse
    s=reverse
print(reverse)