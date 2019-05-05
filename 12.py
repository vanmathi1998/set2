n=int(input("enter the number:"))
rev=0
temp=n
while(temp > 0):
rem=temp%10
rev=(rev*10)+rem
temp=temp//10
print("rev of the given num is %d",,%rev)
if(n==rev):
print("the num is a palindrome",%n)
else:
print("the num is not a palindrome",%n)
